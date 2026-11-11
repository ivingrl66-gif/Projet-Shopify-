import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
def wordmark(font, text, track=0.0, size=100):
    f=TTFont(font); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    s=size/upm; x=0; paths=[]
    for ch in text:
        gn=cmap[ord(ch)]; g=gs[gn]
        pen=SVGPathPen(gs); tp=TransformPen(pen,(s,0,0,-s,x,0)); g.draw(tp)
        paths.append(pen.getCommands()); x+=g.width*s+track*size
    asc=f['hhea'].ascent*s
    return ' '.join(paths), x-track*size, asc
if __name__=='__main__':
    d,w,a=wordmark(sys.argv[1],sys.argv[2],float(sys.argv[3]))
    print(w,a); open(sys.argv[4],'w').write(d)
