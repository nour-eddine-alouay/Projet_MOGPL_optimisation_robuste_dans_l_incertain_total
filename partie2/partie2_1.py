from gurobipy import Model, GRB, quicksum

# Exemple de vecteur z
z = [8, 3, 5, 10, 1, 7]  # Exemple de valeurs
n = len(z)  # Taille du vecteur
k = 3  # Nombre de plus petites valeurs à sélectionner

# Modèle Gurobi
m = Model("maxOWA_linearization")

# Variables binaires a_ik
a = m.addVars(n, vtype=GRB.BINARY, name="a")

# Fonction objectif : minimiser la somme des k plus petites valeurs
m.setObjective(quicksum(a[i] * z[i] for i in range(n)), GRB.MINIMIZE)

# Contraintes
m.addConstr(quicksum(a[i] for i in range(n)) == k, "select_k_values")  # Sélectionner k valeurs

# Résolution
m.optimize()

# Extraction de L_k(z)
L_k = sum(a[i].x * z[i] for i in range(n))

# Résultats
print(f"Les {k} plus petites valeurs de z sont sélectionnées :")
for i in range(n):
    if a[i].x > 0.5:
        print(f"z[{i}] = {z[i]}")

print(f"L_k(z) = {L_k}")
