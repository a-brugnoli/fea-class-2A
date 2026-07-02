from numpy import pi
import numpy as np
import matplotlib.pyplot as plt
import imageio
from io import BytesIO
from matplotlib.ticker import MaxNLocator
from src.postprocessing.plot_config import configure_matplotlib

configure_matplotlib()

# Parameters
a = 300 # mm
b = 300 # mm
h = 5 # mm

E = 75000 # Pa
nu = 0.3
D = E*h**3/(12*(1-nu**2)) # Pa.mm^3

F = 1000 # N
p0 = F/(a*b) # Pa

# Grid
nx, ny = 50, 50
x = np.linspace(0, a, nx)
y = np.linspace(0, b, ny)
X, Y = np.meshgrid(x, y)

Kmax = 12

def navier_plate(K):
    w = np.zeros_like(X)
    for i in range(K):
        m = 2*i + 1
        for j in range(K):
            n = 2*j + 1
            denom = m * n * ((m/a)**2 + (n/b)**2)**2
            w += np.sin(m*pi*X/a) * np.sin(n*pi*Y/b) / denom
    return -(16 * p0) / (pi**6 * D) * w


# -------------------------
# Convergence solutions
# -------------------------
Ws = [navier_plate(K) for K in range(1, Kmax+1)]

# -------------------------
# Maximum deflection evaluation (NEW)
# -------------------------
x_mid = a / 2
y_mid = b / 2

def navier_center(K):
    w = 0.0
    for i in range(K):
        m = 2*i + 1
        for j in range(K):
            n = 2*j + 1
            denom = m * n * ((m/a)**2 + (n/b)**2)**2
            w += np.sin(m*pi*x_mid/a) * np.sin(n*pi*y_mid/b) / denom
    return -(16 * p0) / (pi**6 * D) * w


w_center_list = np.array([navier_center(K) for K in range(1, Kmax+1)])

w_max = w_center_list[-1]  # best approximation

# coefficient adimensionnel
C_num = w_max * D / (p0 * a**4)

print("=== Navier verification ===")
print(f"w_max (centre) ≈ {w_max:.6e} mm")
print(f"Coefficient C = wD/(p a^4) ≈ {C_num:.6f}")

# -------------------------
# Create GIF frames
# -------------------------
frames = []
for k in range(Kmax):
    fig = plt.figure()
    plt.contourf(X, Y, Ws[k], levels=25)
    plt.title(f"Navier convergence K={k+1}")
    plt.xlabel("x")
    plt.ylabel("y")

    buf = BytesIO()
    plt.savefig(buf, format="png", dpi=120)
    plt.close(fig)
    buf.seek(0)
    frames.append(imageio.v2.imread(buf))

gif_path = "./examples/results/navier_convergence.gif"
imageio.mimsave(gif_path, frames, fps=2)

# -------------------------
# Convergence metric plot
# -------------------------
K_exact = 100
W_exact = navier_plate(K_exact)

errors = []
for ii in range(Kmax):
    errors.append(np.max(np.abs(Ws[ii] - W_exact)))

plt.figure()
plt.plot(np.arange(1, Kmax+1), errors, marker='o')
plt.yscale('log')
plt.xlabel("$k$")
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.ylabel("max $|w_k - w_{\\mathrm{ex}}|$")
plt.title("Error up to $m=2k+1, n=2k+1$")
plt.grid(True)
plt.savefig("./examples/results/navier_convergence_plot.pdf")
plt.show()

gif_path