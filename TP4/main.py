def pontos2(arr, current, media, h, counter, first):
    if(current<media):
        return sorted(arr)
    arr.append(current)
    current = first - counter * h
    return pontos2(arr, current, media, h, counter+1, first)

def pontos1(arr, current, media, h, counter, first):
    if(current>media):
        return sorted(arr)
    arr.append(current)
    current = first + counter * h
    return pontos1(arr, current, media, h, counter+1, first)

def pontosxy(h):
    y_i=1
    xy = []
    listOfPoints1 = pontos1([], 0, 0.5, h, 1, 0)
    listOfPoints2 = pontos2([], 1, 0.5 + h, h, 0, 1-h)
    listOfPoints1.extend(listOfPoints2)
    for i in range(0,len(listOfPoints1)):
        x = listOfPoints1[i]
        xy.append(( x, y_i ))
        y_i = y_i + h*((x**2) - y_i)
    return xy

def main():
    print("----------INICIO CALCULO h = 0.1----------\n")
    print(pontosxy(0.1))
    print("----------FIM CALCULO h = 0.1----------\n")

    print("----------INICIO CALCULO h = 0.01----------\n")
    print(pontosxy(0.01))
    print("----------FIM CALCULO h = 0.01----------\n")

    print("----------INICIO CALCULO h = 0.001----------\n")
    print(pontosxy(0.001))
    print("----------FIM CALCULO h = 0.001----------\n")
main()
