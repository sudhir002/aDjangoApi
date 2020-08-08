import os
import json

path = os.getcwd()

def SQuerry(type, inputDataP):
    file = open(path + "/file/{}".format('TestJSON.json'))
    jData = json.load(file)
    mainList = jData["members"]
    allID = [list(x.values())[0] for x in mainList]
    if inputDataP in allID:
        indexofID = allID.index(inputDataP)
        print('--------------', inputDataP, indexofID)
        finalData = mainList[indexofID]
        return finalData
    else:
        return ({'status': 'no found'})