# Cannelures Laminoir

Gestion des cylindres des cages de laminage 1 à 16 : état des cannelures, commentaires,
tracés des options et base des cylindres.

## Fichiers

| Fichier                        | Rôle                                                                                                            |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `index.html`                   | L'application.                                                                                                  |
| `laminoir-db.json`             | La base de données : cylindres, état et commentaires des cannelures, noms des options, tracés, commentaires HS. |
| `serveur.py`                   | Petit serveur (Python, sans dépendance) qui fait travailler l'application sur `laminoir-db.json`.               |
| `demarrer.bat` / `demarrer.sh` | Lancent le serveur (Windows / Linux).                                                                           |
| `app.html`                     | Même application, version publiée sur claude.ai.                                                                |

## Installer sur un poste

1. Installer Python 3 (https://www.python.org ; sous Windows, cocher « Add python to PATH »).
2. Copier le dossier (`index.html`, `serveur.py`, `laminoir-db.json`, `demarrer.bat`) sur le poste.
3. Double-cliquer sur `demarrer.bat`. Le navigateur s'ouvre sur http://localhost:8080.

Chaque modification est écrite tout de suite dans `laminoir-db.json`. La version précédente
est gardée dans `laminoir-db.sauvegarde.json`.

## Plusieurs machines

- **Une base commune** : lancer le serveur sur un seul poste. Les autres postes ouvrent
  `http://<nom-ou-IP-du-poste>:8080`. Tous travaillent sur le même `laminoir-db.json` et
  voient les modifications des autres en moins de 5 secondes. Le port 8080 doit être
  autorisé dans le pare-feu de ce poste.
- **Une base par machine** : copier le dossier sur chaque machine et lancer `demarrer.bat`
  sur chacune. Pour reprendre les données d'une autre machine, copier son `laminoir-db.json`
  (serveur arrêté) ou utiliser « Importer JSON » dans l'onglet Cylindres.

Sans serveur (`index.html` ouvert directement), les données restent dans le navigateur ;
les boutons « Exporter JSON » et « Importer JSON » de l'onglet Cylindres permettent de les
sortir ou de les charger.

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
