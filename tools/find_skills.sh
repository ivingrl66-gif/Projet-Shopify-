#!/usr/bin/env bash
# Recherche dans l'annuaire public des skills (skills.sh), triée par nombre d'installations.
# Usage : tools/find_skills.sh mots clés en anglais
curl -sS --get "https://skills.sh/api/search" --data-urlencode "q=$*" | python3 -c '
import sys, json
d = json.load(sys.stdin)
sk = sorted(d.get("skills", []), key=lambda s: -s.get("installs", 0))
if not sk:
    print("Aucun skill trouvé.")
for s in sk[:15]:
    print("%8d  %s@%s" % (s.get("installs", 0), s["source"], s["skillId"]))
'
