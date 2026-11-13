# Maison Dorlote : plan du site

## Principes

1. **Le client arrive via Google Ads pour acheter.** La page d'accueil est une page de vente. Le prix et le bouton d'achat sont accessibles immédiatement.
2. **Simplicité** : un seul produit, un seul parcours, aucun popup intrusif, aucune étape inutile.
3. **Honnêteté** : pas de faux avis, faux prix barrés, faux comptes à rebours ni fausses alertes de stock. C'est aussi une condition pour que Google Merchant Center ne suspende pas le compte.

## Page d'accueil (= page produit) : « produit d'abord » (13/11)

Le client venu de Google doit voir la photo, le prix et le bouton d'achat **sans défiler**, sur mobile comme sur ordinateur.

1. **Barre d'annonce** : livraison offerte · satisfait ou remboursé 30 jours (· garantie 2 ans sur ordinateur).
2. **En-tête** : logo, FAQ, panier.
3. **Bloc d'achat en premier** (ordinateur : galerie à gauche, fiche à droite collante ; mobile : galerie qui glisse puis fiche) :
   - galerie : 1. lampe seule allumée, 2. maman de nuit, 3. tactile, 4. poignée, 5. lumière neutre, 6. chambre d'enfant (compteur « 1 / 6 » sur mobile) ;
   - nom, promesse « La lumière qui ne réveille personne. », prix, offres 1 ou 2 lampes (côte à côte sur mobile) ;
   - « Ajouter au panier », « Acheter maintenant » (paiement express), « En stock » et date de livraison estimée ;
   - idée cadeau, réassurance, logos de paiement ;
   - **volets** : Description (ouvert), Caractéristiques, Livraison et retours, Questions fréquentes.
   - Mesure : bouton d'achat visible dès l'arrivée (mobile 390 × 844 : haut du bouton à environ 740 px ; ordinateur 1440 × 900 : environ 680 px).
4. **Récit** : la grande image sombre de la maman, avec le titre et le problème de 3 h du matin.
5. Avant/après, teintes, gestes, usages, sécurité, comparatif, avis, FAQ complète, garanties, dernier appel, contact.
6. **Barre d'achat fixe sur mobile** dès que le bouton d'achat est dépassé.

## Formulaire de contact (bas de page, ancre #contact)

- Prénom, nom, canal de réponse au choix (email, SMS, appel) et coordonnée correspondante.
- Thème : la lumière, batterie et recharge, durée de vie, garantie, livraison, retours, ma commande, autre.
- **Réponse rapide** : dès qu'un thème est choisi, la réponse de la FAQ s'affiche, ce qui évite souvent l'envoi.
- Numéro de commande facultatif pour le thème « Ma commande ».
- Consentement RGPD obligatoire, validation en français, écran de confirmation.
- Engagement affiché : réponse sous 24 h, les jours ouvrés.
- Dans Shopify : formulaire de contact natif (`{% form 'contact' %}`), les messages arrivent dans la boîte mail de la boutique. Les réponses par SMS ou appel se font à la main.

## Logos de paiement
- Maquette : icônes officielles de la bibliothèque `payment_icons` (MIT), celles utilisées par Shopify.
- Thème Shopify : afficher **uniquement les moyens réellement activés** avec `{% for type in shop.enabled_payment_types %}{{ type | payment_type_svg_tag: class: 'pi' }}{% endfor %}`, et le bouton de paiement express natif (`{{ form | payment_button }}`).

## Panier (tiroir latéral)

- Jauge de livraison offerte (« Plus que X € pour la livraison offerte »).
- Proposition de l'adaptateur secteur USB-C en un clic.
- Accès direct au paiement Shopify.

## FAQ, questions prévues

- Est-ce que la lumière éblouit ? Peut-on la régler très bas ?
- Quelle autonomie ? Comment la recharger ? L'adaptateur est-il fourni ?
- Peut-on l'utiliser dans une chambre de bébé ? Chauffe-t-elle ?
- Quelle différence entre les versions avec et sans horloge, avec et sans télécommande ?
- Comment fonctionne la minuterie ?
- Quels délais de livraison ? Le suivi ?
- Comment retourner le produit ? Qui paie le retour ?
- Quelle garantie ?
- Comment vous contacter ?

## Autres pages

- FAQ complète, contact.
- Pages légales : mentions légales, CGV, confidentialité, retours et rétractation, livraison.

## Exigences Google Ads et Merchant Center

- Coordonnées visibles (email, adresse), politiques de retour et de livraison accessibles.
- Délais de livraison réels et cohérents partout.
- Prix identique sur le site et dans le flux produit.
- Aucune allégation trompeuse.

## Informations manquantes avant mise en ligne

Prix de vente, seuil de livraison offerte, délais réels, réponses du fournisseur, coordonnées de l'entreprise (SIRET, adresse), médiateur de la consommation.
