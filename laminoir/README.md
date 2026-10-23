# Suivi des consommations — Service Laminoir

Application HTML autonome (aucune installation) avec base de données `data.json`.

## Onglets

- **Synthèse** : dépenses du mois (total et par onglet), écart vs mois précédent, suivi des budgets, répartition, évolution sur 6 mois, dépenses par autorisant, top 5 des dépenses et points clés.
- **Ricambi** : pièces de rechange par famille (roulements, hydraulique, électrique…).
- **EPI** : silhouette d'opérateur où chaque zone (casque, lunettes, masque, bouchons d'oreille, gants, vêtements, manchettes, chaussures) affiche son % et son montant, colorée du vert (moins cher) au rouge (plus cher).
- **Outillage** : dépenses regroupées par catégorie (vérins, clés, marteaux, levage, mesure…).

Chaque onglet permet d'ajouter, modifier, supprimer et rechercher des lignes. Une désignation déjà connue préremplit la catégorie, la référence et le prix.

## Importer l'extraction (copier-coller)

1. Dans l'extraction des consommations, sélectionnez **tout le tableau, ligne de titres comprise** (Soc., Mag., … Valore … Nome Autorizzante … Descrizione2), puis copiez-le.
2. Dans l'application, faites **Ctrl+V n'importe où sur la page** (ou bouton **📋 Coller les données**). L'import et la mise à jour sont immédiats.

- Le montant utilisé est la colonne **Valore** ; la date est **Data Documento**.
- Chaque nouveau collage **remplace** l'import précédent et les données de démo. Les lignes saisies à la main sont conservées.
- Si la ligne de titres manque, les colonnes sont lues dans l'ordre standard de l'extraction.
- **Onglet** : déterminé par **Descrizione2** (« … PROTECTION INDIVIDUEL » → EPI, « … OUTILLAGE … » → Outillage, le reste → Ricambi). Le tableau « Classement des familles » de la Synthèse permet de corriger une famille ; le choix est mémorisé pour les imports suivants.
- **Catégorie** : EPI et Outillage sont classés par mots-clés de la désignation (CASQUE, GANT, LUNETTE, VERIN, CLE, MARTEAU…) ; les Ricambi prennent la famille Descrizione2. Une ligne mal classée se corrige avec ✎.

## Filtre et extraction par autorisant

- Liste **Autorisant** dans l'en-tête : filtre toute l'application sur un « Nome Autorizzante ».
- Synthèse → **Dépenses par autorisant** : montant par onglet pour chaque autorisant du mois ; cliquer un nom active le filtre, **⬇ CSV** extrait ses lignes.
- **⬇ CSV du mois** exporte le mois en tenant compte du filtre.

## Utilisation

1. Ouvrir `index.html` dans Chrome ou Edge.
2. **📂 Ouvrir JSON** : charger `data.json`. Dans Chrome/Edge, **💾 Enregistrer JSON** réécrit ensuite directement ce fichier ; sinon un nouveau `data.json` est téléchargé et remplace l'ancien.
3. Les saisies sont aussi sauvegardées automatiquement dans le navigateur entre deux enregistrements.
4. **⬇ CSV du mois** : export pour Excel.

Servie par un serveur web (ex. `python3 -m http.server` dans ce dossier), l'application charge `data.json` automatiquement au premier lancement. Ouverte en double-cliquant, elle démarre sur les données de démonstration intégrées tant qu'aucun fichier n'a été ouvert.

## Format de `data.json`

```json
{
  "service": "Laminoir",
  "budgets": { "ricambi": 22000, "epi": 4500, "outillage": 4000 },
  "categories": { "ricambi": ["…"], "epi": ["…"], "outillage": ["…"] },
  "mapping": { "LAMINOIR.XXX": "outillage" },
  "consommations": [
    {
      "id": "c0001",
      "date": "2026-10-02",
      "type": "epi",
      "categorie": "Gants",
      "designation": "Gants anti-coupure niveau D",
      "reference": "GAN-COUP-D",
      "quantite": 21,
      "valeur": 168.42,
      "prelevant": "KEVIN",
      "autorisant": "DUPONT CLAIRE",
      "famille": "LAMINOIR.EQUIPEMENT DE PROTECTION INDIVIDUEL",
      "document": "6359",
      "commentaire": "",
      "source": "import"
    }
  ]
}
```

`type` vaut `ricambi`, `epi` ou `outillage` ; `source` vaut `import`, `manuel` ou `demo`. Le fichier fourni contient des données fictives (mai à octobre 2026, noms inventés) qui disparaissent au premier collage.
