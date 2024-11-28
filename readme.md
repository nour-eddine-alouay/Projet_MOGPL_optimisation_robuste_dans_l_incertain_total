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
### **1.3. Dépendances Python**
Installez les bibliothèques nécessaires en exécutant la commande suivante :
   ```bash
   pip install matplotlib

## **2. Structure du projet**
L'organisation du projet est la suivante :
   ```bash
   ├── partie1/
   │   ├── partie1_1.py  # Code pour la question 1 de la partie 1
   │   ├── partie1_2.py  # Code pour la question 2 de la partie 1
   │   ├── partie1_3.py  # Code pour la question 3 de la partie 1
   │   ├── partie1_4.py  # Code pour la question 4 de la partie 1
   │
   ├── partie2/
   │   ├── partie2_1.py  # Code pour la question 1 de la partie 2
   │   ├── partie2_2.py  # Code pour la question 2 de la partie 2
   │   ├── partie2_3.py  # Code pour la question 3 de la partie 2
   │   ├── partie2_4.py  # Code pour la question 4 de la partie 2
   │
   ├── partie3/
   │   ├── partie3_1.py  # Code pour la question 1 de la partie 3
   │   ├── partie3_2.py  # Code pour la question 2 de la partie 3
   │   ├── partie3_3.py  # Code pour la question 3 de la partie 3
   │   ├── partie3_4.py  # Code pour la question 4 de la partie 3
   │
   ├── GR2_aloy_alyasfani.pdf  # Rapport détaillant le projet
   ├── README.md  # Fichier de documentation
   ```


## **3. Instructions d'exécution**
### **3.1. Exécution globale**
Pour exécuter toutes les parties du projet, suivez ces étapes :
1. Naviguez dans le dossier correspondant à la partie souhaitée :
   ```bash
   cd partieX
   ```

Remplacez X par le numéro de la partie (1, 2 ou 3).
2. Exécutez le fichier Python correspondant à la question :
   ```bash
   python partieX_Y.py
   ```

## **4. Résultats et analyse**

Les résultats des simulations incluent :

   Les solutions optimales pour chaque critère (maximin, minimax regret, maxOWA, minOWA).
   Les chemins robustes pour des graphes générés aléatoirement.
   L'évolution des temps de résolution pour différentes tailles de graphes.
Ces résultats sont :
   Affichés dans la console.
   Documentés dans le fichier GR2_aloy_alyasfani.pdf, qui contient des tableaux et des graphiques pour chaque question.
