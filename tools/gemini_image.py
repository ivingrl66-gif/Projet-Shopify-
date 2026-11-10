import sys, json, base64, urllib.request, os
model, ref, out, prompt = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
parts=[{"text":prompt}]
for r in ref.split(','):
    if r: parts.append({"inline_data":{"mime_type":"image/png","data":base64.b64encode(open(r,'rb').read()).decode()}})
body={"contents":[{"parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5"}}}
req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
try:
    d=json.load(urllib.request.urlopen(req,timeout=300))
except urllib.error.HTTPError as e:
    print("HTTP",e.code,e.read().decode()[:600]); sys.exit(1)
n=0
for c in d.get("candidates",[]):
    for p in c.get("content",{}).get("parts",[]):
        if "inlineData" in p:
            open(out,'wb').write(base64.b64decode(p["inlineData"]["data"])); n+=1
        elif "text" in p: print("TEXT:",p["text"][:300])
print("images:",n,"usage:",d.get("usageMetadata"))
