import random
import time
from gurobipy import Model, GRB, quicksum

# Paramètres des instances
n_values = [5, 10, 15]  # Nombre d'objets/projets
p_values = [10, 15, 20]  # Nombre de scénarios
num_instances = 10  # Nombre d'instances pour chaque couple (n, p)
results = []

# Fonction pour générer une instance et résoudre avec maxOWA ou minOWA
def solve_instance(n, p, mode="maxOWA"):
    # Génération aléatoire des coûts, utilités, et scénarios
    costs = [random.randint(1, 100) for _ in range(n)]
    scenarios = [[random.randint(1, 100) for _ in range(n)] for _ in range(p)]
    budget = int(0.5 * sum(costs))  # Budget fixé à 50% du coût total

    # Modèle Gurobi
    m = Model(f"{mode}_robust_knapsack")

    # Variables de décision pour les projets sélectionnés
    x = m.addVars(n, vtype=GRB.BINARY, name="x")

    # Variables pour les regrets
    r = m.addVars(p, vtype=GRB.CONTINUOUS, name="r")  # Regrets triés
    b = m.addVars(p, p, vtype=GRB.CONTINUOUS, name="b")  # Variables d'ajustement des regrets

    # Calcul des temps dans chaque scénario
    times = [quicksum(scenarios[i][j] * x[j] for j in range(n)) for i in range(p)]

    # Fonction objectif
    if mode == "maxOWA":
        weights = [1 - i / p for i in range(p)]  # Poids décroissants pour maxOWA
        m.setObjective(quicksum(weights[k] * r[k] for k in range(p)), GRB.MAXIMIZE)
    elif mode == "minOWA":
        weights = [1 / (k + 1) for k in range(p)]  # Poids croissants pour minOWA
        m.setObjective(quicksum(weights[k] * r[k] for k in range(p)), GRB.MINIMIZE)

    # Contraintes de regret
    for k in range(p):
        for i in range(p):
            m.addConstr(r[k] >= times[i] - b[i, k], f"regret_constr_{i}_{k}")

    # Contrainte de budget
    m.addConstr(quicksum(costs[j] * x[j] for j in range(n)) <= budget, "budget")

    # Résolution
    start_time = time.time()
    m.optimize()
    end_time = time.time()

    # Retourner le temps de résolution
    return end_time - start_time

# Boucle pour générer et résoudre les instances
for n in n_values:
    for p in p_values:
        maxOWA_times = []
        minOWA_times = []
        for _ in range(num_instances):
            # Résoudre avec maxOWA
            maxOWA_time = solve_instance(n, p, mode="maxOWA")
            maxOWA_times.append(maxOWA_time)

            # Résoudre avec minOWA
            minOWA_time = solve_instance(n, p, mode="minOWA")
            minOWA_times.append(minOWA_time)

        # Calculer les temps moyens
        avg_maxOWA_time = sum(maxOWA_times) / num_instances
        avg_minOWA_time = sum(minOWA_times) / num_instances

        # Stocker les résultats
        results.append((n, p, avg_maxOWA_time, avg_minOWA_time))

# Afficher les résultats
print("Résultats :")
for n, p, avg_max, avg_min in results:
    print(f"(n={n}, p={p}) -> maxOWA: {avg_max:.4f}s, minOWA: {avg_min:.4f}s")

# Visualisation des résultats
import matplotlib.pyplot as plt

# Extraire les données pour le graphique
n_values, p_values, avg_max_times, avg_min_times = zip(*[
    (n, p, avg_max, avg_min) for n, p, avg_max, avg_min in results
])

# Graphique
plt.figure(figsize=(10, 6))
plt.plot(range(len(avg_max_times)), avg_max_times, label="maxOWA", marker='o')
plt.plot(range(len(avg_min_times)), avg_min_times, label="minOWA", marker='s')
plt.xticks(range(len(avg_max_times)), [f"n={n}, p={p}" for n, p in zip(n_values, p_values)], rotation=45)
plt.ylabel("Temps moyen de résolution (s)")
plt.xlabel("(n, p)")
plt.title("Évolution du temps de résolution pour maxOWA et minOWA")
plt.legend()
plt.tight_layout()
plt.show()
