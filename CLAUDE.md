# Projet Nuitelle : instructions pour Claude

Boutique Shopify mono-produit **Nuitelle** : une lampe de chevet / veilleuse LED rechargeable (modèle fournisseur TL-0191), pour les **jeunes parents** (biberon de nuit, chambre de bébé), aussi vendue comme **cadeau de naissance**.

Le propriétaire est francophone, débutant en e-commerce, et attend un avis d'expert critique. **Toujours répondre en français**, avec des phrases simples.

## À lire au début de chaque session

1. `docs/journal.md` : où en est le projet, décisions prises, points en attente, prochaines étapes. **Commencer par là.**
2. `DESIGN.md` : identité visuelle (« Nuit ambrée »), couleurs, polices, logo, ton. Toute page doit s'y conformer.
3. `docs/site.md` : structure du site et parcours d'achat.
4. `docs/produit-tl0191.md` : fiche du produit retenu (confirmé / à vérifier / interdit).
5. `docs/fournisseurs.md` : fournisseurs contactés et statut.
6. `docs/google-ads.md` : plan publicitaire.

`docs/produit.md` décrit l'ancien modèle abandonné (GGBEE), mais ses sections 6 à 8 (commerce, marque, légal) restent valables.

## Règle n° 1 : les skills d'abord (exigée par le propriétaire)

Pour **tout travail concret** (créer ou modifier le site, la maquette, le thème, les visuels, les textes, les pages légales, les campagnes, la configuration Shopify…), **avant de proposer quoi que ce soit** :

1. **Skills installés** : vérifier ceux du projet (`.claude/skills/`) et ceux de la session. Les utiliser s'ils couvrent la demande.
2. **Annuaire public** : chercher des skills complémentaires avec `tools/find_skills.sh <mots-clés en anglais>` (annuaire skills.sh, trié par installations ; voir aussi le skill `find-skills`). Faire 2 ou 3 recherches avec des mots-clés différents.
3. **Choisir avec soin** :
   - préférer les sources officielles (`shopify/…`, `anthropics/…`, `vercel-labs/…`) et plus de 1 000 installations ;
   - se méfier en dessous de 100 installations ;
   - **lire entièrement le SKILL.md** (et tout script fourni) avant d'installer ;
   - installer dans `.claude/skills/<nom>/` du dépôt, puis commit et push.
4. **Utiliser le ou les skills**, puis ajouter sa propre expertise par-dessus.
5. **Si aucun skill ne convient**, le dire clairement au propriétaire (« aucun skill adapté trouvé »), puis travailler avec ses propres connaissances.
6. **Dans chaque réponse de travail**, indiquer en une ligne quels skills ont été utilisés ou trouvés.

**Exception, voulue par le propriétaire** : pour une simple question ou une discussion (conseil rapide, explication, avis, analyse d'un devis ou d'un message fournisseur), répondre directement, sans chercher de skill.

**Superpowers** (obra/superpowers, installé le 12/11) : utiliser surtout `brainstorming` (avant une nouvelle fonctionnalité), `writing-plans`, `verification-before-completion` et `systematic-debugging`. Adaptations pour ce projet : on reste sur la branche `main` (pas de worktrees ni de branches, le propriétaire suit sur GitHub) ; les sous-agents seulement pour un gros chantier ; le TDD là où c'est pertinent (scripts, logique du panier), pas pour du texte ou du design ; poser les questions de cadrage en français, simplement, sans noyer le propriétaire.

**Animation et 3D** (installés le 12/11) :
- **Motion design web** : skills d'Emil Kowalski (`animate`, `review-animations`, `improve-animations`, `choreograph`, `animation-performance`, `apple-design`…) pour décider quoi animer et comment ;
- **GSAP officiel** (`gsap-core`, `gsap-scrolltrigger`, `gsap-timeline`…) pour les animations au défilement ;
- **Three.js** (`threejs-*`, de cloudai-x) pour une éventuelle lampe 3D interactive.

Règle du projet : les animations restent discrètes, n'alourdissent jamais le mobile et respectent `prefers-reduced-motion` (voir `DESIGN.md`). Une scène 3D doit prouver qu'elle aide à vendre avant d'être ajoutée (poids, vitesse, fidélité au produit).

Attention aux skills juridiques : la plupart visent le droit américain. Pour les pages légales françaises, ils servent de base de structure, pas de référence juridique.

## Règles du projet

- **Honnêteté commerciale** : jamais de faux avis, faux prix barrés, faux comptes à rebours ni fausses alertes de stock (illégal en France, et motif de suspension Google Merchant Center).
- **Aucune allégation santé** (« protège les yeux », « améliore le sommeil », « sans lumière bleue ») : parler de confort.
- **Ne jamais afficher une caractéristique non confirmée** par le fournisseur ou l'échantillon. Sur la maquette, les infos provisoires sont en classe `.tbd` (encadré pointillé).
- **Skill Impeccable** (`.claude/skills/impeccable`) : l'utiliser pour tout travail de design ou de texte (règles : pas de surtitre au-dessus des titres, typographie française avec espaces insécables, contraste, états des contrôles). Lancer son détecteur après chaque modification de page : `.claude/skills/impeccable/scripts/impeccable detect --json maquette/index.html`.
- **Ne pas surcharger** l'accueil : le client doit pouvoir acheter en quelques secondes.
- Commit et push sur `main` après chaque étape significative (le propriétaire suit sur GitHub).

## Maquette

- Fichier : `maquette/index.html`, images dans `maquette/img/`, logos dans `maquette/logo/`.
- Publiée comme Artifact privé : https://claude.ai/artifact/RNf3NJzUxZRy8kNaE4SvTY (pour la mettre à jour depuis une nouvelle session : la lire avec `action: "read"` puis publier avec `url`).
- Vérification visuelle : Playwright (Chromium préinstallé), à 1440 px et 390 px de large. Envelopper le fichier dans un squelette HTML (`<!doctype html>…`) pour le prévisualiser en local.

## Génération d'images (Gemini)

- La clé API Gemini est stockée dans les **secrets réseau** de l'environnement (hôte `generativelanguage.googleapis.com`, en-tête `x-goog-api-key`) : le proxy l'ajoute automatiquement, rien à configurer.
- Outil : `python3 -I tools/gemini_image.py <modèle> <images_ref_séparées_par_virgule> <sortie.png> <format ex 4:5> "<prompt>"`.
- Modèle utilisé : `gemini-3-pro-image`. Toujours fournir les photos réelles du produit en référence (`docs/produit/tl0191/visuels/`) pour que la lampe reste fidèle.
- Style imposé : nuit, lumière chaude 3000 K, ombres brun chaud, aucun texte incrusté.
- L'IA écrit mal les chiffres de l'horloge : vérifier par zoom, et si besoin tracer l'heure à la main (méthode utilisée pour `hero-desktop`).
- Originaux archivés dans `docs/produit/tl0191/generees/`.

## Logo

- « L'arche lumineuse » : arche (poignée de la lampe / lettre n) + lueur ambrée, et mot-symbole « nuitelle » en Fraunces vectorisé.
- Régénérer : `python3 -I tools/logos.py tools tools/fonts/fraunces-400.ttf <dossier_sortie>` (variante B = l'arche).

## Boutique Shopify

- Boutique connectée via le connecteur Shopify : « Ma boutique 2 » (hvxyad-am.myshopify.com), plan Basic, EUR, France.
- Prochaine grande étape technique : transformer la maquette en **thème Shopify Online Store 2.0** (Liquid, sections éditables), relié à ce dépôt via l'intégration GitHub de Shopify.
