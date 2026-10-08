# Planning des équipes

Application web (un seul fichier HTML) pour gérer le planning de 4 équipes de 11 agents en postes de 12 h.

## Fonctions

- **Agents** : saisie du matricule, du nom, du prénom et de l'équipe (A à D), import par copier-coller depuis Excel (`matricule;nom;prénom;équipe`), création rapide de 4 × 11 fiches à compléter. L'ordre des agents dans chaque équipe se règle librement (flèches ou glisser-déposer) et s'applique au planning et au tableau des heures.
- **Cycle** : motif de rotation répété par chaque équipe (par défaut le cycle de 28 jours du lundi au dimanche : 6 jours 8h–20h, 6 nuits 20h–8h, 16 repos, les équipes décalées d'une semaine), date de départ et décalage par équipe, avec aperçu et contrôle de couverture.
- **Planning mensuel** : grille jour par jour de toutes les équipes. Un clic sur la ligne d'une équipe la passe en jour, nuit ou repos à une date donnée ; un clic sur la case d'un agent ouvre sa journée.
- **Congés et absences** : CP, RTT, maladie ou autre, sur un jour ou une période (option « seulement les jours travaillés »).
- **Absences partielles** : sur un poste de jour ou de nuit, une absence de quelques heures (par exemple 8h–10h) avec son motif ; ces heures sont retirées des heures travaillées.
- **Remplacements** : pour une absence sur un poste travaillé, la liste des agents en repos disponibles, triés par heures de la semaine, avec alertes (sortie de nuit, enchaînement nuit → jour, dépassement du plafond hebdomadaire). Remplacement sur un jour ou sur toute l'absence. Les postes restant à remplacer sont listés en haut du planning.
- **Effectifs** : nombre d'agents en jour et en nuit pour chaque date, comparé à l'effectif cible. Lignes « Heures jour » et « Heures nuit » : heures réalisées chaque jour par les agents en poste (absences partielles déduites), avec le total du mois.
- **Heures** : heures travaillées par agent et par semaine calendaire (lundi–dimanche), total du mois, nuits comptées en entier le jour de prise de poste (option : réparties à minuit, 4 h + 8 h), export vers Excel par copier-coller.

## Utilisation à plusieurs avec un fichier JSON partagé

1. Placez `index.html` et `planning-data.json` dans un dossier partagé (lecteur réseau, OneDrive ou SharePoint synchronisé…).
2. Chaque utilisateur ouvre `index.html` avec **Google Chrome** ou **Microsoft Edge**, indique son nom, puis « Ouvrir un fichier de planning… » et choisit `planning-data.json` (ensuite « Rouvrir » suffit).
3. Le premier qui ouvre le fichier le modifie ; il est verrouillé à son nom. Les autres le voient en lecture seule, mis à jour toutes les 30 secondes, avec le nom de la personne qui l'utilise.
4. En fin de travail, cliquez « Fermer et libérer le fichier ». Un verrou oublié expire 15 minutes après la fermeture de la page. « Prendre la main » permet de forcer, après confirmation.
5. Chaque enregistrement relit d'abord le fichier : si quelqu'un d'autre l'a modifié entre-temps, rien n'est écrasé et l'application demande de recharger.

`planning-data.exemple.json` montre la structure du fichier (cycle, agents, mois). Le fichier réel `planning-data.json` contient des données personnelles et n'est pas versionné (`.gitignore`). Firefox et Safari ne peuvent que consulter le fichier.

## Utilisation

- `planning.html` est la source publiée comme artefact claude.ai : les données y sont enregistrées dans la base partagée de l'artefact.
- `index.html` est la version autonome à ouvrir dans un navigateur : ses données sont dans le fichier JSON partagé décrit ci-dessus (ou, au choix, dans le navigateur seulement). Elle se régénère avec `./build.sh` après toute modification de `planning.html`.
