import json

# Opening JSON file
fi = open('diff.json', )
fo = open('1.json', )

# returns JSON object as
# a dictionary
diff = json.load(fi)
outputTemplate = json.load(fo)

fi.close()
fo.close()

for item in diff['_content'].items():
    currPacketIndex = int(item[0])
    for field in item[1]:
        outputTemplate[currPacketIndex][field] = "null"

with open("template.json", "w") as outfile:
    json.dump(outputTemplate, outfile)
