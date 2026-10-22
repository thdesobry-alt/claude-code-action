# Arrêt technique hebdo — application de planification

Application web autonome (un fichier `index.html`, aucune installation), construite sur le
modèle de l'application « Arrêt technique ». Elle remplace le classeur
`Gantt SEMAINE xx ø..xlsx`. Les données sont stockées dans `data.json`.

## Principe

- Un **arrêt par semaine** (lundi 07h–18h et mardi par défaut, avec le diamètre laminé), choisi
  en haut de page (◀ Semaine 41 · ø25 ▶).
- Un **Gantt au quart d'heure**, comme la feuille Excel : une ligne par activité, groupée par
  section (zone), avec l'équipe, la fréquence, le pont, les agents et la signature.
- Une **gamme préventive** (activités récurrentes avec fréquence 7 jours, 14 jours, 1 mois…).
  Chaque semaine, « ＋ Semaine » propose les activités échues avec leur créneau, leurs agents,
  leurs modes opératoires et leurs check-lists, plus les activités non soldées de la semaine
  précédente.
- Une **bibliothèque de modes opératoires et de check-lists** à glisser sur les activités.

## Onglets

| Onglet                             | Contenu                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📅 Gantt                           | Un jour à la fois (Lundi / Mardi). Glisser une barre pour la déplacer, ses bords pour changer l'horaire, cliquer sur une ligne vide pour placer un créneau d'1 h (Maj + clic : créneau supplémentaire). Ligne « agents mobilisés » par quart d'heure, conflits d'agent ou de pont signalés en rouge. 🖨️ imprime le Gantt du jour au format de la feuille Excel (A3 paysage, colonne signature). |
| 📋 Activités                       | Compteurs (statuts, check-lists à compléter, points non conformes), avancement par équipe, liste filtrable. Statut modifiable dans la liste ; clic sur une pastille ☑ pour remplir la check-list. Impressions : dossiers d'intervention, analyses de risque, compte rendu.                                                                                                                     |
| 📚 Modes opératoires / check-lists | La bibliothèque : dépôt de fichiers, création et modification des check-lists, nombre d'activités qui utilisent chaque document.                                                                                                                                                                                                                                                                |
| 🔁 Gamme préventive                | Activités récurrentes : fréquence, jour et créneau habituels, agents, documents, dernière réalisation, état pour la semaine affichée (échue, en retard, à jour).                                                                                                                                                                                                                                |
| 🗺️ Schéma laminoir                 | Avancement de la semaine zone par zone ; un clic ouvre le Gantt filtré sur la zone.                                                                                                                                                                                                                                                                                                             |
| 👷 Charge et effectifs             | Agents présents de la semaine (nombre × heures), heures de maintenance par équipe et par jour, taux d'occupation (feuille « Total heures » de l'Excel). Occupation de chaque intervenant au quart d'heure, avec les doublons.                                                                                                                                                                   |
| 🗂️ Semaines                        | Historique des arrêts (activités, soldées, heures, occupation, check-lists), préparation, clôture, import Excel.                                                                                                                                                                                                                                                                                |
| ⚙️ Administration                  | Jours et horaires, pas du Gantt, diamètres, fréquences, consignes, zones et machines, équipes, ponts, personnel, éditeur JSON.                                                                                                                                                                                                                                                                  |

## Modes opératoires et check-lists

- **Ajouter** : glisser des fichiers dans l'onglet 📚 (ou dans le panneau « Bibliothèque » à droite
  des onglets Gantt, Activités et Gamme). PDF, Word, Excel, images → mode opératoire ;
  `.txt` / `.csv` → check-list (un point par ligne). On peut aussi créer une check-list à la main.
- **Format d'une check-list** : une ligne par point ; `# Titre` pour une section ;
  `Point | unité | valeur attendue` pour une mesure (ex. `Pression accumulateur | bar | 120`).
- **Rattacher** : glisser la carte de la bibliothèque sur une activité (Gantt, Activités ou Gamme),
  ou sur l'en-tête d'une zone pour toutes ses activités du jour. Un fichier déposé directement
  sur une activité rejoint la bibliothèque et l'activité. Sur téléphone (pas de glisser-déposer),
  utiliser « Choisir dans la bibliothèque » dans la fiche de l'activité.
- Un document rattaché à une activité qui vient de la gamme est aussi ajouté à la gamme : il
  revient les semaines suivantes.
- **Diamètres** : une check-list marquée pour certains diamètres (ex. « avant démarrage ø25 »)
  n'est jointe qu'aux semaines de ces diamètres. Dans la gamme, « Ø25 » dans la description est
  remplacé par le diamètre de la semaine.
- **Remplir** : OK / NOK / N/A, mesure et commentaire par point, « Rempli par ». Passer une
  activité à « Fait » avec une check-list incomplète demande confirmation. Les points NOK
  apparaissent dans le compte rendu.
- **Dossiers d'intervention** (onglet Activités, après avoir filtré, par exemple Mécanique +
  Lundi) : pour chaque activité, l'analyse de risque, les check-lists et les pages des modes
  opératoires PDF, à imprimer d'un coup.

## Importer le Gantt Excel

Onglet 🗂️ Semaines → **📥 Importer un Gantt Excel** (ou glisser le `.xlsx` sur la page). L'import :

- lit chaque feuille de jour (Lundi, Mardi…) : colonnes Section, Description, Equipe, Fréquences,
  Pont, Agents, puis une case par quart d'heure (15 = 1 agent, 30 = 2 agents ; la colonne
  12h–13h est la pause) ;
- prend la semaine dans le nom du fichier (« SEMAINE 41 ») et le diamètre en C1 (« ø25 ») ;
- range les sections dans les zones du schéma (DÉGROS → Dégrossisseur, TATEUR → Enfournement…)
  et crée les autres (Consignation, CM500, Check-list avant démarrage…) ;
- rapproche les agents du personnel par nom (« KHELOUFI / CASTERA ») ; les inconnus sont créés
  et classés dans l'équipe de la ligne (MSEM, ALPA, SIE → entreprises) ;
- crée l'arrêt de la semaine et alimente la gamme avec les lignes qui ont une fréquence.

L'import lit le classeur avec SheetJS (cdnjs) : il faut une connexion Internet.

## Reprendre l'arrêt technique

Administration → **👷 Reprendre l'arrêt technique (data.json)** : choisir le `data.json` de
l'application « Arrêt technique ». Le personnel (avec le N+1), les équipes, les zones et
machines, les ponts et le compte administrateur sont repris. Les agents créés par l'import Excel
sont alors fusionnés avec la bonne personne quand le nom correspond.

## Utilisation

1. Ouvrir `index.html` dans Chrome ou Edge.
2. Première fois : **✨ Créer une nouvelle base**, puis importer le Gantt Excel de la semaine et
   reprendre l'arrêt technique. Ensuite : **📂 Ouvrir** `data.json`.
3. Les modifications sont conservées dans le navigateur ; **💾 Enregistrer** (Ctrl+S) les écrit
   dans `data.json`.
4. Chaque semaine : **＋ Semaine** → cocher les activités proposées → ajuster le Gantt → imprimer
   le Gantt et les dossiers → saisir statuts, signatures et check-lists → **Clôturer** (onglet
   Semaines) : les activités non soldées passent en « Reportée » et seront proposées la semaine
   suivante.

Le compte administrateur, l'analyse de risque AQA.QSE.15, les photos avant/après et les
obligations pour les entreprises extérieures (n° de commande, plan de prévention) fonctionnent
comme dans l'arrêt technique. Les fichiers joints sont enregistrés dans `data.json` : le fichier
grossit avec eux.

## Structure de `data.json`

- `meta` : `titre`, `admin`, `jours[]` (`dow` 0 = dimanche, `nom`, `debut`, `fin`, `pauses[]`),
  `pas` (minutes), `diametres[]`, `frequences[]`, `consignes[]`, `effectifs[]` par défaut
  (`lib`, `service`, `nb`, `h`).
- `arrets[]` : `id`, `lundi`, `diametre`, `statut` (`prepa`, `encours`, `cloture`),
  `effectifs[]`, `consignes[]`, `notes`.
- `activites[]` : `arret`, `gamme`, `zone`, `machine`, `service` (équipe du Gantt), `designation`,
  `frequence`, `jour` (indice dans `meta.jours`), `creneaux[]` (`debut`, `fin` en `HH:MM`), `nb`
  (agents mobilisés), `intervenants[]`, `pont`, `statut`, `signePar`, `signeLe`, `modes[]`
  (`doc`, `rep` = réponses par point `{v: ok|nok|na, m, c}`, `par`, `date`), `ar`, `docs`,
  `photos`, `commande`, `pdpRef`, `origine` / `reprise` (report d'une semaine à l'autre), `ordre`.
- `gamme[]` : mêmes champs de planification, plus `modes[]` (ids de documents), `actif`,
  `derniere` (dernière réalisation saisie à la main).
- `bibliotheque[]` : `type` (`mop` ou `checklist`), `titre`, `ref`, `version`, `service`, `zone`,
  `diametres[]`, `fichier` (`nom`, `type`, `data`), `points[]` (`t`, `unite`, `attendu`,
  `section`), `consigne`.
- `zones[]`, `flux[]`, `personnel[]`, `equipes[]`, `services[]`, `ponts[]` : comme l'arrêt
  technique.
