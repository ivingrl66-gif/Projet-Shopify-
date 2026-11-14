"""Génère templates/index.json et templates/product.dorlote.json du thème Maison Dorlote
à partir du contenu de la maquette (maquette/index.html)."""
import re, json, html, sys
s = open('maquette/index.html').read()
img = lambda n: f'shopify://shop_images/{n}'

def between(a, b, start=0):
    i = s.index(a, start); j = s.index(b, i); return s[i + len(a):j]

# Volets de la fiche produit (sauf Description, qui vient de la fiche Shopify)
volets = {}
for m in re.finditer(r'<details(?: open)?><summary>(.*?)</summary><div class="volet">(.*?)</div></details>', s, re.S):
    titre, contenu = m.group(1), m.group(2).strip()
    if titre == 'Description':
        continue
    contenu = contenu.replace('href="#faq"', 'href="#faq"')
    contenu = contenu.replace('<dt>Intensité</dt><dd>Réglable en continu (appui long)</dd>', '<dt>Intensité</dt><dd>Réglable à la télécommande</dd>').replace('<dt>Commande</dt><dd>Tactile sur le dessus, et télécommande</dd>', '<dt>Commande</dt><dd>Télécommande incluse</dd>')
    volets[titre] = re.sub(r'\n\s+', '\n', contenu)

faq = []
for m in re.finditer(r'<details data-cat="(\w+)"><summary>(.*?)</summary><div class="rep">(.*?)</div></details>', s, re.S):
    cat, q, r = m.groups()
    q = html.unescape(q).replace(' ?', ' ?').replace(' ', ' ')
    r = re.sub(r'<span class="tbd">(.*?)</span>', r'(\1)', r)
    r = r.replace('&#8239;', ' ')
    r = r.replace("Oui. Maintenez le doigt sur le dessus de la lampe pour baisser l'intensité jusqu'à une simple lueur. Relâchez quand le niveau vous convient.", "Oui. Avec la télécommande, baissez l'intensité jusqu'à une simple lueur, sans vous lever.")
    faq.append((cat, q, r))

def sec(type_, settings=None, blocks=None):
    d = {"type": type_, "settings": settings or {}}
    if blocks:
        d["blocks"] = {f"b{i}": b for i, b in enumerate(blocks)}
        d["block_order"] = [f"b{i}" for i in range(len(blocks))]
    return d

def page(with_product):
    sections = {}
    order = []
    def add(key, d):
        sections[key] = d; order.append(key)
    vb = [{"type": "volet", "settings": {"titre": t, "contenu": c}} for t, c in volets.items()]
    ps = {}
    if with_product:
        ps["produit"] = "lampe-dorlote"
    add("produit", sec("dorlote-produit", ps))
    add("recit", sec("dorlote-recit", {"image": img("dorlote-recit.webp"), "image_mobile": img("dorlote-recit-mobile.webp")},
        [{"type": "point", "settings": {"texte": t}} for t in ["Sans fil, rechargeable", "3 teintes de lumière", "Horloge intégrée"]]))
    add("avant_apres", sec("dorlote-avant-apres", {"avant": img("dorlote-avant.webp"), "apres": img("dorlote-apres.webp")}, [
        {"type": "point", "settings": {"titre": "Pas de point lumineux", "texte": "L'abat-jour diffuse la lumière sur toute sa surface. Le regard ne tombe jamais sur une LED nue."}},
        {"type": "point", "settings": {"titre": "Une teinte chaude", "texte": "La lumière ambrée reste douce pour des yeux à peine ouverts, et garde la chambre dans l'ambiance de la nuit."}},
        {"type": "point", "settings": {"titre": "Juste assez", "texte": "Depuis la télécommande, baissez l'intensité jusqu'à une simple lueur : de quoi voir le biberon, pas plus."}}]))
    add("teintes", sec("dorlote-teintes", {"texte": "Avec la télécommande, passez d'une teinte à l'autre sans vous lever. Ici, choisissez-en une pour voir la différence."}, [
        {"type": "teinte", "settings": {"nom": "Chaude", "usage": "Pour la nuit, les biberons, l'endormissement", "image": img("dorlote-teinte-chaude.webp"), "couleur": "#e8a55b", "couleur_centre": "#ffd9a0"}},
        {"type": "teinte", "settings": {"nom": "Neutre", "usage": "Pour se lever, s'habiller, ranger", "image": img("dorlote-teinte-neutre.webp"), "couleur": "#f0dcbc", "couleur_centre": "#fff6e6"}},
        {"type": "teinte", "settings": {"nom": "Froide", "usage": "Pour lire ou travailler", "image": img("dorlote-teinte-froide.webp"), "couleur": "#d9e2ec", "couleur_centre": "#ffffff"}}]))
    add("usages", sec("dorlote-usages", {}, [
        {"type": "usage", "settings": {"image": img("dorlote-usage-biberon.webp"), "heure": "03:12", "titre": "Le biberon de nuit", "texte": "Assez de lumière pour préparer et donner le biberon, assez peu pour que bébé se rendorme vite."}},
        {"type": "usage", "settings": {"image": img("dorlote-usage-enfant.webp"), "heure": "21:30", "titre": "La chambre d'enfant", "texte": "Une veilleuse rassurante pour les petits qui ont peur du noir, qui ne fait pas d'ombre inquiétante."}},
        {"type": "usage", "settings": {"image": img("dorlote-usage-lecture.webp"), "heure": "23:45", "titre": "La lecture au lit", "texte": "Finir son chapitre sans réveiller la personne qui dort à côté."}}]))
    ds = {"produit": "lampe-dorlote"} if with_product else {}
    add("details", sec("dorlote-details", ds, vb))
    add("securite", sec("dorlote-securite", {}, [
        {"type": "point", "settings": {"icone": "batterie", "titre": "Aucun fil la nuit", "texte": "Elle fonctionne sur batterie : pas de câble qui traîne près du lit ou du berceau."}},
        {"type": "point", "settings": {"icone": "chaleur", "titre": "Des LED qui restent tièdes", "texte": "Des LED basse consommation, qui ne chauffent pas comme une ampoule classique (à vérifier sur l'échantillon)."}},
        {"type": "point", "settings": {"icone": "diffusion", "titre": "Aucune LED visible", "texte": "La lumière passe à travers tout l'abat-jour : rien ne fixe le regard de bébé."}},
        {"type": "point", "settings": {"icone": "norme", "titre": "Normes européennes", "texte": "Marquage CE et conformité RoHS, documents disponibles sur demande (à confirmer)."}}]))
    rows = [("Lumière chaude qui n'éblouit pas", "oui", "oui", "non"), ("Intensité réglable, de la lueur à la lecture", "oui", "non", "Parfois"),
            ("3 teintes de lumière", "oui", "non", "non"), ("Sans fil, se transporte d'une pièce à l'autre", "oui", "Rarement", "non"),
            ("L'heure visible sans allumer son téléphone", "oui", "non", "non"), ("Satisfait ou remboursé 30 jours", "oui", "Selon le vendeur", "—")]
    add("comparatif", sec("dorlote-comparatif", {}, [{"type": "ligne", "settings": {"critere": c, "v1": a, "v2": b, "v3": d}} for c, a, b, d in rows]))
    add("avis", sec("dorlote-avis"))
    add("faq", sec("dorlote-faq", {}, [{"type": "question", "settings": {"categorie": c, "question": q, "reponse": r}} for c, q, r in faq]))
    add("garanties", sec("dorlote-garanties", {}, [
        {"type": "garantie", "settings": {"titre": "Livraison offerte", "texte": "En 6 à 9 jours ouvrés, avec un numéro de suivi par email."}},
        {"type": "garantie", "settings": {"titre": "Satisfait ou remboursé", "texte": "30 jours pour l'essayer chez vous. Si elle ne vous convient pas, nous vous remboursons."}},
        {"type": "garantie", "settings": {"titre": "Garantie 2 ans", "texte": "Remplacement ou remboursement en cas de défaut."}},
        {"type": "garantie", "settings": {"titre": "Une réponse sous 24 h", "texte": "Écrivez-nous : une personne vous répond, les jours ouvrés."}}]))
    add("final", sec("dorlote-final", {"image": img("dorlote-teinte-chaude.webp")}))
    add("contact", sec("dorlote-contact"))
    return {"layout": "dorlote", "sections": sections, "order": order}

out = sys.argv[1]
json.dump(page(True), open(f'{out}/templates/index.json', 'w'), ensure_ascii=False, indent=2)
json.dump(page(False), open(f'{out}/templates/product.dorlote.json', 'w'), ensure_ascii=False, indent=2)
print(len(volets), 'volets', len(faq), 'questions')
