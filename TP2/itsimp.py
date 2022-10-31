#IMPOORTACOES
import math

#DECLARACAO FUNCOES
def func(x):
    return math.acos(math.log(x)/x)

def itsimp(x0, x1, erroiter, count, eps):

    print(count,x1, erroiter)
    if(erroiter<=eps):
        return [x1, erroiter, count]

    x0 = x1
    x1 = func(x0)
    erroiter = abs(x1-x0)
    return itsimp(x0, x1, erroiter, count+1, eps)
