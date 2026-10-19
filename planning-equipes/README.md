# Planning des équipes

Application web (un seul fichier HTML) pour gérer le planning de 4 équipes de 11 agents en postes de 12 h.

## Fonctions

- **Agents** : saisie du matricule, du nom, du prénom et de l'équipe (A à D), import par copier-coller depuis Excel (`matricule;nom;prénom;équipe`), création rapide de 4 × 11 fiches à compléter. L'ordre des agents dans chaque équipe se règle librement (flèches ou glisser-déposer) et s'applique au planning et au tableau des heures.
- **Maintien four** : affectation « MF » de jour (8h–20h) ou de nuit (20h–8h), choisie dans la journée d'un agent. Ses heures comptent dans les heures de l'agent ; un agent de production mis en maintien four laisse son poste à remplacer. Ligne « Maintien four » sous les heures jour/nuit du planning.
- **Remplaçants** : rubrique à part (code `REMP` à l'import) pour les renforts de production. Ils n'ont pas de cycle, apparaissent sous les équipes dans le planning et sont proposés en premier pour remplacer un absent.
- **Polyvalence** : une matrice par équipe (et pour les remplaçants), opérateurs en lignes et fonctions en colonnes ; chaque case passe par maîtrisé (vert), en formation (orange), non maîtrisé (rouge), non concerné (noir). Les colonnes se gèrent dans l'onglet ; une ligne de pied compte les opérateurs qui maîtrisent chaque fonction. Stockée dans `polyvalence` du fichier JSON.
- **Début de contrat** : date facultative (onglet Agents ou formulaire d'ajout, confirmée avec « Valider ») ; l'agent apparaît dans le planning à partir de ce mois, les jours précédents sont hachurés et ne comptent ni heures ni effectif.
- **Fin de contrat** : date saisie dans l'onglet Agents puis confirmée avec « Valider » (rien n'est enregistré pendant la saisie) ; l'agent reste visible jusqu'à la fin de ce mois (jours suivants hachurés), disparaît ensuite du planning, de la polyvalence et des remplacements, et ses mois de présence restent dans la base.
- **Changement d'équipe** : choisir la nouvelle équipe demande une date d'effet (ou « correction d'erreur ») ; l'historique est conservé dans `moves` de la fiche. Le mois du changement, l'agent apparaît dans ses deux équipes, chacune avec ses heures ; ensuite seulement dans la nouvelle.
- **Cycle** : motif de rotation répété par chaque équipe (par défaut le cycle de 28 jours du lundi au dimanche : 6 jours 8h–20h, 6 nuits 20h–8h, 16 repos, les équipes décalées d'une semaine), date de départ et décalage par équipe, avec aperçu et contrôle de couverture.
- **Planning mensuel** : grille jour par jour de toutes les équipes. Un clic sur la ligne d'une équipe la passe en jour, nuit ou repos à une date donnée ; un clic sur la case d'un agent ouvre sa journée.
- **Congés et absences** : CP, RTT, maladie ou autre, sur un jour ou une période (option « seulement les jours travaillés »).
- **Absences partielles** : sur un poste de jour ou de nuit, une absence de quelques heures (par exemple 8h–10h) avec son motif ; ces heures sont retirées des heures travaillées.
- **Remplacements** : pour une absence sur un poste travaillé, la liste des agents en repos disponibles, triés par heures de la semaine, avec alertes (sortie de nuit, enchaînement nuit → jour, dépassement du plafond hebdomadaire). Remplacement sur un jour ou sur toute l'absence. Les postes restant à remplacer sont listés en haut du planning.
- **Effectifs** : nombre d'agents en jour et en nuit pour chaque date, comparé à l'effectif cible. Lignes « Heures jour » et « Heures nuit » : heures réalisées chaque jour par les agents en poste (absences partielles déduites), avec le total du mois.
- **Heures** : heures réalisées (jusqu'à la veille incluse ; les jours à venir ne sont pas comptés, les heures prévues apparaissent au survol) par agent et par semaine calendaire (lundi–dimanche), total du mois, nuits comptées en entier le jour de prise de poste (option : réparties à minuit, 4 h + 8 h), export vers Excel par copier-coller.

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
