# Nuitelle : système de design

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

**L'arche lumineuse** : une arche fine (la poignée de la lampe, et la lettre « n ») avec une lueur ambrée en dessous, comme une lumière sous une porte. À côté, le mot-symbole « nuitelle » en minuscules, en Fraunces légère, vectorisé.

Fichiers dans `maquette/logo/` :
- `nuitelle-logo-clair.svg` : pour fonds sombres ;
- `nuitelle-logo-fonce.svg` : pour fonds clairs ;
- `nuitelle-icone.svg` : l'arche seule, pour favicon et avatars.

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
