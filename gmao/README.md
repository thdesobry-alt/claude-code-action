# GMAO Ligne

Outil de suivi d'usure en un seul fichier HTML, avec une base JSON.

## Utilisation

1. Placez `gmao.html` et `gmao-data.json` dans un dossier partagé.
2. Ouvrez `gmao.html` dans Chrome ou Edge.
3. **📂 Ouvrir BDD** → choisissez `gmao-data.json`. **💾 Enregistrer** (ou Ctrl+S) écrit directement dans ce fichier.
   Si quelqu'un a modifié le fichier entre-temps, l'outil vous prévient avant de l'écraser.
   Sous Firefox, l'enregistrement télécharge un nouveau `gmao-data.json` qui remplace l'ancien.

## Principe

- Chaque équipement a deux compteurs : **heures** et **tonnes** (bouton ⏱ Relevé compteurs).
- Chaque organe est suivi en heures **ou** en tonnes (au choix, page 🎚 Seuils ou ✏️ sur l'organe), avec un seuil de vigilance et un seuil de remplacement.
- Usure = compteur actuel − compteur au dernier remplacement.
  - 🟢 vert : sous le seuil de vigilance
  - 🟠 orange : seuil de vigilance atteint
  - 🔴 rouge : seuil de remplacement atteint
- **🔁 Remplacé** remet l'usure de l'organe à zéro et l'inscrit au journal (exportable en CSV).

Les seuils et compteurs livrés dans `gmao-data.json` sont des **exemples** : remplacez-les par vos valeurs.

## Modèle des organes (v2)

- **TRO-0** : galet supérieur (écrase la billette), galet inférieur, un vérin pneumatique de serrage de chaque côté (côté piste / côté moteur), flexibles.
- **Soudeuse** : bagues acier et téflon suivies séparément pour le vérin offsetting supérieur et pour l'inférieur (une bague à chaque bout du vérin), 4 galets porteurs (2 à l'avant côté piste, 2 à l'arrière côté moteur).

Une base créée avec l'ancien modèle est convertie automatiquement à l'ouverture : les organes dédoublés gardent l'usure de l'organe d'origine, et les galets porteurs démarrent à zéro. Enregistrez ensuite le fichier.

## Soudeuse en 3D

La soudeuse est dessinée uniquement en 3D. « Vue côté piste » et « Vue côté moteur » orientent la machine, ⟲ / ⟳ la font tourner, et on peut aussi glisser sur le dessin. Les couleurs d'état et le clic sur une pièce fonctionnent comme sur les autres dessins.

Organes suivis en plus : rail côté piste, rail côté moteur, crémaillère (le long du rail côté moteur, elle fait avancer la soudeuse). Une base existante les reçoit automatiquement à l'ouverture, avec un suivi qui démarre à zéro.

## Centrale Nortek

Cuve de centrale, 2 pompes de fonctionnement (en bas à gauche) suivies du filtre avant envoi dans les coffrets, pompe de recirculation (en bas à droite) avec ses 2 filtres, et EV de retour à la bâche. Une base existante reçoit la centrale automatiquement à l'ouverture : elle prend les compteurs de la centrale hydraulique enfournement et son suivi démarre à zéro.

## Voies à rouleaux motorisées

La voie rouleaux enfournement est dessinée avec un palier à chaque bout de chaque rouleau et un motoréducteur en haut. C'est une option de l'équipement (« Modifier l'équipement » → « Voie à rouleaux motorisée »), qu'on peut aussi activer sur la voie de chargement. Paliers et motoréducteurs sont dessinés en gris : ils ne sont pas suivis pour l'instant.

## Pousseuse

Chaque bras a son propre moteur et son propre réducteur sur le dessin. Ils apparaissent en gris (« non suivi ») tant qu'aucun organe ne leur est rattaché : pour les suivre, « Ajouter un organe » et choisir l'emplacement « Moteur bras gauche », « Réducteur bras droit », etc.
