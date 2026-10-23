# Suivi des consommations — Service Laminoir

Application HTML autonome (aucune installation) avec base de données `data.json`.

## Onglets

- **Synthèse** : dépenses du mois (total et par onglet) avec l'écart vs mois précédent, répartition, évolution sur 6 mois, points clés et **Top 10 des plus grosses dépenses du mois**.
- **Ricambi** : **dépenses par machine** (Descrizione2). Cliquer une machine affiche le **top 5** de ses plus grosses dépenses ; dessous, le **TOP 10 des articles les plus coûteux**.
- **EPI** : silhouette d'opérateur où chaque zone (casque, lunettes, masque, bouchons d'oreille, gants, vêtements, manchettes, chaussures) affiche son % et son montant, du vert canard (moins cher) au rouge (plus cher). Cliquer un EPI (silhouette ou classement) affiche le **top 10** de ses dépenses.
- **Outillage** : dépenses regroupées par catégorie (vérins, clés, marteaux, levage, mesure…). Cliquer une catégorie affiche son **top 10**.

Chaque onglet a son tableau « Détail du mois » et un formulaire de saisie manuelle (✎ pour modifier, ✕ pour supprimer).

## Filtrer et trier les tableaux

Tous les tableaux ont une ligne de filtres sous les titres de colonnes :

- texte : contient (sans tenir compte des majuscules ni des accents), ex. `gant` ;
- nombres : `>100`, `<50`, `>=10`, `=3`, ou une partie du nombre affiché ;
- cliquer un titre de colonne trie (re-cliquer inverse le sens) ;
- le pied du tableau donne le nombre de lignes et le total de la valeur filtrée.

La liste **Autorisant** de l'en-tête filtre toute l'application sur un « Nome Autorizzante ».

## Importer l'extraction (copier-coller)

1. Dans l'extraction des consommations, sélectionnez le tableau (de préférence avec la ligne de titres Soc., Mag., … Valore … Nome Autorizzante … Descrizione2), puis copiez-le.
2. Dans l'application, faites **Ctrl+V n'importe où sur la page** (ou bouton **📋 Coller les données**). L'import et la mise à jour sont immédiats.

- Les lignes collées **s'ajoutent** aux données existantes. Une ligne déjà présente (même date, document, produit, quantité, valeur, prélevant et autorisant) n'est pas ajoutée deux fois : on peut recoller une extraction qui chevauche la précédente.
- **↶ Annuler le dernier collage** (bas de page) retire les lignes du dernier collage.
- Les données de démonstration disparaissent au premier collage.
- Le montant utilisé est la colonne **Valore** ; la date est **Data Documento**. Sans ligne de titres, les colonnes sont lues dans l'ordre standard de l'extraction.
- **Onglet** : déterminé par **Descrizione2** (« … PROTECTION INDIVIDUEL » → EPI, « … OUTILLAGE … » → Outillage, le reste → Ricambi, rangé par machine).
- **Catégorie** : EPI et Outillage sont classés par mots-clés de la désignation (CASQUE, GANT, LUNETTE, VERIN, CLE, MARTEAU…). Une ligne mal classée se corrige avec ✎.

## Utilisation

1. Ouvrir `index.html` dans Chrome ou Edge.
2. **📂 Ouvrir JSON** : charger `data.json`. Dans Chrome/Edge, **💾 Enregistrer JSON** réécrit ensuite directement ce fichier ; sinon un nouveau `data.json` est téléchargé et remplace l'ancien.
3. Les saisies sont aussi sauvegardées automatiquement dans le navigateur entre deux enregistrements.
4. **⬇ CSV du mois** : export pour Excel (filtre autorisant appliqué).

Servie par un serveur web (ex. `python3 -m http.server` dans ce dossier), l'application charge `data.json` automatiquement au premier lancement. Ouverte en double-cliquant, elle démarre sur les données de démonstration intégrées tant qu'aucun fichier n'a été ouvert.

## Format de `data.json`

```json
{
  "service": "Laminoir",
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
      "machine": "409504",
      "document": "6359",
      "commentaire": "",
      "source": "import"
    }
  ]
}
```

`type` vaut `ricambi`, `epi` ou `outillage` ; `source` vaut `import`, `manuel` ou `demo`. Le fichier fourni contient des données fictives (mai à octobre 2026, noms inventés) qui disparaissent au premier collage.
