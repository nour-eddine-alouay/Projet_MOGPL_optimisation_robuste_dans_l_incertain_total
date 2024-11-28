from gurobipy import Model, GRB, quicksum

# Données du graphe
nodes = [1, 2, 3, 4, 5]  # Sommets
arcs = [
    (1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (4, 5)
]  # Arcs
scenario_times = {  # Temps associés aux arcs pour un scénario donné
    (1, 2): 4, (1, 3): 1, (2, 4): 2, (2, 5): 7, (3, 4): 5, (4, 5): 3
}
source = 1  # Sommet initial
destination = 5  # Sommet destination

# Modèle Gurobi
m = Model("Shortest_Path")

# Variables de décision
x = m.addVars(arcs, vtype=GRB.BINARY, name="x")

# Fonction objectif : minimiser le temps total
m.setObjective(
    quicksum(scenario_times[(i, j)] * x[i, j] for (i, j) in arcs),
    GRB.MINIMIZE
)

# Contraintes de conservation des flots
for node in nodes:
    if node == source:
        m.addConstr(
            quicksum(x[i, j] for (i, j) in arcs if i == node) -
            quicksum(x[i, j] for (i, j) in arcs if j == node) == 1,
            f"flow_source_{node}"
        )
    elif node == destination:
        m.addConstr(
            quicksum(x[i, j] for (i, j) in arcs if i == node) -
            quicksum(x[i, j] for (i, j) in arcs if j == node) == -1,
            f"flow_dest_{node}"
        )
    else:
        m.addConstr(
            quicksum(x[i, j] for (i, j) in arcs if i == node) -
            quicksum(x[i, j] for (i, j) in arcs if j == node) == 0,
            f"flow_node_{node}"
        )

# Résolution
m.optimize()

# Extraction du chemin optimal
if m.status == GRB.OPTIMAL:
    print("\nChemin optimal :")
    for (i, j) in arcs:
        if x[i, j].x > 0.5:
            print(f"Arc ({i}, {j}) utilisé.")
    print(f"Temps total minimal : {m.objVal}")
else:
    print("Aucune solution optimale trouvée.")
