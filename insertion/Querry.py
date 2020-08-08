import os
import json

path = os.getcwd()

def Querry(id, real_name, tz, start_time, end_time):
    file = open(path + "/file/{}".format('TestJSON.json'))
    wfile = path + "/file/{}".format('TestJson.json')
    jData = json.load(file)
    mainList = jData["members"]
    '''data prepration for insert_____________'''
    dict = {}
    time = {}
    activity_periods = []
    allID = [list(x.values())[0] for x in mainList]
    if id not in allID:
        dict["id"] = id
        dict["real_name"] = real_name
        dict["tz"] = tz
        time["start_time"] = start_time
        time["end_time"] = end_time
        activity_periods.append(time)
        dict["activity_periods"] = activity_periods
        mainList.append(dict)
        jData["member"] = mainList
        print([x.values() for x in mainList])
        with open(wfile, 'w') as outfile:
            json.dump(jData, outfile, indent=4)
        return ({"Status":"Sucess", "Api Name": "/insertion"})

    else:
        indexOfid = allID.index(id)
        print(indexOfid)
        print(mainList[indexOfid])
        mainList[indexOfid]['id'] = id
        mainList[indexOfid]['real_name'] = real_name
        mainList[indexOfid]['tz'] = tz
        newTime = {}
        newTime["start_time"] = start_time
        newTime["end_time"] = end_time
        mainList[indexOfid]['activity_periods'].append(newTime)
        with open(wfile, 'w') as outfile:
            json.dump(jData, outfile, indent=4)
        return ({"Status": "Updation Sucess", "Reason": "ID is already existing", "Api Name": "/insertion"})
