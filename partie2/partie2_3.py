# Exemple de vecteur z et des poids décroissants w
z = [2, 9, 6, 8, 5, 4]  # Exemple de vecteur z
w = [0.5, 0.3, 0.2, 0.1, 0, 0]  # Poids décroissants

# Trier le vecteur z dans l'ordre croissant
z_sorted = sorted(z)

# Calcul des poids w_k'
n = len(z)
w_prime = [w[k] - (w[k + 1] if k + 1 < n else 0) for k in range(n)]

# Calcul des L_k(z)
L_k = [sum(z_sorted[:k + 1]) for k in range(n)]

# Calcul de g(x) = somme des w_k' * L_k(z)
g_x = sum(w_prime[k] * L_k[k] for k in range(n))

# Affichage des résultats
print("Vecteur z trié (z_(k)) :", z_sorted)
print("Poids w :", w)
print("Poids w' :", w_prime)
print("Valeurs cumulées L_k(z) :", L_k)
print(f"Valeur de g(x) = {g_x}")
