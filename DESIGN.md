# Maison Dorlote : système de design

> Référence visuelle de tout le site. Toute nouvelle page ou section doit s'y conformer.

## Concept

**« Nuit ambrée ».** La marque vit dans la lumière de la lampe à 3000 K dans une chambre sombre. Le site montre la promesse au lieu de la décrire : une lumière douce qui n'éblouit pas.

Signature graphique : **la lueur**, un halo doux sans contour net. Pas de lune, pas d'étoile, pas de nuage, pas de clipart bébé, pas de néon tech.

## Couleurs

| Token | Hex | Usage |
|---|---|---|
| `--nuit` | `#1E1A17` | Fonds sombres, texte principal sur clair |
| `--nuit-surface` | `#2B2420` | Cartes et surfaces sur fond sombre |
| `--ambre` | `#E8A55B` | Boutons d'achat, accents, lueurs |
| `--miel` | `#F4D6A8` | Reflets, survols, halos |
| `--lin` | `#F6EFE6` | Fonds clairs |
| `--gris-chaud` | `#8C8178` | Texte secondaire |

Règles :
- Jamais de noir pur, jamais de blanc pur, jamais de bleu ou de violet.
- L'ambre est réservé à l'action (achat) et à la lumière. Il ne sert pas à décorer.
- Contraste du texte d'au moins 4,5:1.

## Typographie

- **Titres : Fraunces**, axe SOFT élevé, graisse 400 à 600. Doux et éditorial.
- **Texte : Figtree**, 400 et 600. Taille minimale de 16 px sur mobile.
- Interdites : Inter, Poppins, Montserrat.

## Logo

**La maison veilleuse** : une maison au trait arrondi, la nuit, avec une seule fenêtre allumée en ambre (#E8A55B) et un halo doux. Elle dit « Maison » et « veilleuse » d'un coup d'œil. À côté, le mot-symbole « MAISON » (petites capitales espacées) au-dessus de « Dorlote », en Fraunces 400, vectorisé. Le sérieux vient de la typographie, la tendresse de la lueur.

Fichiers dans `maquette/logo/` :
- `maison-dorlote-logo-clair.svg` : logo horizontal pour fonds sombres (en-tête et pied du site) ;
- `maison-dorlote-logo-fonce.svg` : pour fonds clairs (page de paiement Shopify, factures) ;
- `maison-dorlote-empile-clair.svg` / `-fonce.svg` : version empilée (emballage, cartes, réseaux) ;
- `maison-dorlote-icone.svg` : la maison seule sur fond nuit (favicon) ;
- `maison-dorlote-mono-noir.svg` / `-mono-blanc.svg` / `-icone-mono.svg` : une couleur, sans halo (impression, tampon) ;
- `maison-dorlote-avatar.svg` / `-avatar-nom.svg` : avatars Instagram et TikTok.

Exports PNG dans `docs/logo/export/`. Règles : ne pas déformer, ne pas changer les couleurs, ne pas ajouter d'ombre ; laisser autour du logo un espace libre égal à la hauteur de la maison ; taille minimale du logo horizontal : 100 px de large.

Pas de surtitre (petit libellé en capitales) au-dessus des titres : le titre parle seul.

## Photographie

- Toujours de nuit, en lumière chaude, avec un étalonnage commun (tons ambre et brun, noirs doux).
- De vrais moments de parents : mains, biberon, berceau, linge. Le produit est dans la scène.
- Le fond blanc est réservé aux visuels techniques.
- Aucun texte incrusté, aucune image fournisseur brute.

## Ton

- Vouvoiement chaleureux, phrases courtes, rassurantes.
- On parle de confort, jamais de santé : pas de « protège les yeux » ni d'« améliore le sommeil ».
- Aucune exagération ni urgence artificielle.

## Mouvement

- La lampe « s'allume » au défilement, un halo respire lentement, l'avant-après se pilote au curseur.
- Durées de 200 à 600 ms, courbes douces.
- Tout est coupé si le système demande moins d'animations (`prefers-reduced-motion`).
- Aucune animation ne doit bloquer ni retarder l'achat.
