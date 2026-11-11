import sys, json, base64, urllib.request, mimetypes
model, refs, out, aspect, prompt = sys.argv[1:6]
parts=[{"text":prompt}]
for r in [x for x in refs.split(',') if x]:
    mt=mimetypes.guess_type(r)[0] or "image/png"
    parts.append({"inline_data":{"mime_type":mt,"data":base64.b64encode(open(r,'rb').read()).decode()}})
body={"contents":[{"parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":aspect}}}
req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
for attempt in range(2):
    try:
        d=json.load(urllib.request.urlopen(req,timeout=400)); break
    except urllib.error.HTTPError as e:
        print(out,"HTTP",e.code,e.read().decode()[:300]); 
        if attempt: sys.exit(1)
n=0
for c in d.get("candidates",[]):
    for p in c.get("content",{}).get("parts",[]):
        if "inlineData" in p:
            open(out,'wb').write(base64.b64decode(p["inlineData"]["data"])); n+=1
print(out,"images:",n)
