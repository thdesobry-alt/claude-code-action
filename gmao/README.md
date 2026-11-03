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
