# Rapport de non-conformité ALPA (AQA.QUAL.03)

Application web autonome (`index.html`) qui remplit le formulaire PDF
`AQA.QUAL.03.pdf` (indice 5) et génère le rapport à télécharger.

## Utilisation

Ouvrir `index.html` dans un navigateur (Chrome, Edge, Firefox). Une connexion
internet est nécessaire au premier chargement (bibliothèque `pdf-lib`).

1. Cocher **Aciérie / Laminoir / Expédition**.
   - Aciérie → la partie 1.2 (Ronds) est barrée.
   - Laminoir ou Expédition → la partie 1.1 (Billettes) est barrée.
2. Choisir l'**équipe** (A, B, C, D), le **rédacteur** (liste configurable) et la **date**.
3. Compléter la partie 1.1 (Long. = 10.5 m par défaut, Qual. : 200S, 200SG, 240S, 160S)
   ou la partie 1.2.
4. Compléter la partie 2 et choisir le **chef de poste** (liste configurable).
   - Chef de poste = DESOBRY → signature personnelle.
   - Autre chef de poste → signature « PO » (la même signature avec « PO » au-dessus à gauche).
5. **Enregistrer le PDF** (dans le dossier configuré, sinon dans les téléchargements). Les parties 3 à 7 restent vides. Nom du fichier :
   - Aciérie : `AAAA.MM.JJ AQA.QUAL.03 Coulée <qualité> N° <n° de coulée>.pdf`
   - Laminoir / Expédition : `AAAA.MM.JJ AQA.QUAL.03 Fdx <n° fardeau> Coulée <n° de coulée>.pdf`

6. **✉ Partager** : prépare un mail avec l'objet `Fdx NC du JJ/MM/AAAA` et le PDF joint.
   - Mode « Brouillon Outlook » : télécharge un fichier `.eml` ; l'ouvrir lance Outlook
     avec le mail prêt à envoyer (destinataires, objet, pièce jointe).
   - Mode « Partage » : ouvre le menu de partage de Windows ou du téléphone.
7. **📂 Ouvrir le dossier d'enregistrement** : liste les PDF du dossier (du plus récent
   au plus ancien), un clic ouvre le PDF. Un navigateur ne peut pas lancer l'Explorateur Windows.

## Paramètres (⚙)

- Listes des rédacteurs et des chefs de poste.
- Nom du titulaire de la signature (DESOBRY par défaut).
- Signature : à dessiner ou à importer (image sur fond blanc).
- Dossier d'enregistrement (Chrome ou Edge sur ordinateur).
- Destinataires du mail et méthode de partage.

Les paramètres sont enregistrés dans le navigateur du poste (localStorage, et IndexedDB pour le dossier).

## Modifier l'application

`index.html` est généré à partir de `template.html` et du PDF :

```bash
python3 build.py template.html AQA.QUAL.03.pdf index.html
```
