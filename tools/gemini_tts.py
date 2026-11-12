import sys, json, base64, urllib.request
model, voice, out, text = sys.argv[1:5]
body={"contents":[{"parts":[{"text":text}]}],"generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":voice}}}}}
req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
try: d=json.load(urllib.request.urlopen(req,timeout=180))
except urllib.error.HTTPError as e: print("HTTP",e.code,e.read().decode()[:400]); sys.exit(1)
p=d["candidates"][0]["content"]["parts"][0]["inlineData"]; print(p["mimeType"]); open(out,"wb").write(base64.b64decode(p["data"]))
