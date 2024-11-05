
def packIT(list):
    finalArr = []
    for i in range(len(list)):
        finalArr.append({
            'title': list[i][0],
            'location': list[i][1],
            'startTime': list[i][2],
            'endTime': list[i][3]
        })
    
    return finalArr




