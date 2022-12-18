def pontos2(listOfPoints, current, media, h):
    if(current<=media):
        return listOfPoints
    current -= h
    listOfPoints.append(current)
    pontos2(listOfPoints, current, media, h)

def pontos1(listOfPoints, current, media, h):
    if(current>=media):
        return listOfPoints
    current += h
    listOfPoints.append(current)
    pontos1(listOfPoints, current, media, h)

def pontosxy(h):
    xy=[]
    y_i=1

    listOfPoints1 = pontos1([0], 0+h, 0.5, h)
    listOfPoints2 = pontos2([], 1-h, 1/(2+h), h)
    listOfPoints2.append(1)
    listOfPoints1.extend(listOfPoints2)

    for i in range(0,len(listOfPoints1)):
        x = listOfPoints1[i]
        xy.append(( x, y_i ))
        y_i = y_i + h*((x**2) - y_i)
    return xy

print(pontosxy(0.1))
print(pontosxy(0.01))
print(pontosxy(0.001))
