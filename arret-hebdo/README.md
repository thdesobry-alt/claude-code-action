# Arrêt technique hebdo — application de planification

Application web autonome (un fichier `index.html`, aucune installation), construite sur le
modèle de l'application « Arrêt technique ». Elle remplace le classeur
`Gantt SEMAINE xx ø..xlsx`. Les données sont stockées dans `data.json`.

## Principe

- Un **arrêt par semaine** (lundi 07h–18h et mardi par défaut, avec le diamètre laminé), choisi
  en haut de page (◀ Semaine 41 · ø25 ▶).
- Un **Gantt au quart d'heure**, comme la feuille Excel : une ligne par activité, groupée par
  section (zone), avec l'équipe, la fréquence, le pont, les agents et la signature.
- Trois statuts : **Planifié**, **Fait**, **Reporté**.
- **＋ Semaine** prépare la semaine suivante à partir d'un **programme type** (ou de la semaine
  précédente) ; les activités non faites de la semaine précédente y sont reportées. On complète
  ensuite avec les **tâches à planifier** de la réserve.

## Onglets

| Onglet                  | Contenu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 📅 Gantt                | Un jour à la fois (Lundi / Mardi). Glisser une barre pour la déplacer, ses bords pour changer l'horaire, cliquer sur une ligne vide pour placer un créneau d'1 h (Maj + clic : créneau supplémentaire). Ligne « agents mobilisés » par quart d'heure, conflits d'agent ou de pont signalés en rouge. 🖨️ imprime le Gantt du jour au format de la feuille Excel (A3 paysage, colonne signature).                                                                                            |
| 📋 Activités            | Compteurs Planifié / Fait / Reporté, avancement par équipe, liste filtrable avec statut modifiable. Impressions : analyses de risque, compte rendu de l'arrêt.                                                                                                                                                                                                                                                                                                                             |
| 🗺️ Schéma laminoir      | Avancement de la semaine zone par zone ; un clic ouvre le Gantt filtré sur la zone.                                                                                                                                                                                                                                                                                                                                                                                                        |
| 👷 Charge et effectifs  | Agents présents de la semaine (nombre × heures), heures de maintenance par équipe et par jour, taux d'occupation (feuille « Total heures » de l'Excel). Occupation de chaque intervenant au quart d'heure, avec les doublons.                                                                                                                                                                                                                                                              |
| 🧰 Programmes et tâches | **Programmes types** : enregistrer la semaine affichée comme modèle, l'appliquer à une semaine (sans doublons), le revoir (retirer des activités) ou le remplacer par la semaine affichée. **Tâches à planifier** : réserve sans limite de tâches (création, ou « Copier dans les tâches » depuis la fiche d'une activité), recherche par texte, zone, équipe, « jamais planifiées » ; cocher puis « Planifier la sélection » sur la semaine affichée, le jour habituel ou un jour choisi. |
| 🗂️ Semaines             | Historique des arrêts (activités, faites, heures, occupation), préparation, clôture, import Excel.                                                                                                                                                                                                                                                                                                                                                                                         |
| ⚙️ Administration       | Jours et horaires, pas du Gantt, diamètres, fréquences, consignes, zones et machines, équipes, ponts, personnel, éditeur JSON.                                                                                                                                                                                                                                                                                                                                                             |

## Programmes types par diamètre

- Diamètres : ø16, ø18, ø20, ø25, ø28, ø32, ø40 (modifiables dans Administration).
- Un programme type peut être **associé à un diamètre** : il ne contient alors que les tâches
  spécifiques à ce diamètre (check-lists avant démarrage, contrôles des guides…). En choisissant
  le diamètre à l'enregistrement, les activités qui citent ce diamètre (« Ø25 ») sont
  pré-cochées. « Voir / modifier » permet de changer le diamètre, de retirer des activités et
  d'ajouter des tâches de la réserve.
- Les programmes sans diamètre sont les **programmes de base**, proposés dans « Partir de ».
- Dans **＋ Semaine**, on choisit 1 ou 2 diamètres : les tâches des programmes associés à ces
  diamètres sont ajoutées automatiquement (décochables). Changer ou ajouter un diamètre dans les
  paramètres de la semaine propose aussi d'ajouter les tâches du nouveau diamètre.

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
- crée l'arrêt de la semaine avec ses activités (créneaux, agents, fréquences).

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
4. Chaque semaine : **＋ Semaine** → cocher les activités à reprendre → ajuster le Gantt → imprimer
   le Gantt → saisir statuts et signatures → **Clôturer** (onglet Semaines) : les activités encore
   planifiées passent en « Reporté » et seront proposées la semaine suivante.

Le compte administrateur, l'analyse de risque AQA.QSE.15, les photos avant/après et les
obligations pour les entreprises extérieures (n° de commande, plan de prévention) fonctionnent
comme dans l'arrêt technique. Les fichiers joints sont enregistrés dans `data.json` : le fichier
grossit avec eux.

## Structure de `data.json`

- `meta` : `titre`, `admin`, `jours[]` (`dow` 0 = dimanche, `nom`, `debut`, `fin`, `pauses[]`),
  `pas` (minutes), `diametres[]`, `frequences[]`, `consignes[]`, `effectifs[]` par défaut
  (`lib`, `service`, `nb`, `h`).
- `arrets[]` : `id`, `lundi`, `diametre`, `diametre2` (2ᵉ diamètre facultatif), `statut` (`prepa`, `encours`, `cloture`),
  `effectifs[]`, `consignes[]`, `notes`.
- `activites[]` : `arret`, `zone`, `machine`, `service` (équipe du Gantt), `designation`,
  `frequence`, `jour` (indice dans `meta.jours`), `creneaux[]` (`debut`, `fin` en `HH:MM`), `nb`
  (agents mobilisés), `intervenants[]`, `pont`, `statut` (`planifie`, `fait`, `reportee`),
  `signePar`, `signeLe`, `ar`, `docs`, `photos`, `commande`, `pdpRef`, `origine` / `reprise`
  (report d'une semaine à l'autre), `ordre`.
- `programmes[]` : `id`, `nom`, `diametre` (vide = programme de base), `note`, `maj`, `activites[]` (modèles : zone, machine, équipe,
  description, fréquence, jour, créneaux, agents, pont, GMAO).
- `taches[]` : mêmes champs que les modèles, plus `note` et `cree` ; les activités planifiées
  depuis une tâche portent son identifiant dans `tache`.
- `zones[]`, `flux[]`, `personnel[]`, `equipes[]`, `services[]`, `ponts[]` : comme l'arrêt
  technique.
