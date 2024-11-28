from gurobipy import Model, GRB, quicksum

# Données générales pour les deux graphes
graphs = {
    "left": {  # Graphe de gauche
        "nodes": ["a", "b", "c", "d", "e", "f"],
        "arcs": {
            ("a", "b"): (4, 3), ("a", "c"): (5, 1), ("b", "c"): (2, 1),
            ("b", "d"): (1, 4), ("b", "e"): (2, 7), ("b", "f"): (7, 5),
            ("c", "d"): (5, 1), ("e", "f"): (5, 2), ("d", "f"): (3, 2)
        },
        "source": "a",
        "destination": "f"
    },
    "right": {  # Graphe de droite
        "nodes": ["a", "b", "c", "d", "e", "f", "g"],
        "arcs": {
            ("a", "b"): (5, 3), ("a", "c"): (10, 4), ("a", "d"): (2, 6),
            ("b", "d"): (1, 3), ("b", "e"): (4, 6), ("b", "c"): (4, 2),
            ("d", "c"): (1, 4), ("d", "f"): (3, 5), ("c", "e"): (3, 1),
            ("c", "f"): (1, 2), ("e", "g"): (1, 1), ("f", "g"): (1, 1)
        },
        "source": "a",
        "destination": "g"
    }
}

# Résolution pour chaque graphe et chaque scénario
for graph_name, graph_data in graphs.items():
    nodes = graph_data["nodes"]
    arcs = graph_data["arcs"]
    source = graph_data["source"]
    destination = graph_data["destination"]
    
    for k in [2, 4, 8, 16]:
        print(f"\nRésolution pour le graphe {graph_name} avec k={k}")
        
        # Modèle Gurobi
        m = Model(f"Robust_Path_{graph_name}_k{k}")
        
        # Variables de décision
        x = m.addVars(arcs.keys(), vtype=GRB.BINARY, name="x")
        v = m.addVars(2, vtype=GRB.CONTINUOUS, name="v")  # Temps pour chaque scénario
        
        # Fonction objectif : OWA avec w=(k, 1)
        m.setObjective(
            k * v[0] + 1 * v[1],  # Pondération pour OWA
            GRB.MINIMIZE
        )
        
        # Contraintes de conservation des flots
        for node in nodes:
            if node == source:
                m.addConstr(
                    quicksum(x[i, j] for (i, j) in arcs.keys() if i == node) -
                    quicksum(x[i, j] for (i, j) in arcs.keys() if j == node) == 1,
                    f"flow_source_{node}"
                )
            elif node == destination:
                m.addConstr(
                    quicksum(x[i, j] for (i, j) in arcs.keys() if i == node) -
                    quicksum(x[i, j] for (i, j) in arcs.keys() if j == node) == -1,
                    f"flow_dest_{node}"
                )
            else:
                m.addConstr(
                    quicksum(x[i, j] for (i, j) in arcs.keys() if i == node) -
                    quicksum(x[i, j] for (i, j) in arcs.keys() if j == node) == 0,
                    f"flow_node_{node}"
                )
        
        # Contraintes sur les temps pour chaque scénario
        for s in range(2):  # Deux scénarios
            m.addConstr(
                v[s] == quicksum(arcs[(i, j)][s] * x[i, j] for (i, j) in arcs.keys()),
                f"time_scenario_{s}"
            )
        
        # Résolution
        m.optimize()
        
        # Extraction du chemin optimal
        print(f"\nChemin optimal pour k={k} :")
        if m.status == GRB.OPTIMAL:
            for (i, j) in arcs.keys():
                if x[i, j].x > 0.5:
                    print(f"Arc ({i}, {j}) utilisé.")
            print(f"Valeur optimale : {m.objVal}")
        else:
            print("Aucune solution optimale trouvée.")
