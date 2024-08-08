import json
import sys

json_filename = sys.argv[1] 
contents = open(json_filename, errors='replace').read()
pjson = json.loads(contents)

with open(3, 'w') as f:
    f.write(json.dumps(
        {
            "tag": "points",
            "points": (pjson['tests']-pjson['failures'])/pjson['tests']
        }
    ))
