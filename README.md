# Travaux dirigés n°2 — Optimisation
## Exercice 2 — Problème de transport

### Données

- Stocks : D1 = 8 containers et D2 = 9 containers.
- Demandes : M1 = 4, M2 = 5 et M3 = 8 containers.
- Coûts unitaires :

| Dépôt | M1 | M2 | M3 |
|---|---:|---:|---:|
| D1 | 5 | 3 | 4 |
| D2 | 6 | 7 | 2 |

### Méthode

Une solution représente les quantités envoyées par D1 aux trois magasins. D2 fournit les quantités restantes.

Un voisin est créé en déplaçant un container de D1 d'un magasin vers un autre. La recherche taboue choisit le voisin autorisé de coût minimal et garde en mémoire les dernières solutions visitées. Le critère d'aspiration permet d'accepter une solution taboue si elle améliore la meilleure solution connue.

### Résultat obtenu

| Dépôt | M1 | M2 | M3 | Total |
|---|---:|---:|---:|---:|
| D1 | 3 | 5 | 0 | 8 |
| D2 | 1 | 0 | 8 | 9 |

Coût total : `3 × 5 + 5 × 3 + 1 × 6 + 8 × 2 = 52`.

## Exercice 3 — Voyageur de commerce

Le circuit initial demandé est `1-2-3-4-5-6-7-8-1`. Les distances sont interprétées comme symétriques. Les trajets absents du tableau sont considérés comme indisponibles, donc les circuits qui les utilisent sont rejetés.

Un voisin est obtenu en échangeant deux villes, tout en gardant la ville 1 au début du circuit.

### Recuit simulé

Le programme effectue les cinq itérations demandées. Les paramètres choisis sont :

- température initiale : `T0 = 10` ;
- refroidissement : `T suivante = 0,8 × T` ;
- graine aléatoire : `73`, pour rendre l'exécution reproductible.

Une amélioration est acceptée. Une dégradation de coût `Δ` est acceptée avec la probabilité `exp(-Δ/T)`.

### Recherche taboue

La recherche part du circuit initial, examine les voisins réalisables et choisit le meilleur voisin non tabou. La mémoire conserve les sept dernières solutions. Le critère d'aspiration autorise un voisin tabou s'il améliore le meilleur circuit déjà trouvé.

### Résultat obtenu

Les deux méthodes trouvent le circuit :

`1-2-4-5-6-7-3-8-1`

Son coût est `98`.
