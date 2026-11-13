"""Logo Maison Dorlote : « la maison veilleuse ».
Usage : python3 tools/logos_dorlote.py <dossier_sortie>
Produit 3 variantes de symbole (A, B, C), chacune en icône, en logo
horizontal et en logo empilé, pour fonds sombres et clairs.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wordmark import wordmark

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
NUIT, BRUN, AMBRE, MIEL, CREME = '#1E1A17', '#2B2420', '#E8A55B', '#F4D6A8', '#F6EFE6'

def glow(id):
    return (f'<radialGradient id="{id}" cx="50%" cy="50%" r="50%">'
            f'<stop offset="0" stop-color="#FFF1DA"/><stop offset=".3" stop-color="{MIEL}"/>'
            f'<stop offset=".6" stop-color="{AMBRE}" stop-opacity=".7"/>'
            f'<stop offset="1" stop-color="{AMBRE}" stop-opacity="0"/></radialGradient>')

HOUSE = 'M14 54 V31 L32 14.5 L50 31 V54 Z'

def sym(v, line, id, halo=True, win=AMBRE):
    """Symbole dans un carré de 64 unités. line = couleur du trait."""
    st = f'fill="none" stroke="{line}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
    h = lambda cx, cy, r: f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{id})"/>' if halo else ''
    if v == 'A':   # fenêtre carrée allumée
        return (h(32, 40, 15) + f'<path d="{HOUSE}" {st}/>'
                f'<rect x="27" y="35" width="10" height="10" rx="1.6" fill="{win}"/>')
    if v == 'B':   # porte en arche, lumière qui filtre
        return (h(32, 50, 15) + f'<path d="{HOUSE}" {st}/>'
                f'<path d="M26.5 54 V45 a5.5 5.5 0 0 1 11 0 V54 Z" fill="{AMBRE}"/>')
    if v == 'C':   # toit seul, une lueur ronde dessous
        return (h(32, 41, 17) + f'<path d="M12 34 L32 15.5 L52 34" {st}/>'
                f'<circle cx="32" cy="41" r="6.5" fill="{AMBRE}"/>')

def defs(id):
    return f'<defs>{glow(id)}</defs>'

def text_paths(col):
    m, mw, _ = wordmark(os.path.join(FONTS, 'fraunces-400.ttf'), 'MAISON', 0.32, 100)
    d, dw, _ = wordmark(os.path.join(FONTS, 'fraunces-400.ttf'), 'Dorlote', 0.0, 100)
    return m, mw, d, dw

def icon(v, dark=True):
    bg, line = (NUIT, CREME) if dark else (CREME, NUIT)
    id = f'g{v}{"d" if dark else "l"}i'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Maison Dorlote">'
            f'{defs(id)}<rect width="64" height="64" rx="14" fill="{bg}"/>{sym(v, line, id)}</svg>')

def horizontal(v, dark=True):
    line = CREME if dark else NUIT
    id = f'g{v}{"d" if dark else "l"}h'
    m, mw, d, dw = text_paths(line)
    # symbole 64 de haut ; « Dorlote » à 0,46, « MAISON » à 0,17
    sd, sm = 0.42, 0.16
    x0 = 76
    W = x0 + max(dw * sd, mw * sm) + 4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 64" role="img" aria-label="Maison Dorlote">'
            f'{defs(id)}{sym(v, line, id)}'
            f'<path transform="translate({x0} 22) scale({sm})" fill="{line}" d="{m}"/>'
            f'<path transform="translate({x0 - 1} 56) scale({sd})" fill="{line}" d="{d}"/></svg>')

def stacked(v, dark=True):
    line = CREME if dark else NUIT
    id = f'g{v}{"d" if dark else "l"}s'
    m, mw, d, dw = text_paths(line)
    sd, sm = 0.5, 0.19
    W = max(dw * sd, mw * sm, 64) + 8
    cx = W / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 150" role="img" aria-label="Maison Dorlote">'
            f'{defs(id)}<g transform="translate({cx - 32} 0)">{sym(v, line, id)}</g>'
            f'<path transform="translate({cx - mw * sm / 2:.1f} 88) scale({sm})" fill="{line}" d="{m}"/>'
            f'<path transform="translate({cx - dw * sd / 2:.1f} 140) scale({sd})" fill="{line}" d="{d}"/></svg>')

def mono(kind, col):
    """Version une couleur (impression, tampon, gravure) : sans halo."""
    m, mw, d, dw = text_paths(col)
    s_ = sym('A', col, 'x', halo=False, win=col)
    if kind == 'logo':
        sd, sm, x0 = 0.42, 0.16, 76
        W = x0 + max(dw * sd, mw * sm) + 4
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 64" role="img" aria-label="Maison Dorlote">{s_}'
                f'<path transform="translate({x0} 22) scale({sm})" fill="{col}" d="{m}"/>'
                f'<path transform="translate({x0 - 1} 56) scale({sd})" fill="{col}" d="{d}"/></svg>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Maison Dorlote">{s_}</svg>'

def avatar(with_name=False):
    """Carré 1080 pour Instagram / TikTok : contenu dans le cercle central."""
    id = 'gav'
    if not with_name:
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{defs(id)}'
                f'<rect width="64" height="64" fill="{NUIT}"/>'
                f'<g transform="translate(32 33) scale(.62) translate(-32 -34)">{sym("A", CREME, id)}</g></svg>')
    m, mw, d, dw = text_paths(CREME)
    sd, sm = 0.5, 0.19
    W = 300; cx = W / 2; k = W / 300
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}">{defs(id)}'
            f'<rect width="{W}" height="{W}" fill="{NUIT}"/>'
            f'<g transform="translate({cx - 32} 62)">{sym("A", CREME, id)}</g>'
            f'<path transform="translate({cx - mw * sm / 2:.1f} 158) scale({sm})" fill="{CREME}" d="{m}"/>'
            f'<path transform="translate({cx - dw * sd / 2:.1f} 210) scale({sd})" fill="{CREME}" d="{d}"/></svg>')

if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    if len(sys.argv) > 2 and sys.argv[2] == 'final':
        files = {
            'maison-dorlote-logo-clair.svg': horizontal('A', True),    # pour fonds sombres
            'maison-dorlote-logo-fonce.svg': horizontal('A', False),   # pour fonds clairs
            'maison-dorlote-empile-clair.svg': stacked('A', True),
            'maison-dorlote-empile-fonce.svg': stacked('A', False),
            'maison-dorlote-icone.svg': icon('A', True),
            'maison-dorlote-mono-noir.svg': mono('logo', NUIT),
            'maison-dorlote-mono-blanc.svg': mono('logo', '#FFFFFF'),
            'maison-dorlote-icone-mono.svg': mono('icone', NUIT),
            'maison-dorlote-avatar.svg': avatar(False),
            'maison-dorlote-avatar-nom.svg': avatar(True),
        }
        for n, c in files.items():
            open(os.path.join(out, n), 'w').write(c)
        print('ok final'); sys.exit()
    for v in 'ABC':
        for dark in (True, False):
            t = 'clair' if dark else 'fonce'   # clair = pour fonds sombres
            for name, fn in (('icone', icon), ('logo', horizontal), ('empile', stacked)):
                if name == 'icone' and not dark:
                    t2 = 'fond-clair'
                elif name == 'icone':
                    t2 = 'fond-sombre'
                else:
                    t2 = t
                open(os.path.join(out, f'dorlote-{v}-{name}-{t2}.svg'), 'w').write(fn(v, dark))
    print('ok')
