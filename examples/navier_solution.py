from numpy import sin, pi
import numpy as np
import matplotlib.pyplot as plt
import imageio
from io import BytesIO

# Parameters
a = 1.0
b = 1.0
p0 = 1.0
D = 1.0

# Grid (smaller for speed)
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

Ws = [navier_plate(K) for K in range(1, Kmax+1)]

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

gif_path = "./examples/navier_convergence.gif"
imageio.mimsave(gif_path, frames, fps=2)

# -------------------------
# Convergence metric plot
# -------------------------
errors = []
for k in range(1, Kmax):
    errors.append(np.max(np.abs(Ws[k] - Ws[k-1])))

plt.figure()
plt.plot(range(2, Kmax+1), errors, marker='o')
plt.yscale('log')
plt.xlabel("K")
plt.ylabel("max |W_K - W_{K-1}|")
plt.title("Convergence of Navier solution")
plt.grid(True)
plt.show()

gif_path