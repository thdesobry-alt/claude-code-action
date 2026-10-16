# Cannelures Laminoir

Deux fichiers seulement :

| Fichier            | Rôle                                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| `index.html`       | L'application.                                                                                                  |
| `laminoir-db.json` | La base de données : cylindres, état et commentaires des cannelures, noms des options, tracés, commentaires HS. |

## Utilisation

1. Copier `index.html` et `laminoir-db.json` sur le poste (ou dans un dossier partagé du réseau).
2. Ouvrir `index.html` avec **Chrome** ou **Edge**.
3. Cliquer sur « Ouvrir un fichier JSON… » et choisir `laminoir-db.json`, puis autoriser la modification du fichier.

Chaque modification est écrite aussitôt dans le fichier JSON. Aux ouvertures suivantes,
le bouton « Reprendre « laminoir-db.json » » rouvre la même base en un clic.

## Plusieurs machines

- **Une base commune** : mettre `laminoir-db.json` dans un dossier partagé du réseau et
  l'ouvrir depuis chaque poste. L'application relit le fichier toutes les 4 secondes et
  n'écrit que l'élément modifié, pour ne pas écraser le travail des autres postes.
- **Une base par machine** : copier les deux fichiers sur chaque machine.

Onglet Cylindres : « Changer de base… », « Exporter JSON » (copie de sauvegarde) et
« Importer JSON » (remplace la base ouverte par le contenu d'un autre fichier).

Firefox et Safari ne permettent pas d'écrire dans un fichier : l'application y garde les
données dans le navigateur, et « Exporter JSON » / « Importer JSON » servent à les échanger.

## Cages affichées selon le diamètre laminé

| Ø laminé | Cages               |
| -------- | ------------------- |
| 16       | 1 à 16, sauf 7 et 8 |
| 18, 20   | 1 à 14              |
| 25       | 1 à 12              |
| 28       | 1 à 12, sauf 7 et 8 |
| 32       | 1 à 10              |
| 40       | 1 à 9, sauf 7       |

Les cages 1 à 6 ont toujours 1 frette et 1 cannelure, utilisée par défaut par les trois tracés.
Les cannelures sont numérotées en continu depuis le côté moteur.
