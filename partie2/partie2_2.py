from gurobipy import Model, GRB, quicksum

# Données
z = [2, 9, 6, 8, 5, 4]  # Exemple de vecteur z
n = len(z)  # Taille du vecteur

# Liste pour stocker les résultats
results = []

# Résolution pour chaque k
for k in range(1, n + 1):
    print(f"\n--- Résolution pour k = {k} ---")
    
    # Modèle Gurobi
    m = Model(f"dual_k_{k}")

    # Variables duales
    r_k = m.addVar(vtype=GRB.CONTINUOUS, name="r_k")
    b = m.addVars(n, vtype=GRB.CONTINUOUS, name="b")

    # Fonction objectif : maximiser k * r_k + sum(b_i)
    m.setObjective(k * r_k + quicksum(b[i] for i in range(n)), GRB.MAXIMIZE)

    # Contraintes : r_k + b_i <= z_i
    for i in range(n):
        m.addConstr(r_k + b[i] <= z[i], f"dual_constr_{i}")

    # Résolution
    m.optimize()

    # Extraction de la valeur de L_k(z)
    L_k = k * r_k.x + sum(b[i].x for i in range(n))
    results.append((k, L_k))

    # Affichage des résultats
    print(f"Pour k = {k}, L_k(z) = {L_k}")

# Résultats finaux
print("\nRésultats finaux :")
for k, L_k in results:
    print(f"k = {k}, L_k(z) = {L_k}")
