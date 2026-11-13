import sys; sys.path.insert(0,'/home/user/projet-shopify-/tools')
from logos_dorlote import text_paths, HOUSE, NUIT, AMBRE, CREME, MIEL
def st(c): return f'fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
def win(style,line,bg):
    if style=='1':  # fenêtre à croisillons
        return (f'<rect x="26" y="34" width="12" height="12" rx="1.2" fill="{AMBRE}"/>'
                f'<path d="M32 34 V46 M26 40 H38" stroke="{bg}" stroke-width="1.6"/>')
    if style=='2':  # fenêtre en arche
        return f'<path d="M27 47 V39.5 a5 5 0 0 1 10 0 V47 Z" fill="{AMBRE}"/>'
    if style=='3':  # arche + croisillon
        return (f'<path d="M26.5 47.5 V39.5 a5.5 5.5 0 0 1 11 0 V47.5 Z" fill="{AMBRE}"/>'
                f'<path d="M32 34 V47.5 M26.5 41.5 H37.5" stroke="{bg}" stroke-width="1.5"/>')
    if style=='4':  # fenêtre ronde (œil-de-bœuf)
        return f'<circle cx="32" cy="40" r="5.5" fill="{AMBRE}"/>'
def sym(style,line,bg):
    if style=='5':  # maison pleine, fenêtre en arche découpée
        return (f'<path d="{HOUSE}" fill="{line}" stroke="{line}" stroke-width="4" stroke-linejoin="round"/>'
                f'<path d="M27 54 V41.5 a5 5 0 0 1 10 0 V54 Z" fill="{AMBRE}"/>')
    return f'<path d="{HOUSE}" {st(line)}/>'+win(style,line,bg)
def horiz(style,dark):
    line,bg=(CREME,NUIT) if dark else (NUIT,'#F6EFE6')
    m,mw,d,dw=text_paths(line); sd,sm,x0=0.42,0.16,76; W=x0+max(dw*sd,mw*sm)+4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 64">{sym(style,line,bg)}'
      f'<path transform="translate({x0} 22) scale({sm})" fill="{line}" d="{m}"/>'
      f'<path transform="translate({x0-1} 56) scale({sd})" fill="{line}" d="{d}"/></svg>')
def icon(style):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{NUIT}"/><g transform="translate(32 34) scale(.86) translate(-32 -34)">{sym(style,CREME,NUIT)}</g></svg>'
names={'1':'1 · Fenêtre à croisillons','2':'2 · Fenêtre en arche','3':'3 · Arche à croisillons','4':'4 · Œil-de-bœuf','5':'5 · Maison pleine, porte en arche'}
rows=''
for k,t in names.items():
    ic=icon(k)
    rows+=f'<h2>{t}</h2><div class=row><div class="c d">{horiz(k,True)}</div><div class="c l">{horiz(k,False)}</div><div class="c l ic"><span class=a>{ic}</span><span class=b>{ic}</span><span class=e>{ic}</span></div></div>'
open(sys.argv[1],'w').write(f'''<!doctype html><meta charset=utf-8><style>body{{margin:0;padding:28px 36px;background:#EDE5DA;font:600 19px system-ui;color:#1E1A17}}h2{{margin:22px 0 10px;font-size:19px}}
.row{{display:grid;grid-template-columns:1.3fr 1.3fr 1fr;gap:16px}}.c{{border-radius:14px;height:170px;display:flex;align-items:center;justify-content:center;gap:18px}}
.d{{background:#1E1A17}}.l{{background:#F6EFE6}}.c>svg{{height:80px;width:auto}}.a svg{{width:96px;height:96px}}.b svg{{width:32px;height:32px}}.e svg{{width:16px;height:16px}}</style>{rows}''')
