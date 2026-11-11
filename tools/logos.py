import sys; sys.path.insert(0, sys.argv[1])
from wordmark import wordmark
from fontTools.ttLib import TTFont
F=sys.argv[2]; OUT=sys.argv[3]
LIN='#F6EFE6'; NUIT='#1E1A17'; AMBRE='#E8A55B'; MIEL='#F4D6A8'
def halo(cx,cy,r,id):
    return f'''<defs><radialGradient id="{id}" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFF1DA"/><stop offset=".28" stop-color="{MIEL}"/><stop offset=".55" stop-color="{AMBRE}" stop-opacity=".75"/><stop offset="1" stop-color="{AMBRE}" stop-opacity="0"/></radialGradient></defs><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{id})"/>'''
# --- symbole B : l'arche (poignée / lettre n) et sa lueur
def sym_arche(col, id):
    return halo(32,43,17,id)+f'<path d="M16 54 V33 a16 16 0 0 1 32 0 V54" fill="none" stroke="{col}" stroke-width="4.6" stroke-linecap="round"/>'
# --- symbole A : la lanterne (silhouette de la lampe)
def sym_lanterne(col,id):
    return f'''<defs><radialGradient id="{id}g" cx="50%" cy="45%" r="65%"><stop offset="0" stop-color="#FFF1DA"/><stop offset=".6" stop-color="{MIEL}"/><stop offset="1" stop-color="{AMBRE}"/></radialGradient></defs>
<path d="M22 22 V16 a10 10 0 0 1 20 0 V22" fill="none" stroke="{col}" stroke-width="3.6" stroke-linecap="round"/>
<rect x="12" y="22" width="40" height="34" rx="10" fill="url(#{id}g)"/><rect x="12" y="47" width="40" height="9" rx="4.5" fill="{col}" opacity=".9"/>'''
# --- symbole C : halo dans un carré doux
def sym_halo(col,id,bg):
    return f'<rect x="6" y="6" width="52" height="52" rx="16" fill="{bg}"/>'+halo(32,32,20,id)
def wm(text,weight,track,col):
    d,w,a=wordmark(F.replace('400',str(weight)),text,track); return f'<path d="{d}" fill="{col}"/>',w
def lockup(sym_svg, text, weight, track, col, extra='', scale=1):
    p,w=wm(text,weight,track,col)
    # symbole 64 de haut, mot-symbole hauteur x ~48 -> échelle .9, aligné sur la ligne de base y=56
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 6 {int(69+w*0.62)+6} 52" height="{int(64*scale)}"><g>{sym_svg}</g><g transform="translate(69 54) scale(.62)">{p}{extra}</g></svg>'
def idot(weight,track,id):
    f=TTFont(F.replace('400',str(weight))); cm=f.getBestCmap(); gs=f.getGlyphSet(); s=100/f['head'].unitsPerEm
    x=sum(gs[cm[ord(c)]].width*s+track*100 for c in 'nu'); wi=gs[cm[0x131]].width*s
    return halo(x+wi/2,-66,13,id)
variants={
 'A-lanterne': lambda col,bg,i: lockup(sym_lanterne(col,'a'+i),'nuitelle',400,.02,col),
 'B-arche': lambda col,bg,i: lockup(sym_arche(col,'b'+i),'nuitelle',300,.05,col),
 'C-halo': lambda col,bg,i: lockup(sym_halo(col,'c'+i,'#2B2420' if bg==NUIT else '#ECE2D5'),'nuıtelle',400,.02,col,idot(400,.02,'ci'+i)),
}
icons={'A-lanterne':lambda i:f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{NUIT}"/>{sym_lanterne(LIN,"ia"+i)}</svg>',
 'B-arche':lambda i:f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{NUIT}"/>{sym_arche(LIN,"ib"+i)}</svg>',
 'C-halo':lambda i:f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{NUIT}"/>{halo(32,32,22,"ic"+i)}</svg>'}
for k,fn in variants.items():
    open(f'{OUT}/{k}-dark.svg','w').write(fn(LIN,NUIT,'d'))
    open(f'{OUT}/{k}-light.svg','w').write(fn(NUIT,LIN,'l'))
    open(f'{OUT}/{k}-icon.svg','w').write(icons[k]('x'))
print('ok')
