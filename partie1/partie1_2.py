from gurobipy import *

# Données
projets = range(10)
scenarios = range(2)
utilites = [[70, 18, 16, 14, 12, 10, 8, 6, 4, 2],  # Utilités pour s1
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 70]]  # Utilités pour s2
couts = [60, 10, 15, 20, 25, 20, 5, 15, 20, 60]  # Coûts des projets
budget = 100  # Budget total

# Calcul des z*_i
z_star = []
for i in scenarios:
    # Modèle pour maximiser z_i(x)
    m = Model(f"z_star_{i}")
    x = m.addVars(projets, vtype=GRB.BINARY, name="x")
    m.setObjective(quicksum(utilites[i][j] * x[j] for j in projets), GRB.MAXIMIZE)
    m.addConstr(quicksum(couts[j] * x[j] for j in projets) <= budget, "budget")
    m.optimize()
    z_star.append(m.objVal)

print("\nValeurs de z*_i :")
for i in scenarios:
    print(f"z*_{i+1} = {z_star[i]}")

# Résolution du problème minmax regret
m = Model("minmax_regret")

# Variables de décision : x_j = 1 si le projet j est sélectionné, 0 sinon
x = m.addVars(projets, vtype=GRB.BINARY, name="x")

# Variable auxiliaire R pour le regret maximal
R = m.addVar(vtype=GRB.CONTINUOUS, name="R")

# Mise à jour du modèle
m.update()

# Fonction objectif : minimiser R
m.setObjective(R, GRB.MINIMIZE)

# Contraintes de regret
for i in scenarios:
    m.addConstr(R >= z_star[i] - quicksum(utilites[i][j] * x[j] for j in projets), f"regret_{i}")

# Contrainte de budget
m.addConstr(quicksum(couts[j] * x[j] for j in projets) <= budget, "budget")

# Résolution
m.optimize()

# Résultats
print("\nSolution optimale :")
for j in projets:
    print(f"Projet {j+1} sélectionné :", x[j].x)
print("\nValeur du regret maximal (R) :", R.x)

# Calcul du vecteur z(x*)
z = [sum(utilites[i][j] * x[j].x for j in projets) for i in scenarios]
print("\nVecteur z(x*) :")
for i in scenarios:
    print(f"z_{i+1}(x*) = {z[i]}")
