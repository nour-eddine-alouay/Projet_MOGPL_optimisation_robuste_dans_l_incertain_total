import random
import time
from gurobipy import Model, GRB, quicksum

# Fonction pour générer un graphe aléatoire
def generate_random_graph(n_scenarios, n_nodes, density=0.4):
    arcs = {}
    for i in range(n_nodes):
        for j in range(n_nodes):
            if i != j and random.random() < density:
                arcs[(i, j)] = [random.randint(1, 100) for _ in range(n_scenarios)]
    return arcs

# Fonction pour résoudre le problème avec un critère donné
def solve_criteria(graph, source, destination, n_scenarios, criterion, weights=None):
    model = Model(f"Path_{criterion}")
    arcs = list(graph.keys())

    # Variables de décision
    x = model.addVars(arcs, vtype=GRB.BINARY, name="x")
    v = model.addVars(n_scenarios, vtype=GRB.CONTINUOUS, name="v")  # Temps pour chaque scénario

    # Contraintes de conservation des flots
    for node in range(len(graph)):
        if node == source:
            model.addConstr(
                quicksum(x[i, j] for (i, j) in arcs if i == node) -
                quicksum(x[i, j] for (i, j) in arcs if j == node) == 1,
                f"flow_source_{node}"
            )
        elif node == destination:
            model.addConstr(
                quicksum(x[i, j] for (i, j) in arcs if i == node) -
                quicksum(x[i, j] for (i, j) in arcs if j == node) == -1,
                f"flow_dest_{node}"
            )
        else:
            model.addConstr(
                quicksum(x[i, j] for (i, j) in arcs if i == node) -
                quicksum(x[i, j] for (i, j) in arcs if j == node) == 0,
                f"flow_node_{node}"
            )
    
    # Contraintes sur les temps pour chaque scénario
    for s in range(n_scenarios):
        model.addConstr(
            v[s] == quicksum(graph[(i, j)][s] * x[i, j] for (i, j) in arcs),
            f"time_scenario_{s}"
        )

    # Définir la fonction objectif selon le critère
    if criterion == "maximin":
        model.setObjective(quicksum(v[s] for s in range(n_scenarios)), GRB.MAXIMIZE)
    elif criterion == "minimax_regret":
        r = model.addVar(vtype=GRB.CONTINUOUS, name="r")
        for s in range(n_scenarios):
            model.addConstr(r >= v[s], f"regret_{s}")
        model.setObjective(r, GRB.MINIMIZE)
    elif criterion == "maxOWA":
        model.setObjective(
            quicksum(weights[s] * v[s] for s in range(n_scenarios)), GRB.MAXIMIZE
        )
    elif criterion == "minOWA":
        model.setObjective(
            quicksum(weights[s] * v[s] for s in range(n_scenarios)), GRB.MINIMIZE
        )
    
    # Résolution
    start_time = time.time()
    model.optimize()
    elapsed_time = time.time() - start_time

    return elapsed_time

# Étude des temps de résolution
n_values = [2, 5, 10]  # Nombre de scénarios
p_values = [10, 15, 20]  # Nombre de nœuds
num_instances = 10  # Nombre d'instances par couple (n, p)
results = []

for n in n_values:
    for p in p_values:
        for criterion in ["maximin", "minimax_regret", "maxOWA", "minOWA"]:
            times = []
            for _ in range(num_instances):
                # Générer un graphe aléatoire
                graph = generate_random_graph(n, p)
                source = 0
                destination = p - 1
                weights = [1 / (s + 1) for s in range(n)]  # Pondérations pour OWA

                # Résoudre le problème
                elapsed_time = solve_criteria(graph, source, destination, n, criterion, weights)
                times.append(elapsed_time)

            # Calculer le temps moyen
            avg_time = sum(times) / len(times)
            results.append((n, p, criterion, avg_time))

# Affichage des résultats
print("Résultats :")
for n, p, criterion, avg_time in results:
    print(f"(n={n}, p={p}, critère={criterion}) -> Temps moyen : {avg_time:.4f}s")
