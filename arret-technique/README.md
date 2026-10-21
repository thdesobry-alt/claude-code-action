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

## Compte administrateur

Le bouton **🔒 Administrateur** (en haut à droite) ouvre la connexion. Au premier clic, si
`data.json` ne contient pas encore de compte, il propose de le créer (identifiant + mot de
passe d'au moins 6 caractères). Le compte est stocké dans `data.json` (`meta.admin`, mot de
passe haché et salé) : pensez à **💾 Enregistrer** après l'avoir créé.

Connecté, l'administrateur dispose de l'onglet **⚙️ Administration** :

- **Arrêt technique** : titre, dates de début et de fin, fin d'affichage, jalons, consignes,
  heures par jour et temps perdu.
- **Zones et machines** : ajout, renommage, type (ligne, zone générale, utilité), ordre dans le
  sens du produit, taille et position, liste des machines/équipements de la zone ; suppression
  avec réaffectation des activités. Sur le schéma, **✏️ Modifier le schéma** permet de
  déplacer les zones à la souris.
- **Services**, **équipes**, **ponts roulants**, **personnel** : ajout, modification,
  suppression (avec réaffectation des éléments liés).
- **Données** : éditeur JSON de toute la base, export d'une copie datée, purge de la copie
  gardée dans le navigateur. Identifiant et mot de passe se changent depuis le même onglet.

Sans connexion, on peut toujours créer et modifier des activités (statut, planning, intervenants,
machine), réserver les ponts et saisir les absences. Sont réservés à l'administrateur : les
paramètres de l'arrêt, les zones, machines, services, équipes, ponts et personnel, la suppression
d'activités et l'éditeur JSON.

> Ce mot de passe protège contre les fausses manipulations, pas contre une personne
> malveillante : l'application tourne entièrement dans le navigateur, et quiconque peut
> modifier `data.json` peut retirer le compte. Pour une vraie protection, limitez les droits
> d'écriture sur le dossier partagé.

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

## Zones du Pareto laminoir

Les zones et les machines viennent de l'application « Arrêts de production » (onglet Schéma
laminoir) : Enfournement / Défournement, Soudeuse, Train, Ligne petit diamètre, Ligne gros
diamètre, Refroidissoir jusque VR9, KNCA, Évacuation TR12 12bis, Station eau, plus une zone
« Général / hors schéma ». Chaque zone porte ses machines avec leur code Macc (209 machines).

Le bouton **Reprendre les zones du Pareto laminoir** (Administration → Zones et machines)
applique ce découpage à la base ouverte : les activités passent de l'ancienne zone à la nouvelle,
sont rattachées à une machine quand la désignation la désigne sans ambiguïté (cage 7, KNCA2,
CV3-1…), et gardent sinon l'ancien nom de zone en tête de désignation.

## Réimporter depuis Excel

```bash
pip install openpyxl
python3 outils/import_excel.py "Planning arrêt Été 2026 v0.xlsm" data.json
```

Après un import, ouvrir le fichier dans l'application et cliquer sur **Reprendre les zones du
Pareto laminoir** (Administration). Le script reprend les opérations (onglet _Planning_), le personnel (_bdd personnel_), les
services (_Liste_) et les dates de l'arrêt. Les intervenants sont rapprochés du personnel par
nom ou prénom (« JEROME/OUSMAN » → BOUTIN Jérome, MARNA Ousmane) ; les noms inconnus
(entreprises extérieures : MSEM, ALPA, SIE…) sont créés dans l'équipe « Entreprises / non
référencés ».

## Structure de `data.json`

- `meta` : `admin` (`login`, `sel`, `hash` SHA-256), titre, `debut`, `fin`, `finAffichage`, `jalons[]`, `consignes[]`, `capacite`
  (heures par jour de semaine, 0 = dimanche), `tempsPerdu`, `modeCharge`.
- `zones[]` : `id`, `nom`, `type` (`process`, `general`, `utilite`) et position sur le schéma
  (`x`, `y`, `w`, `h`) ; `flux[]` : ordre des zones dans le sens du produit (flèches).
- `zones[].machines[]` : `id`, `nom` des machines/équipements de la zone.
- `activites[]` : `zone`, `machine` (id de machine, facultatif), `service`, `designation`, `statut` (`afaire`, `encours`, `fait`,
  `nonnecessaire`, `reportee`), `intervenants[]` (ids du personnel), `gmao`, `moi`, `dureeH`,
  `debut`, `fin`, `debutReel`, `pont`, `commentaire`.
- `personnel[]` : `nom`, `prenom`, `matricule`, `poste`, `equipe`, `absences[]` (dates).
- `equipes[]`, `services[]`, `ponts[]`, `reservations[]` (`pont`, `date`, `creneau` M/A/J,
  `type` utilisation/indispo, `activite`, `libelle`, `demandeur`).

Toutes les dates sont au format `AAAA-MM-JJ`.
