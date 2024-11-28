# Importer Matplotlib et vérifier son installation
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Matplotlib n'est pas installé. Installation en cours...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt

# Points à représenter
z_x1_star = (118, 20)  # Point correspondant à z(x_1^*)
z_x2_star = (20, 112)  # Point correspondant à z(x_2^*)
z_x_star = (66, 66)    # Point correspondant à z(x^*)
z_x_prime_star = (70, 50)  # Point correspondant à z(x^{\prime*})

# Création du graphique
plt.figure(figsize=(8, 6))
plt.scatter(*z_x1_star, color='red', label="z(x_1*) (max z1)")
plt.scatter(*z_x2_star, color='blue', label="z(x_2*) (max z2)")
plt.scatter(*z_x_star, color='green', label="z(x*) (maxmin)")
plt.scatter(*z_x_prime_star, color='orange', label="z(x'*) (minmax regret)")

# Ajouter une droite entre z(x_1*) et z(x_2*)
plt.plot([z_x1_star[0], z_x2_star[0]], [z_x1_star[1], z_x2_star[1]], color='purple', linestyle='--', label="Ligne entre z(x_1*) et z(x_2*)")

# Annotation des points
plt.annotate("z(x_1*)", z_x1_star, textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate("z(x_2*)", z_x2_star, textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate("z(x*)", z_x_star, textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate("z(x'*)", z_x_prime_star, textcoords="offset points", xytext=(-10,10), ha='center')

# Axes et quadrillage
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Titre et légendes
plt.title("Représentation des points dans le plan z1(x), z2(x)")
plt.xlabel("z1(x)")
plt.ylabel("z2(x)")
plt.legend()
plt.show()
