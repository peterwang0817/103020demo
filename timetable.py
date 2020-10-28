import requests

stationID = 3360
url = "https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/StationLiveBoard/Station/"+str(stationID)+"?$top=30&$format=JSON"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
response_json = response.json()
print("車次\t開往\t車種\t時間\t備註\t誤點")
for liveboard in response_json["StationLiveBoards"]:
    message = liveboard["TrainNo"] + "\t"
    message += liveboard["EndingStationName"]["Zh_tw"] + "\t"
    message += liveboard["TrainTypeName"]["Zh_tw"] + "\t"
    message += liveboard["ScheduleDepartureTime"][:5] + "\t"
    if liveboard["TripLine"] == 0: message += "\t"
    elif liveboard["TripLine"] == 1: message += "山線\t"
    elif liveboard["TripLine"] == 2: message += "海線\t"
    elif liveboard["TripLine"] == 3: message += "成追線\t"
    if liveboard["DelayTime"] == 0: message += "準點"
    else: message += "晚" + str(liveboard["DelayTime"]) + "分"
    print(message)
