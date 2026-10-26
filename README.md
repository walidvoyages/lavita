# La Vita Spa — Site web FR / AR

Site vitrine statique bilingue pour La Vita Spa, Sahloul, Sousse.

## Contenu

- **29 pages HTML** en français et en arabe, dont 3 articles de conseils en français.
- **8 nouvelles pages massage à domicile** : une page générale FR/AR et des pages dédiées à **Sousse, Tunis et Nabeul** en FR/AR.
- Section massage à domicile sur les accueils FR/AR, navigation enrichie et liens internes entre les villes.
- Pages services : massages, hammam individuel, soins du visage, rituel hammam + massage.
- Styles CSS améliorés et responsive (`assets/css/enhancements.css`), animations légères, formulaire de demande de rendez-vous ouvrant WhatsApp.
- Le formulaire permet de renseigner la **ville et le quartier** pour les demandes à domicile.
- Balises title/description uniques, données structurées Schema.org, balises hreflang et canonical après configuration du domaine, Open Graph et robots.txt.
- Images WebP optimisées.

## Mise en ligne

Publiez **le contenu de ce dossier à la racine du domaine** (`public_html` chez Hostinger, ou la racine d'un hébergement statique compatible). Le site utilise des chemins absolus commençant par `/` : il ne doit pas être déployé dans un sous-répertoire sans adaptation.

Le site est statique : pas besoin de Node.js ni d'une base de données. Pas de paiement en ligne, d'admin ni de confirmation automatique de réservation. Le formulaire ouvre WhatsApp : c'est une demande, pas une réservation confirmée.

## SEO — étape indispensable à la mise en ligne

1. Editez `seo-config.json` et remplissez `public_domain` avec le domaine réel HTTPS, par exemple `https://www.votre-domaine.tn` (sans barre oblique finale).
2. Exécutez `python3 build.py` depuis le dossier du projet. Cela génère les canonical URLs absolues, les références structurées et `sitemap.xml` / robots.txt pour le domaine publié.
3. Publiez **à nouveau** les fichiers générés.
4. Configurez Google Search Console, vérifiez la propriété et soumettez `/sitemap.xml`.
5. Vérifiez l'exactitude des coordonnées, du nom commercial et des services auprès de l'établissement. Activez / mettez à jour Google Business Profile.

Sans domaine configuré, le site fonctionne, mais le sitemap, les canonicals et les hreflang absolus restent inactifs volontairement pour éviter de soumettre des URLs incorrectes. **Il faut configurer le domaine avant la publication SEO finale**.

## Important : massage à domicile

Les pages de Sousse, Tunis et Nabeul permettent au client de **demander** une intervention à domicile. Elles ne déclarent **aucune antenne à Tunis ou Nabeul** et ne garantissent pas une zone desservie ni un déplacement. Toute prestation à domicile doit être validée par La Vita Spa (disponibilité, tarif, frais de transport, professionnel et rendez-vous). **Vérifiez auprès de La Vita Spa que la prestation à domicile peut réellement être proposée avant de publier ces pages.**

## Coordonnées / réservations

- `25 213 968` : numéro actuellement utilisé dans le bouton WhatsApp.
- `21 870 211` : contact téléphonique complémentaire.
- Instagram : `@la_vita_spa_sousse`.
- Adresse : Rue Pakistan, Sahloul, Sousse.

Ces données proviennent des supports fournis et doivent être confirmées avant publication. Si le numéro WhatsApp change, remplacez `21625213968` dans `assets/js/app.js` (les numéros HTML sont générés dans `build.py`).

## Modification du contenu

Les pages HTML sont produites par `build.py`. Pour changer le contenu global, modifiez `build.py` puis lancez `python3 build.py`. CSS : `assets/css/style.css` et `assets/css/enhancements.css`. JS : `assets/js/app.js`. Images : `assets/img/`.

## Test local

Dans le dossier du projet : `python3 -m http.server 8000`, puis ouvrez `http://localhost:8000/` dans un navigateur. `file://` n'est pas une simulation correcte car les liens du site utilisent des chemins depuis la racine du domaine.

## À noter

L'optimisation technique SEO aide à l'indexation et à la pertinence mais ne garantit pas une position Google précise. Aucun tarif n'a été inventé ; les prix, créneaux et durées sont à confirmer avec le spa.
