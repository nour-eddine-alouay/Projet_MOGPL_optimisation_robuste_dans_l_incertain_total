from gurobipy import Model, GRB, quicksum

# Données simplifiées
n = 2  # Nombre de scénarios
p = 2  # Nombre de projets
scenarios = [
    [2, 4],  # Scénario 1
    [3, 1]   # Scénario 2
]
costs = [1, 2]  # Coûts des projets
budget = 3  # Budget maximum
w = [0.6, 0.4]  # Poids décroissants

# Ajustement des poids w pour correspondre à n
if len(w) < n:
    w.extend([0] * (n - len(w)))
elif len(w) > n:
    w = w[:n]

# Modèle Gurobi
m = Model("minOWA_regrets")

# Variables de décision pour les projets sélectionnés
x = m.addVars(p, vtype=GRB.BINARY, name="x")

# Variables pour les regrets
r = m.addVars(n, vtype=GRB.CONTINUOUS, name="r")  # Regrets triés
b = m.addVars(n, n, vtype=GRB.CONTINUOUS, name="b")  # Variables d'ajustement des regrets

# Calcul des temps dans chaque scénario
times = [quicksum(scenarios[i][j] * x[j] for j in range(p)) for i in range(n)]

# Nouvelle fonction objectif : minimiser les regrets et favoriser la sélection de projets
m.setObjective(quicksum(w[k] * r[k] for k in range(n)), GRB.MINIMIZE)

# Contraintes de regret simplifiées
for k in range(n):
    for i in range(n):
        m.addConstr(r[k] >= times[i], f"regret_constr_{i}_{k}")

# Contrainte de budget
m.addConstr(quicksum(costs[j] * x[j] for j in range(p)) <= budget, "budget")

# Contrainte : au moins un projet doit être sélectionné
m.addConstr(quicksum(x[j] for j in range(p)) >= 1, "at_least_one_project")

# Résolution
m.optimize()

# Diagnostic : Temps calculés pour chaque scénario
print("\nDiagnostic : Temps calculés pour chaque scénario :")
for i, t in enumerate(times):
    print(f"Scénario {i + 1} : {t.getValue() if t.getValue() is not None else 'Non calculé'}")

# Diagnostic : Valeurs de regret après résolution
print("\nDiagnostic : Valeurs des regrets après résolution :")
for k in range(n):
    print(f"r[{k + 1}] = {r[k].x if r[k].x is not None else 'Non calculé'}")

# Résultats
if m.status == GRB.OPTIMAL:
    print("\nSolution optimale trouvée :")
    print("\nProjets sélectionnés :")
    for j in range(p):
        if x[j].x > 0.5:
            print(f"Projet {j + 1}")
    print("\nValeur optimale de la fonction objectif :", m.objVal)
else:
    print("\nAucune solution optimale trouvée.")
