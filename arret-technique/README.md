# Arrêt technique — application de planification

Application web autonome (un fichier `index.html`, aucune installation) qui remplace le
classeur `Planning arrêt Été 2026.xlsm`. Les données sont stockées dans `data.json`.

## Onglets

| Onglet               | Contenu                                                                                                                                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📋 Activités         | Compteurs par statut (cliquables), avancement par service, liste des opérations groupée par zone avec filtres (zone, service, statut, intervenant, planifiée ou non, recherche). Statut modifiable directement dans la liste ; clic = fiche. |
| 🏗️ Ponts roulants    | Calendrier des ponts (DEMAG, ANSELMI, ajout possible) par demi-journée. Réservation d'utilisation ou indisponibilité (maintenance du pont), détection des conflits, liste des activités qui demandent un pont et pas encore réservées.       |
| 🗺️ Schéma laminoir   | Schéma de la ligne dans le sens du produit + zones générales et utilités. Chaque zone affiche son avancement et le nombre d'opérations restantes. Un clic ouvre le **Gantt de la zone**.                                                     |
| 👷 Charge de travail | Bilan heures disponibles / heures planifiées par équipe (avec % de temps perdu), puis calendrier opérateur × jour coloré selon la charge. Clic sur une case : détail des activités du jour et saisie des absences (CP…).                     |

Dans le Gantt : glisser une barre pour la déplacer, tirer son bord droit pour changer la durée,
cliquer sur un jour vide d'une ligne non planifiée pour la planifier (la date de fin est
calculée à partir de la durée en heures et de la capacité journalière).

Les dates de l'arrêt, les jalons, les consignes, la capacité par jour (Lun 10 h, Mar–Jeu 7 h,
Ven 6,5 h) et le temps perdu se modifient en cliquant sur la ligne de dates sous le titre.

## Utilisation

1. Ouvrir `index.html` dans Chrome ou Edge.
2. Au premier lancement, cliquer sur **📂 Ouvrir** et choisir `data.json`
   (si l'application est servie par un serveur web, `data.json` est chargé automatiquement).
3. Les modifications sont conservées dans le navigateur au fil de l'eau ;
   **💾 Enregistrer** (ou Ctrl+S) les écrit dans `data.json`. Chrome/Edge réécrivent directement
   le fichier choisi ; les autres navigateurs téléchargent un nouveau `data.json`.

Pour partager le planning, déposer `index.html` et `data.json` dans un dossier commun :
chacun ouvre le même fichier. Attention, deux personnes qui enregistrent en même temps
écrasent mutuellement leurs modifications.

## Réimporter depuis Excel

```bash
pip install openpyxl
python3 outils/import_excel.py "Planning arrêt Été 2026 v0.xlsm" data.json
```

Le script reprend les opérations (onglet _Planning_), le personnel (_bdd personnel_), les
services (_Liste_) et les dates de l'arrêt. Les intervenants sont rapprochés du personnel par
nom ou prénom (« JEROME/OUSMAN » → BOUTIN Jérome, MARNA Ousmane) ; les noms inconnus
(entreprises extérieures : MSEM, ALPA, SIE…) sont créés dans l'équipe « Entreprises / non
référencés ».

## Structure de `data.json`

- `meta` : titre, `debut`, `fin`, `finAffichage`, `jalons[]`, `consignes[]`, `capacite`
  (heures par jour de semaine, 0 = dimanche), `tempsPerdu`, `modeCharge`.
- `zones[]` : `id`, `nom`, `type` (`process`, `general`, `utilite`) et position sur le schéma
  (`x`, `y`, `w`, `h`) ; `flux[]` : ordre des zones dans le sens du produit (flèches).
- `activites[]` : `zone`, `service`, `designation`, `statut` (`afaire`, `encours`, `fait`,
  `nonnecessaire`, `reportee`), `intervenants[]` (ids du personnel), `gmao`, `moi`, `dureeH`,
  `debut`, `fin`, `debutReel`, `pont`, `commentaire`.
- `personnel[]` : `nom`, `prenom`, `matricule`, `poste`, `equipe`, `absences[]` (dates).
- `equipes[]`, `services[]`, `ponts[]`, `reservations[]` (`pont`, `date`, `creneau` M/A/J,
  `type` utilisation/indispo, `activite`, `libelle`, `demandeur`).

Toutes les dates sont au format `AAAA-MM-JJ`.
