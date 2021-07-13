import json, os, sys
from jsoncomparison import Compare
from progress_bars import ProgressBar

fa = open('template.json', )
actual = json.load(fa)
fa.close()

numDiffsDone = 0
numDiffsTodo = len(os.listdir("./json"))

with ProgressBar(sys.stdout) as progress:
    for filename in os.listdir("./json"):
        progress.update(numDiffsDone / numDiffsTodo)
        # Opening JSON file
        fe = open("./json/" + filename, )

        # returns JSON object as
        # a dictionary
        expected = json.load(fe)

        # Closing file
        fe.close()

        # diffcheck
        diff = Compare().check(expected, actual)

        betterDiff = {}

        try:
            for item in diff['_content'].items():
                currPacketIndex = int(item[0])
                tempDiffPacket = {}
                for field in item[1]:
                    tempDiffPacket[field] = item[1][field]['_expected']
                betterDiff[currPacketIndex] = tempDiffPacket
        except:
            with open("jsonDiffs/" + filename[0:-5] + "_diff.json",
                      "w") as outfile:
                json.dump({"Error": "Diff Check Failed on " + filename},
                          outfile)
        else:
            with open("jsonDiffs/" + filename[0:-5] + "_diff.json",
                      "w") as outfile:
                json.dump(betterDiff, outfile)

        numDiffsDone += 1
