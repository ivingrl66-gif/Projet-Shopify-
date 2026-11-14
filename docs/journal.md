# Journal du projet Maison Dorlote (ex-Nuitelle)

Dernière mise à jour : 13 novembre 2026.

## Où en est-on

La **maquette du site est quasi terminée** et validée par le propriétaire (« travail fabuleux »). Elle attend les informations du fournisseur et le SIRET pour devenir publiable, puis sa transformation en thème Shopify.

## Décisions prises

### Marque
- **Nom** : Nuitelle. ⚠️ Vérifier INPI et EUIPO (proximité phonétique avec Nutella) et la disponibilité de nuitelle.fr. Le .com est pris ; .store, .net et .org étaient disponibles.
- **Slogan** : « La lumière qui ne réveille personne. »
- **Cible** : jeunes parents (biberon de 3 h, change, chambre de bébé). Cibles secondaires : cadeau de naissance (grands-parents, proches), chambre d'enfant (peur du noir), lecture au lit.
- **Identité** : « Nuit ambrée » (voir `DESIGN.md`). Polices Fraunces et Figtree, vouvoiement.
- **Logo** : « l'arche lumineuse », validé après une première version jugée « moyenne ».

### Offre
- **Boutique mono-produit**. Pas de second produit avant d'avoir des ventes.
- **Prix proposés, à valider** : 34,90 € la lampe, 59,90 € le lot de 2 (soit 29,95 € la lampe), adaptateur secteur USB à 7,90 € proposé dans le panier.
- **Livraison offerte dès 40 €**, avec jauge dans le panier.
- **Satisfait ou remboursé 30 jours**, garantie légale 2 ans.
- **Option cadeau** : case « C'est pour offrir » et message dans le panier.
- Réponse aux questions sous 24 h, les jours ouvrés.

### Site (maquette)
Accueil = page de vente, dans cet ordre :
1. image plein écran ;
2. bloc d'achat ;
3. avant/après interactif ;
4. sélecteur des 3 teintes ;
5. les 3 gestes ;
6. usages (03:12, 21:30, 23:45, avec l'heure sur la lampe qui correspond) ;
7. sécurité bébé ;
8. comparatif ;
9. caractéristiques ;
10. bandeau avis (vide, honnête) ;
11. FAQ filtrable (14 questions) ;
12. garanties ;
13. dernier appel ;
14. formulaire de contact avec réponses rapides par thème.

Mobile : barre d'achat fixe en bas. Panier : jauge, adaptateur, option cadeau.

### Visuels
11 images générées par IA à partir des photos réelles du TL-0191, validées (« les visuels sont parfaits »). L'avant-après a été retouché à la demande : la mère se protège légèrement les yeux sous le plafonnier, sans exagération.

## En attente

### Côté fournisseur (TL-0191, Alibaba) : messages prêts dans `docs/messages-fournisseur.md`
- 🚩 **Marquage CE, RoHS, documents batterie (UN38.3 / MSDS)** : bloquant pour vendre en Europe (la fiche Alibaba indique « Certification : Aucun »).
- Prix par quantité, livraison comprise ; délais vers la France ; entrepôt UE ; dropshipping possible ?
- Batterie (mAh, autonomie, temps de charge), port de charge, valeurs en Kelvin.
- Contenu de la boîte, adaptateur, couleur de la poignée, version avec télécommande.
- Chaleur des LED ; colis neutre sans prix ni facture ; carte message cadeau ; logo sur la boîte.
- Échantillon : à commander dès que possible (photos et vidéo maison, vérifications).
- Minimum de commande de 50 pièces : négocier 30, ou passer par un agent (CJdropshipping) ou un second fournisseur.

### Côté propriétaire
- Créer la micro-entreprise sur formalites.entreprises.gouv.fr (gratuit), cocher l'ACRE. Attendre le SIRET (10 à 30 jours).
- Après le SIRET : médiateur de la consommation, éco-organismes (équipements électriques et batteries) et identifiant unique, dépôt de marque INPI conseillé, nom de domaine.
- Valider les prix, le seuil de livraison et le délai de réponse de 24 h.
- Plus tard : section « Qui sommes-nous » (prénom et photo du propriétaire), à décider.

### Réponse fournisseur du 11/11
Frais de port : 23 USD pour 1 colis, 3,04 USD par lampe pour 30, 2,59 USD pour 50, 1,77 USD pour 100. Délai de 13 à 15 jours. Cartes de vœux offertes. Dropshipping à 23 USD par colis : non rentable. **Orientation : petit stock en France, expédié soi-même.** Prix unitaire et CE toujours manquants (détail dans `docs/fournisseurs.md`).

### Sourcing CJ réussi (12/11)
Lampe identique (poignée, télécommande, rechargeable) à **2,47 $ + 8,80 $ de port, livrée en 4 à 7 jours**. CJ devient le fournisseur principal pressenti. Échantillons en cours aussi chez Toonies et Temu (comparaison). Prix conseillé : 39,90 € livraison offerte, 59,90 € les 2.

### Optimisation de la maquette (12/11, skills cro, storefront-best-practices, schema, web-perf, copywriting, impeccable)
- Prix appliqués : 39,90 € la lampe, 59,90 € les 2 (−19,90 €), livraison offerte (jauge supprimée).
- Délai CJ affiché : 6 à 9 jours ouvrés, avec date estimée calculée sous le bouton d'achat ; « En stock ».
- Bouton « Acheter maintenant » (paiement express Apple Pay / Shop Pay / Google Pay, natif Shopify).
- Produit retenu (CJ) : poignée fixe sur le dessus, télécommande incluse ; dimensions à confirmer sur l'échantillon.
- Données structurées Produit (prix, stock, livraison offerte, retours 30 jours) pour Google Shopping.
- Performance : image d'accueil préchargée, images hors écran en chargement différé. Mesure mobile ralentie : affichage principal 2,1 s → 1,4 s, stabilité 0,002.
- Accessibilité : compteur du panier annoncé aux lecteurs d'écran, boutons de quantité de 44 px.

## Prochaines étapes

1. Transformer la maquette en **thème Shopify** (Online Store 2.0), boutique protégée par mot de passe pendant l'attente du SIRET.
2. Rédiger les **pages légales** : mentions légales, CGV, confidentialité, rétractation avec formulaire, livraison.
3. Remplacer toutes les infos `[à compléter]` dès les réponses du fournisseur.
4. Préparer la **campagne Google Ads** (voir `docs/google-ads.md`), sans la lancer.
5. Lancement le jour où le SIRET arrive : paiements, retrait du mot de passe, lancement des pubs.

## Idées notées pour plus tard
- Bouton de paiement express (Apple Pay, Shop Pay) dans le bloc d'achat : natif dans le thème Shopify.
- Date de livraison estimée sous le bouton d'achat (« recevez-la entre le X et le Y »), dès que les délais sont connus.
- Vidéo de 10 secondes : doigt sur la lampe, lumière qui baisse.
- Avis : offrir des lampes à 5 à 10 parents de l'entourage contre un avis honnête, en signalant que le produit a été offert.
- Tester un prix de 39,90 € une fois les premières ventes faites.
- Emails de panier abandonné de Shopify (gratuits) : à activer au lancement.

### Nom de marque remis en question (13/11)
« Nuitelle » trop proche de « Nutella ». Pistes avec un .fr libre (vérifié sur le registre AFNIC le 13/11) : petitchut.fr, lueurette.fr, petiteveille.fr, nuitambree.fr, troisheures.fr, sourdinette.fr, lueurdenuit.fr, brindelueur.fr. Aucune marque trouvée sous ces noms par recherche web (à confirmer à l'INPI). Décision en attente.
« Petit Chut » écarté (13/11) : à l'oreille, on entend « petite chute ». Nouvelles pistes avec .fr libre (AFNIC, 13/11) : chuchoti.fr, chutchut.fr, toutbas.fr, murmurette.fr, toutdoucement.fr. Aucune marque trouvée par recherche web (INPI à confirmer).
Pistes « plus sérieuses » (13/11, .fr libres sur AFNIC) : demivoix.fr, maisonchuchoti.fr, nuitfeutree.fr, maisonsourdine.fr, demiteinte.fr (sens négatif « résultat en demi-teinte »). Recommandation : Demi-Voix.
Piste « Maison » (13/11, .fr libres sur AFNIC) : maisonberceuse.fr, maisondorlote.fr, maisontendre.fr, maisonpetale.fr, maisondoudou.fr. Maison Dodo écarté (marque de literie DODO existante). Recommandation : Maison Berceuse.

### Nouveau nom : Maison Dorlote (13/11) ✅
- **Nom choisi : Maison Dorlote** (« dorloter » : tendresse ; « Maison » : sérieux). Produit : « la lampe Dorlote ». Slogan inchangé.
- **Domaines achetés chez IONOS** (jusqu'au 13/11/2027) : maisondorlote.fr (principal) et maisondorlotte.fr (faute de frappe, à rediriger vers le principal). Vérifiés sur l'AFNIC.
- **Email** : contact@maisondorlote.fr, fonctionnel (testé par le propriétaire), configuré sur iPhone en IMAP.
- **Logo validé : « la maison veilleuse »** (piste A, fenêtre allumée). Kit complet : logos clair/foncé, empilé, icône, une couleur, avatars Instagram/TikTok 1080 px, favicons (`docs/logo/`).
- **Maquette renommée** : nom, logo, favicon, email, domaine dans les données Google.
- Reste à faire : vérifier « Maison Dorlote » sur data.inpi.fr (et dépôt de marque après le SIRET), réserver @maisondorlote sur Instagram et TikTok, rediriger maisondorlotte.fr.

### Domiciliation (13/11)
Dossier envoyé à une société de domiciliation (adresse du siège). Prochaine étape : signer le contrat, puis déclarer la micro-entreprise sur formalites.entreprises.gouv.fr (ACRE) et attendre le SIRET. L'adresse de domiciliation servira dans les mentions légales (aucune adresse personnelle sur le site).
- La société de domiciliation prépare aussi le dossier d'immatriculation (micro-entreprise, RCS) : extrait K et SIRET attendus sous 5 à 9 jours (annoncé le 13/11). À vérifier sur le récapitulatif : activité commerciale de vente en ligne, nom commercial « Maison Dorlote », adresse de domiciliation, ACRE.

### Thème Shopify « Maison Dorlote » (13-14/11)
- Thème non publié « Maison Dorlote » (copie de Horizon) dans la boutique. Code source dans `theme/` (mise en page `layout/dorlote.liquid`, 16 sections `dorlote-*`, panier Ajax `snippets/dorlote-panier.liquid`, `assets/dorlote.js`). Contenu des modèles généré par `tools/build_templates.py`.
- Envoi vers Shopify : `themeFilesUpsert` avec les fichiers bruts de GitHub (dépôt public). L'outil d'aperçu Shopify ne voit pas ces fichiers (copie de travail figée) : vérifier dans l'aperçu de l'admin.
- Produit « La lampe Dorlote » créé (actif, publié sur la boutique en ligne et Shop) : 1 lampe 39,90 €, lot de 2 59,90 €, 6 photos, modèle `product.dorlote`.
- Images des sections dans Fichiers (`dorlote-*.webp`), logo lueur et favicon dans Fichiers.
- Réglages : couleurs Nuit ambrée, boutons ambre arrondis, logo, favicon, note de panier activée.
- Reste : publier le thème (accord du propriétaire), polices Google à héberger sur Shopify (RGPD), adaptateur à créer avant de le proposer dans le panier, pages légales, pages Horizon (panier, politiques) encore au style d'origine.

### Retours du propriétaire sur le thème (14/11)
- **La lampe n'a pas de commande tactile : uniquement la télécommande.** Section « gestes » supprimée, textes corrigés (teintes, avant/après, FAQ, caractéristiques, description produit, légende Instagram), photo « doigt sur la lampe » retirée du produit.
- Volets (description, caractéristiques, livraison, FAQ courte) sortis du bloc d'achat : nouvelle section « Tout savoir sur la lampe » placée après le récit, l'avant/après, les teintes et les usages (« vendre du rêve d'abord »).
- « En stock » agrandi.
- Bouton violet « Acheter avec Shop » : bouton de paiement express automatique de Shopify (Apple Pay sur iPhone, Google Pay sur Android/Chrome, Shop Pay sinon). Décision du propriétaire en attente.

### Bandeau défilant (14/11)
- Méthode : retouches d'abord sur la maquette seulement ; report dans Shopify en un lot, sur demande.
- Barre d'annonce transformée en bandeau qui défile lentement (32 s, linéaire), pause au survol, immobile si « mouvement réduit ». Ajouté : « Paiement sécurisé ». À reporter dans le thème Shopify.
- Page de paiement : c'est la page sécurisée de Shopify (non modifiable en code sur le plan Basic). Personnalisable seulement en couleurs, logo et polices (Paramètres › Paiement › Personnaliser). Le numéro de carte s'y met déjà en forme par groupes de 4 chiffres (espaces), automatiquement.
- Maquette alignée (14/11) : volets sortis du bloc d'achat vers « Tout savoir sur la lampe » (après les usages), lien discret « Voir les caractéristiques de la lampe » sous le bloc d'achat, section gestes et toute mention du tactile supprimées, photo du doigt retirée de la galerie.
