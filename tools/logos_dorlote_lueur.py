import sys; sys.path.insert(0,'/home/user/projet-shopify-/tools')
from logos_dorlote import text_paths, HOUSE, NUIT, AMBRE, CREME, MIEL
INNER='M16 54 V32 L32 17.4 L48 32 V54 Z'
WIN='M26 48 V39 a6 6 0 0 1 12 0 V48 Z'
def sym(line,id):
    return (f'<defs><clipPath id="c{id}"><path d="{INNER}"/></clipPath>'
            f'<radialGradient id="r{id}" cx="32" cy="43" r="19" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{AMBRE}" stop-opacity=".55"/><stop offset=".55" stop-color="{AMBRE}" stop-opacity=".18"/>'
            f'<stop offset="1" stop-color="{AMBRE}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect x="0" y="0" width="64" height="64" fill="url(#r{id})" clip-path="url(#c{id})"/>'
            f'<path d="{HOUSE}" fill="none" stroke="{line}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="{WIN}" fill="{MIEL}"/><path d="{WIN}" fill="{AMBRE}" transform="translate(32 48) scale(.78) translate(-32 -48)" opacity=".0"/>')
def horiz(line,id):
    m,mw,d,dw=text_paths(line); sd,sm,x0=0.42,0.16,76; W=x0+max(dw*sd,mw*sm)+4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 64">{sym(line,id)}'
      f'<path transform="translate({x0} 22) scale({sm})" fill="{line}" d="{m}"/>'
      f'<path transform="translate({x0-1} 56) scale({sd})" fill="{line}" d="{d}"/></svg>')
def icon(line,id):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="8 8 48 50">{sym(line,id)}</svg>'
for name,svg in [('logo',horiz(CREME,'a')),('symbole',icon(CREME,'b'))]:
    open(f'{sys.argv[1]}/{name}.svg','w').write(svg)
    open(f'{sys.argv[1]}/{name}.html','w').write(f'<!doctype html><meta charset=utf-8><style>html,body{{margin:0;height:100%;background:#1E1A17}}body{{display:flex;align-items:center;justify-content:center}}svg{{width:{"78vw" if name=="logo" else "auto"};height:{"auto" if name=="logo" else "70vh"}}}</style>{svg}')
