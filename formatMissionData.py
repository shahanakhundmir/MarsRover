def outputAsString(missionData):
    for data in missionData:
        if type(data)== str:
            print(data)
        else:
            print(f"{data.get('x')} {data.get('y')} {data.get('direction')}")