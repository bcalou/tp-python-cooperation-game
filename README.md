# Le jeu de la coopération

Chaque joueur a le droit de modifier le fichier qui lui est attribué dans le dossier `cooperation/players`.

## Méthode `play()`

La première chose à faire est de surcharger la méthode `play`, définie par la classe parente `Player`. Par défaut, la méthode résulte en une coopération systématique.


```py
def play(self, opponent: 'Player') -> Action:
    return Action.COOPERATE
```

Mais vous pouvez décider de tricher :

```py
def play(self, opponent: 'Player') -> Action:
    return Action.CHEAT
```

**Seule cette fonction peut-être étendue**. Vous avez le droit de créer de nouvelles fonctions pour les appeler à partir de la fonction `play`.

**Si votre méthode génère une erreur, la coopération est le résultat par défaut**.

## But du jeu

Amasser le plus de gain en choisissant les actions les plus judicieuses.

À chaque manche, chaque joueur rencontre tous les autres. Une rencontre est constituée d'une série de 10 duels.

Autrement dit, la méthode play de chaque joueur sera appelée 10 fois avec chaque adversaire.

À chaque tour :
- Si les deux joueurs coopèrent, ils gagnent **2 pièces** chacun
- Si les deux joueurs trichent, ils ne gagnent rien
- Si un joueur triche tandis que l'autre coopère, le tricheur gagne **3 pièces** et l'autre joueur perd **une pièce**

## À votre disposition

### `opponent`

La méthode `play()` est appelée avec le paramètre `opponent`. Cette variable contient le nom de votre adversaire (ou allié !).

### `self._fight_history`

Cette variable est un tableau contenant l'historique de votre rencontre avec l'adversaire actuel.

Au moment du premier appel à `play` face à un adversaire donné, ce tableau est vide.

La fois suivante, il contient les décisions prises par vous et votre adversaire au premier tour, par exemple :

```py
[
    {
        'self_action': <Action.COOPERATE: 1>,
        'opponent_action': <Action.COOPERATE: 1>
    }
]
```

### `self._say()`

Si vous voulez laisser une trace dans les journaux textuels de la prochaine manche, vous pouvez vous exprimer en appelant cette méthode. Mais restez poli, tout de même.

### `main.py`

Vous pouvez lancer le fichier `main.py` de votre côté pour effectuer une simulation de la prochaine manche.

### Journaux

Les enregistrement textuels et visuels des manches jouées se trouvent dans le dossier `logs`.
