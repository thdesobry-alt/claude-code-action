# Suivi des consommations — Service Laminoir

Application HTML autonome (aucune installation) avec base de données `data.json`.

## Onglets

- **Synthèse** : dépenses du mois (total et par onglet), écart vs mois précédent, suivi des budgets, répartition, évolution sur 6 mois, top 5 des dépenses et points clés.
- **Ricambi** : pièces de rechange par famille (roulements, hydraulique, électrique…).
- **EPI** : silhouette d'opérateur où chaque zone (casque, lunettes, masque, bouchons d'oreille, gants, vêtements, manchettes, chaussures) affiche son % et son montant, colorée du vert (moins cher) au rouge (plus cher).
- **Outillage** : dépenses regroupées par catégorie (vérins, clés, marteaux, levage, mesure…).

Chaque onglet permet d'ajouter, modifier, supprimer et rechercher des lignes. Une désignation déjà connue préremplit la catégorie, la référence et le prix.

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
  "consommations": [
    {
      "id": "c0001",
      "date": "2026-10-02",
      "type": "epi",
      "categorie": "Gants",
      "designation": "Gants anti-coupure niveau D",
      "reference": "GAN-COUP-D",
      "quantite": 21,
      "prixUnitaire": 8.02,
      "demandeur": "Cylindrerie",
      "commentaire": ""
    }
  ]
}
```

`type` vaut `ricambi`, `epi` ou `outillage`. Le fichier fourni contient des données fictives (mai à octobre 2026) à remplacer par les vôtres.
