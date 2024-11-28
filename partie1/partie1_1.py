from gurobipy import *

# Données
projets = range(10)
scenarios = range(2)
utilites = [[70, 18, 16, 14, 12, 10, 8, 6, 4, 2],  # Utilités pour s1
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 70]]  # Utilités pour s2
couts = [60, 10, 15, 20, 25, 20, 5, 15, 20, 60]  # Coûts des projets
budget = 100  # Budget total

# Modèle
m = Model("maxmin")

# Variables de décision : x_j = 1 si le projet j est sélectionné, 0 sinon
x = m.addVars(projets, vtype=GRB.BINARY, name="x")

# Variable auxiliaire t pour la performance minimale
t = m.addVar(vtype=GRB.CONTINUOUS, name="t")

# Mise à jour du modèle
m.update()

# Fonction objectif : maximiser t
m.setObjective(t, GRB.MAXIMIZE)

# Contraintes : t <= z_i(x) pour chaque scénario
for i in scenarios:
    m.addConstr(t <= quicksum(utilites[i][j] * x[j] for j in projets), f"scenario_{i}")

# Contrainte de budget
m.addConstr(quicksum(couts[j] * x[j] for j in projets) <= budget, "budget")

# Résolution
m.optimize()

# Résultats
print("\nSolution optimale :")
for j in projets:
    print(f"Projet {j+1} sélectionné :", x[j].x)
print("\nValeur de la performance minimale (t) :", t.x)
# Calcul du vecteur image z(x*)
z1 = sum(utilites[0][j] * x[j].x for j in projets)
z2 = sum(utilites[1][j] * x[j].x for j in projets)

print("\nVecteur image z(x*) :")
print(f"z1(x*) = {z1}")
print(f"z2(x*) = {z2}")
