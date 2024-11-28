# Projet MOGPL : Optimisation Robuste dans l'Incertain Total

Ce projet implémente différentes approches d'optimisation robuste, réparties en trois parties principales :
1. **Linéarisation des critères maximin et minmax regret**.
2. **Linéarisation du critère maxOWA et minOWA des regrets**.
3. **Application à la recherche d’un chemin robuste dans un graphe**.

Chaque partie est subdivisée en plusieurs sous-questions, avec un fichier Python pour chaque réponse.

## **1. Prérequis**

### **1.1. Python**
- Installez la dernière version de Python (>= 3.8).
- Téléchargez Python depuis [python.org](https://www.python.org/downloads/).

### **1.2. Gurobi**
1. Téléchargez Gurobi depuis [gurobi.com](https://www.gurobi.com/).
2. Suivez les étapes pour activer une licence académique gratuite.
3. Installez la bibliothèque Python pour Gurobi :
   ```bash
   pip install gurobipy
