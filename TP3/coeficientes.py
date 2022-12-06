#VARIAVEIS GLOBAIS
counter = 1

#FUNCOES
def coeficientes(counter, coefic, h, pontos, MAX):
    if counter >= MAX:
        return coefic

    p1 = round(h[counter]/6, 8)
    p2 = round((h[counter]+h[counter+1])/3, 8)
    p3 = round(h[counter+1]/6, 8)
    p4 = round((pontos[counter+1][1]-pontos[counter][1])/h[counter+1]-(pontos[counter][1]-pontos[counter-1][1])/h[counter], 8)

    coefic.append((counter,p1,p2,p3,p4))

    return coeficientes(counter+1, coefic, h, pontos, MAX)

def final_res(h, pontos, MAX):
    coefic = []
    coeficientes(counter, coefic, h, pontos, MAX)
    print("----------- RESULTADO FINAL ----------")
    for i in coefic:
        print("Counter = {}".format(i[0]))
        print("Valores = {}, {}, {}, {}\n".format(i[1],i[2], i[3], i[4]))



        