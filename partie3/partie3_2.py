from gurobipy import Model, GRB, quicksum

# Graphe de gauche
nodes_left = ["a", "b", "c", "d", "e", "f"]
arcs_left = {
    ("a", "b"): (4, 3), ("a", "c"): (5, 1), ("b", "c"): (2, 1),
    ("b", "d"): (1, 4), ("b", "e"): (2, 7), ("b", "f"): (7, 5),
    ("c", "d"): (5, 1), ("e", "f"): (5, 2), ("d", "f"): (3, 2)
}
source = "a"
destination = "f"

# Résoudre pour chaque scénario
for scenario in [1, 2]:
    m = Model(f"Shortest_Path_Left_s{scenario}")
    
    # Variables de décision
    x = m.addVars(arcs_left.keys(), vtype=GRB.BINARY, name="x")
    
    # Fonction objectif : minimiser le temps total
    m.setObjective(
        quicksum(arcs_left[(i, j)][scenario - 1] * x[i, j] for (i, j) in arcs_left.keys()),
        GRB.MINIMIZE
    )
    
    # Contraintes de conservation des flots
    for node in nodes_left:
        if node == source:
            m.addConstr(
                quicksum(x[i, j] for (i, j) in arcs_left.keys() if i == node) -
                quicksum(x[i, j] for (i, j) in arcs_left.keys() if j == node) == 1,
                f"flow_source_{node}"
            )
        elif node == destination:
            m.addConstr(
                quicksum(x[i, j] for (i, j) in arcs_left.keys() if i == node) -
                quicksum(x[i, j] for (i, j) in arcs_left.keys() if j == node) == -1,
                f"flow_dest_{node}"
            )
        else:
            m.addConstr(
                quicksum(x[i, j] for (i, j) in arcs_left.keys() if i == node) -
                quicksum(x[i, j] for (i, j) in arcs_left.keys() if j == node) == 0,
                f"flow_node_{node}"
            )
    
    # Résolution
    m.optimize()
    
    # Extraction du chemin optimal
    print(f"\nChemin optimal pour le graphe de gauche dans le scénario s{scenario} :")
    if m.status == GRB.OPTIMAL:
        for (i, j) in arcs_left.keys():
            if x[i, j].x > 0.5:
                print(f"Arc ({i}, {j}) utilisé.")
        print(f"Temps total minimal : {m.objVal}")
    else:
        print("Aucune solution optimale trouvée.")

        
        
# Graphe de droite
nodes_right = ["a", "b", "c", "d", "e", "f", "g"]
arcs_right = {
    ("a", "b"): (5, 3), ("a", "c"): (10, 4), ("a", "d"): (2, 6),
    ("b", "d"): (1, 3), ("b", "e"): (4, 6), ("b", "c"): (4, 2),
    ("d", "c"): (1, 4), ("d", "f"): (3, 5), ("c", "e"): (3, 1),
    ("c", "f"): (1, 2), ("e", "g"): (1, 1), ("f", "g"): (1, 1)
}
destination_right = "g"

# Résoudre pour chaque scénario
for scenario in [1, 2]:
    m = Model(f"Shortest_Path_Right_s{scenario}")
    
    # Variables de décision
    x = m.addVars(arcs_right.keys(), vtype=GRB.BINARY, name="x")
    
    # Fonction objectif : minimiser le temps total
    m.setObjective(
        quicksum(arcs_right[(i, j)][scenario - 1] * x[i, j] for (i, j) in arcs_right.keys()),
        GRB.MINIMIZE
    )
    
    # Contraintes de conservation des flots
    for node in nodes_right:
        if node == source:
            m.addConstr(
                quicksum(x[i, j] for (i, j) in arcs_right.keys() if i == node) -
                quicksum(x[i, j] for (i, j) in arcs_right.keys() if j == node) == 1,
                f"flow_source_{node}"
            )
        elif node == destination_right:
            m.addConstr(
                quicksum(x[i, j] for (i, j) in arcs_right.keys() if i == node) -
                quicksum(x[i, j] for (i, j) in arcs_right.keys() if j == node) == -1,
                f"flow_dest_{node}"
            )
        else:
            m.addConstr(
                quicksum(x[i, j] for (i, j) in arcs_right.keys() if i == node) -
                quicksum(x[i, j] for (i, j) in arcs_right.keys() if j == node) == 0,
                f"flow_node_{node}"
            )
    
    # Résolution
    m.optimize()
    
    # Extraction du chemin optimal
    print(f"\nChemin optimal pour le graphe de droite dans le scénario s{scenario} :")
    if m.status == GRB.OPTIMAL:
        for (i, j) in arcs_right.keys():
            if x[i, j].x > 0.5:
                print(f"Arc ({i}, {j}) utilisé.")
        print(f"Temps total minimal : {m.objVal}")
    else:
        print("Aucune solution optimale trouvée.")
