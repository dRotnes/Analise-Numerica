#IMPORTACOES
import math

#DECLARACAO FUNCOES
def func(x):
    return (x*math.cos(x)) - math.log(x)

def der_func(x):
    return (math.cos(x)) - (x*math.sin(x)) - (1/x)

def newt(x0, erroiter, count, eps):
    raiz=x0
    print(count, raiz, erroiter)
    if der_func(raiz) == 0: # se a derivada for zero sai    
        return [raiz, erroiter, count]

    if(erroiter<= eps):
        return [raiz, erroiter, count]

    raiz = raiz-func(raiz)/der_func(raiz)
    erroiter = abs(raiz-x0)


    return newt(raiz, erroiter, count+1, eps)