from gurobipy import Model, GRB, quicksum

# Données
z = [2, 9, 6, 8, 5, 4]  # Exemple de vecteur z
w = [0.5, 0.3, 0.2, 0.1, 0, 0]  # Poids décroissants
n = len(z)

# Calcul des poids w_k'
w_prime = [w[k] - (w[k + 1] if k + 1 < n else 0) for k in range(n)]

# Modèle Gurobi
m = Model("OWA")

# Variables
r = m.addVars(n, vtype=GRB.CONTINUOUS, name="r")  # Variables r_k
b = m.addVars(n, n, vtype=GRB.CONTINUOUS, name="b")  # Variables b_ik

# Fonction objectif
m.setObjective(
    quicksum(w_prime[k] * (k * r[k] - quicksum(b[i, k] for i in range(n))) for k in range(n)),
    GRB.MAXIMIZE
)

# Contraintes
for k in range(n):
    for i in range(n):
        m.addConstr(r[k] - b[i, k] <= z[i], f"constr_{i}_{k}")
    for i in range(n):
        m.addConstr(b[i, k] >= 0, f"nonnegativity_b_{i}_{k}")

# Résolution
m.optimize()

# Résultats
print("\nRésultats :")
print("Valeurs des r_k :")
for k in range(n):
    print(f"r_{k + 1} = {r[k].x}")
print("\nValeurs des b_ik :")
for k in range(n):
    for i in range(n):
        print(f"b_{i + 1},{k + 1} = {b[i, k].x}")

# Calcul de la valeur optimale
objective_value = m.objVal
print(f"\nValeur optimale de l'OWA : {objective_value}")
