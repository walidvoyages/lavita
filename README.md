# La Vita Spa — Site web FR / AR

Site vitrine statique bilingue pour La Vita Spa, Sahloul, Sousse.

## Contenu

- 21 routes HTML indexables en français et en arabe, dont 3 articles en français.
- Pages services : massages, hammam individuel, soins du visage, rituel hammam + massage.
- Affichage responsive, animations légères et formulaire de demande de rendez-vous qui ouvre WhatsApp.
- Balises title/description, données structurées Schema.org, hreflang, Open Graph et robots.txt.
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

Sans domaine configuré, le site fonctionne, mais le sitemap et les canonicals absolus sont laissés inactifs volontairement pour éviter de soumettre des URLs incorrectes.

## Coordonnées / réservations

- `25 213 968` : numéro actuellement utilisé dans le bouton WhatsApp.
- `21 870 211` : contact téléphonique complémentaire.
- Instagram : `@la_vita_spa_sousse`.
- Adresse : Rue Pakistan, Sahloul, Sousse.

Ces données proviennent des supports fournis et doivent être confirmées avant publication. Si le numéro WhatsApp change, remplacez `21625213968` dans `assets/js/app.js` (les numéros HTML sont générés dans `build.py`).

## Modification du contenu

Les pages HTML sont produites par `build.py`. Pour changer le contenu global, modifiez `build.py` puis lancez `python3 build.py`. CSS : `assets/css/style.css`. JS : `assets/js/app.js`. Images : `assets/img/`.

## Test local

Dans le dossier du projet : `python3 -m http.server 8000`, puis ouvrez `http://localhost:8000/` dans un navigateur. `file://` n'est pas une simulation correcte car les liens du site utilisent des chemins depuis la racine du domaine.

## À noter

L'optimisation technique SEO aide à l'indexation et à la pertinence mais ne garantit pas une position Google précise. Aucun tarif n'a été inventé ; les prix, créneaux et durées sont à confirmer avec le spa.
