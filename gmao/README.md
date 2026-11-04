# GMAO Ligne

Outil de suivi d'usure en un seul fichier HTML, avec une base JSON.

## Utilisation

1. Placez `gmao.html` et `gmao-data.json` dans un dossier partagé.
2. Ouvrez `gmao.html` dans Chrome ou Edge.
3. **📂 Ouvrir BDD GMAO** → choisissez `gmao-data.json`. **💾 Enregistrer** (ou Ctrl+S) écrit directement dans ce fichier.
   Si quelqu'un a modifié le fichier entre-temps, l'outil vous prévient avant de l'écraser.
   Sous Firefox, l'enregistrement télécharge un nouveau `gmao-data.json` qui remplace l'ancien.

## Principe

- Tout est suivi **à la tonne** : chaque organe a un seuil de vigilance et un seuil de remplacement en tonnes (page 🎚 Seuils ou ✏️ sur l'organe).
- Le tonnage vient de la base production (page 🏭 Production) ; sans base production, il se saisit avec « ⚖️ Saisir tonnages ».
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

Une deuxième image sous le dessin de la centrale montre les coffrets **LAO 2, LAO 3 et LAO 4**, tous identiques : en haut la tuyauterie d'air (filtre, manomètre réglable, EV, pressostat), en bas la tuyauterie d'huile (compteur, EV principale, puis ligne A et ligne B avec chacune une EV et un pressostat). Chaque composant est un organe suivi (10 par coffret).


Cuve de centrale, 2 pompes de fonctionnement (en bas à gauche) suivies du filtre avant envoi dans les coffrets, pompe de recirculation (en bas à droite) avec ses 2 filtres, et EV de retour à la bâche. Une base existante reçoit la centrale automatiquement à l'ouverture : elle prend les compteurs de la centrale hydraulique enfournement et son suivi démarre à zéro.

## Voies à rouleaux motorisées

La voie rouleaux enfournement est dessinée avec un palier à chaque bout de chaque rouleau et un motoréducteur en haut. C'est une option de l'équipement (« Modifier l'équipement » → « Voie à rouleaux motorisée »), qu'on peut aussi activer sur la voie de chargement. Les deux voies (enfournement et chargement) sont motorisées : chaque rouleau a son moteur, suivi au tonnage comme un organe (« Moteur R1 », « Moteur R2 »…, emplacement « Moteur du rouleau n°k »). Les paliers et réducteurs restent en gris, non suivis.

## Pousseuse

Chaque bras a son propre moteur, son propre réducteur et une noix mécanique au milieu du bras sur le dessin. Ils apparaissent en gris (« non suivi ») tant qu'aucun organe ne leur est rattaché : pour les suivre, « Ajouter un organe » et choisir l'emplacement « Moteur bras gauche », « Réducteur bras droit », « Noix mécanique bras gauche », etc.

## Défourneuse

Galet supérieur et galet inférieur, deux vérins pneumatiques (côté piste / côté moteur) qui pressent le galet supérieur sur la billette, et un moteur hydraulique par galet. Une base existante reçoit ces 6 organes à l'ouverture, avec un suivi qui démarre à zéro.

## Centrale hydraulique enfournement

3 pompes (moteur au-dessus de chaque pompe), filtre et réservoir. Dans une base existante, l'ancienne pompe devient « Pompe 1 » (son usure est conservée) et les pompes 2 et 3 sont ajoutées avec un suivi qui démarre à zéro.

## Base production (tonnages par diamètre)

Page « 🏭 Production » (si on choisit par erreur la base production avec « Ouvrir BDD GMAO », elle est reconnue et connectée comme base production) :

1. **Connexion** : « Choisir le fichier production… » (ex. `base_production_laminoir.json` sur le dossier partagé), ou « Adresse web » si la base est servie par un serveur. Le choix est mémorisé : à chaque ouverture, la GMAO relit automatiquement la dernière version du fichier. Si le navigateur demande une autorisation, cliquer « 🏭 Reconnecter la production » dans le bandeau (et choisir « Autoriser à chaque visite »).
2. **Diamètres par équipement** : cocher les diamètres qui font travailler chaque équipement (aucun coché = tous les diamètres). Aussi modifiable dans « Modifier l'équipement ».
3. **Calcul** : pour un organe suivi en tonnes, usure = tonnes produites dans les diamètres de l'équipement depuis la date de son dernier remplacement (journées de production à partir de cette date incluse), + les tonnes antérieures au début de la base si on les a saisies dans la fiche de l'organe. Les heures restent saisies par relevé.

Si la base n'est pas joignable, la GMAO utilise la dernière copie lue (gardée dans le navigateur) et le signale dans le bandeau.

## Suivi à la tonne uniquement

Le compteur d'heures a été supprimé. À l'ouverture d'une base qui contenait des organes suivis en heures, leurs seuils sont convertis en tonnes avec une cadence moyenne de 85 t/h (ex. 2 000 h → 170 000 t), et une ligne est ajoutée au journal. Ces seuils convertis sont à vérifier sur la page 🎚 Seuils.

## Arrêts techniques

Page « 🛠 Arrêts techniques » : ajouter, modifier ou supprimer les arrêts (date de début, fin facultative, libellé) et régler le délai de vigilance (30 jours par défaut). Pour chaque arrêt à venir, la page liste les organes à remplacer.

Chaque organe se remplace soit **à la tonne** (seuils de vigilance et de remplacement en tonnes), soit **aux arrêts techniques** : « remplacer tous les N arrêts » (1 = à chaque arrêt, 2 = un arrêt sur deux…). Pour un organe aux arrêts :

- les arrêts comptés sont ceux passés depuis la date de son dernier remplacement (un arrêt le jour même du remplacement ne compte pas) ;
- 🟠 orange quand l'arrêt où il doit être remplacé arrive dans le délai de vigilance ;
- 🔴 rouge si cet arrêt est passé sans que le remplacement soit déclaré.

Le choix se fait dans la fiche de l'organe (✏️) ou sur la page 🎚 Seuils. À la déclaration d'un remplacement, on peut choisir l'arrêt technique pendant lequel il a été fait.

## Curseur et centrale hydraulique curseur

- **Curseur** : en bas, le vérin hydraulique curseur relié par un tronçon au vérin pneumatique curseur monté en sens opposé au bout ; au-dessus, décalé vers la droite, le vérin déviateur ; encore au-dessus, décalé vers la droite, le vérin séparateur.
- **Centrale hydraulique curseur** : même dessin que la centrale d'enfournement (réservoir, filtre, pompes). Elle a 2 pompes ; le nombre de pompes (1 à 3) se règle dans « Modifier l'équipement ».

Une base existante reçoit ces deux équipements à l'ouverture, avec un suivi qui démarre à zéro.

## TRO-0 : entraînement

À gauche des galets : un moteur, un réducteur, et deux allonges qui relient le réducteur au galet supérieur et au galet inférieur. Les flexibles des deux vérins descendent sous le TRO-0 jusque sous le moteur, où ils sont reliés à une EV. Le moteur, le réducteur, les allonges et l'EV sont suivis ; une base existante les reçoit à l'ouverture, avec un suivi qui démarre à zéro.

## Soudeuse : mors et transfos

- Les mors sont suivis séparément : côté four (à gauche) supérieur et inférieur, côté train de laminage (à droite) supérieur et inférieur. Une base existante convertit l'ancien « Mors » en 4 organes qui reprennent son usure.
- Les transfos sont dessinés derrière la soudeuse (côté moteur), avec un éclair jaune (symbole électrique) sur chaque face, et reliés aux mors par des barres de courant.

## Centrale TRO-7 CV5

Centrale hydraulique à 2 pompes, sans cuve (option « Centrale sans cuve » dans « Modifier l'équipement »). Le filtre est dessiné mais n'est pas suivi tant qu'aucun organe ne lui est rattaché. Une base existante reçoit cette centrale à l'ouverture, avec un suivi qui démarre à zéro.

## Moteurs de cage

Onglet « ⚙️ Moteurs de cage » : les moteurs des cages 1 à 16, dessinés en deux rangées, chacun suivi comme un organe (seuils, remplacement, arrêts techniques). Le tableau « Diamètres travaillés par cage » permet de cocher, pour chaque cage, les diamètres dans lesquels elle travaille : son moteur ne compte que les tonnes produites dans ces diamètres (sans case cochée : tous les diamètres). Une base existante reçoit ces 16 moteurs à l'ouverture, avec un suivi qui démarre à zéro.
