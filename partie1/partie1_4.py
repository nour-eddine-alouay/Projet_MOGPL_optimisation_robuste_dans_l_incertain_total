import time
import random
from gurobipy import Model, GRB, quicksum

# Paramètres
n_values = [5, 10, 15]  # Nombre de scénarios
p_values = [10, 15, 20]  # Nombre de projets
num_instances = 10  # Nombre d'instances par (n, p)

results = []

for n in n_values:
    for p in p_values:
        instance_times = []
        
        for _ in range(num_instances):
            # Générer les coûts et utilités aléatoires
            costs = [random.randint(1, 100) for _ in range(p)]
            utilities = [[random.randint(1, 100) for _ in range(p)] for _ in range(n)]
            budget = 0.5 * sum(costs)
            
            # Résoudre le problème
            start_time = time.time()
            
            try:
                # Modèle Gurobi
                m = Model("robust_knapsack")
                
                # Variables de décision
                x = m.addVars(p, vtype=GRB.BINARY, name="x")
                t = m.addVar(vtype=GRB.CONTINUOUS, name="t")
                
                # Fonction objectif : minimiser le regret maximal
                m.setObjective(t, GRB.MINIMIZE)
                
                # Contraintes de regrets
                for i in range(n):
                    m.addConstr(t >= quicksum(utilities[i][j] * x[j] for j in range(p)) - max(utilities[i]), f"regret_{i}")
                
                # Contrainte de budget
                m.addConstr(quicksum(costs[j] * x[j] for j in range(p)) <= budget, "budget")
                
                # Résolution
                m.optimize()
                
            except Exception as e:
                print(f"Erreur lors de la résolution : {e}")
            
            # Temps de résolution
            end_time = time.time()
            instance_times.append(end_time - start_time)
        
        # Temps moyen pour cette combinaison (n, p)
        avg_time = sum(instance_times) / len(instance_times)
        results.append((n, p, avg_time))

# Afficher les résultats
print("Résultats :")
for n, p, avg_time in results:
    print(f"(n={n}, p={p}) : Temps moyen = {avg_time:.2f} secondes")
