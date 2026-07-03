import numpy as np
import matplotlib.pyplot as plt
from src.postprocessing.plot_config import configure_matplotlib
configure_matplotlib()

# Définition de la plage de valeurs pour le rapport d'aspect alpha = a/b
alpha = np.linspace(0.2, 4.0, 500)

# Création du graphique
fig, ax = plt.subplots(figsize=(10, 6))

# Tracé pour n = 1 (mode fondamental transversal)
# On fait varier m de 1 à 4 pour voir les transitions de modes
for m in [1, 2, 3, 4]:
    k_n1 = (m / alpha + (1**2) * alpha / m) ** 2
    ax.plot(alpha, k_n1, label=f'm={m}, n=1', linestyle='-', linewidth=2)

# Tracé pour n = 2 (deuxième mode transversal)
# On trace pour m=1 et m=2 à titre de comparaison
for m in [1, 2]:
    k_n2 = (m / alpha + (2**2) * alpha / m) ** 2
    ax.plot(alpha, k_n2, label=f'm={m}, n=2', linestyle='--', linewidth=1.5)

# Configuration des axes et du style
ax.set_xlabel(r"Rapport d'aspect $\alpha = a/b$")
ax.set_ylabel(r"$\frac{N^{\mathrm{cr}} b^2}{\pi^2 D}$")
ax.set_title("Évolution du facteur de flambement en fonction de l'élancement", fontweight='bold')
ax.set_ylim(0, 45)
ax.set_xlim(0.2, 4.0)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

# Ajustement des marges et sauvegarde de l'image
plt.tight_layout()
plt.savefig('./examples/results/flambement_plaques.pdf', dpi=300)

import numpy as np
import matplotlib.pyplot as plt

# Configuration de la grille de la plaque (ex: plaque de dimensions a=2, b=1)
a, b = 2.0, 1.0
x = np.linspace(0, a, 100)
y = np.linspace(0, b, 100)
X, Y = np.meshgrid(x, y)

# Calcul des modes (n=1 dans les deux cas)
W_m1 = np.sin(1 * np.pi * X / a) * np.sin(1 * np.pi * Y / b)  # m=1, n=1
W_m2 = np.sin(2 * np.pi * X / a) * np.sin(1 * np.pi * Y / b)  # m=2, n=1

# Création de la figure pour l'affichage 3D
fig = plt.figure(figsize=(14, 6))

# ---- Sous-graphique 1 : Mode m=1, n=1 ----
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, W_m1, cmap='coolwarm', edgecolor='none', alpha=0.9)
ax1.set_xlabel('$x$', labelpad=10)
ax1.set_ylabel('$y$', labelpad=10)
ax1.set_title('Mode m=1, n=1', fontweight='bold')
ax1.set_zlim(-1, 1)

fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)
plt.tight_layout()
plt.savefig('./examples/results/mode_11.pdf', dpi=300)

# ---- Sous-graphique 2 : Mode m=2, n=1 ----
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, Y, W_m2, cmap='coolwarm', edgecolor='none', alpha=0.9)
ax2.set_xlabel('$x$', labelpad=10)
ax2.set_ylabel('$y$', labelpad=10)
ax2.set_title('Mode m=2, n=1', fontweight='bold')
ax2.set_zlim(-1, 1)

fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)
plt.tight_layout()
plt.savefig('./examples/results/mode_21.pdf', dpi=300)

plt.show()