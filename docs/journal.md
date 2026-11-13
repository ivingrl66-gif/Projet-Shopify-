# Journal du projet Nuitelle

Dernière mise à jour : 11 novembre 2026.

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
