# Projet Maison Dorlote : instructions pour Claude

Boutique Shopify mono-produit **Maison Dorlote** (produit : « la lampe Dorlote » ; nommée Nuitelle jusqu'au 13/11, abandonné car trop proche de Nutella) : une lampe de chevet / veilleuse LED rechargeable (modèle fournisseur TL-0191), pour les **jeunes parents** (biberon de nuit, chambre de bébé), aussi vendue comme **cadeau de naissance**.

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

**Shopify** (installés le 12/11) : le skill officiel `shopify` (Shopify AI Toolkit : Liquid, Admin API, CLI, données personnalisées…, avec recherche dans la doc et validation du code) et les standards Liquid de `benjaminsehl/liquid-skills` (`shopify-liquid-themes`, `liquid-theme-standards`, `liquid-theme-a11y`). À utiliser pour tout le thème. L'accès à la boutique elle-même passe par le **connecteur Shopify** (outils `mcp__Shopify__*`), déjà relié à « Ma boutique 2 ». ⚠️ Les scripts du skill `shopify` envoient par défaut des statistiques d'usage à Shopify (dont un extrait de la demande) : demander l'avis du propriétaire avant de les lancer.

**Animation et 3D** (installés le 12/11) :
- **Motion design web** : skills d'Emil Kowalski (`animate`, `review-animations`, `improve-animations`, `choreograph`, `animation-performance`, `apple-design`…) pour décider quoi animer et comment ;
- **GSAP officiel** (`gsap-core`, `gsap-scrolltrigger`, `gsap-timeline`…) pour les animations au défilement ;
- **Three.js** (`threejs-*`, de cloudai-x) pour une éventuelle lampe 3D interactive.

Règle du projet : les animations restent discrètes, n'alourdissent jamais le mobile et respectent `prefers-reduced-motion` (voir `DESIGN.md`). Une scène 3D doit prouver qu'elle aide à vendre avant d'être ajoutée (poids, vitesse, fidélité au produit).

**Optimisation et marketing** (installés le 12/11) :
- **Conversion et textes** (Corey Haines, marketingskills) : `cro`, `copywriting`, `copy-editing`, `marketing-psychology`, `ab-testing`, `offers`, `pricing` ;
- **Mesure et publicité** : `analytics`, `conversion-tracking`, `ads`, `ad-creative`, `emails`, `referrals`, `influencer-marketing` ;
- **Vitesse** : `web-perf` (Cloudflare), `debug-optimize-lcp` (Chrome DevTools), `performance-optimization` (Addy Osmani) ;
- **Référencement** : `schema`, `seo-audit`, `seo-ecommerce`, `storefront-best-practices` (Medusa).

Ces skills visent surtout le marché américain : adapter au droit français (pas de faux prix barrés ni de fausse urgence, RGPD, consentement cookies) et au ton Maison Dorlote.

Attention aux skills juridiques : la plupart visent le droit américain. Pour les pages légales françaises, ils servent de base de structure, pas de référence juridique.

**Disponibilité des skills** : ils sont dans `.claude/skills/` du dépôt (toute session sur ce projet les a). Pour les autres sessions cloud, le script de démarrage de l'environnement « Default » clone ce dépôt et copie les skills dans `~/.claude/skills/`. Après l'ajout d'un skill, faire commit et push pour qu'il se propage.

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
- **Rendu naturel, pas « IA »** (retour du propriétaire) : style photo prise sur le vif au smartphone en mode nuit, vraie maison un peu en désordre (lange, babyphone, verre d'eau, linge), peau réelle et cernes, cadrage imparfait, grain. Jamais de rendu « éditorial », « premium » ou « cinéma ». Montrer le problème (la nuit, la fatigue, le plafonnier qui éblouit).
- **Image d'accueil** (validée en sombre, le 12/11) : ambiance « dramatique et feutrée » de la toute première version, une seule lueur ambrée, environ deux tiers de l'image dans l'ombre, sujet à droite et grand mur sombre à gauche pour le titre. Palette ancrée sur #1E1A17, #E8A55B, #F6EFE6.
- L'IA écrit mal les chiffres de l'horloge : vérifier par zoom, et si besoin tracer l'heure à la main (méthode utilisée pour `hero-desktop`).
- Originaux archivés dans `docs/produit/tl0191/generees/`.

## Logo

- « La maison veilleuse » (validé le 13/11) : une maison au trait, une seule fenêtre allumée en ambre avec un halo, et le mot-symbole « MAISON / Dorlote » en Fraunces vectorisé.
- Fichiers dans `maquette/logo/` (SVG), exports PNG (avatars 1080, favicons, logos 1200) dans `docs/logo/export/`, aperçu dans `docs/logo/maison-dorlote-kit.png`.
- Régénérer : `python3 tools/logos_dorlote.py maquette/logo final`.

## Domaine et email

- Domaines achetés chez IONOS le 13/11 (jusqu'au 13/11/2027) : **maisondorlote.fr** (principal) et maisondorlotte.fr (faute de frappe, à rediriger).
- Email : **contact@maisondorlote.fr** (IONOS, IMAP `imap.ionos.fr` / SMTP `smtp.ionos.fr`), fonctionnel.

## Boutique Shopify

- Boutique connectée via le connecteur Shopify : « Ma boutique 2 » (hvxyad-am.myshopify.com), plan Basic, EUR, France.
- Prochaine grande étape technique : transformer la maquette en **thème Shopify Online Store 2.0** (Liquid, sections éditables), relié à ce dépôt via l'intégration GitHub de Shopify.
