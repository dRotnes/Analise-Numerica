#IMPOORTACOES
import math

#DECLARACAO FUNCOES
def func(x):
    return (x*math.cos(x)) - math.log(x)

def bisec(a, b, erroiter, m , vfa, count, eps):
    print(count, m, erroiter)
    if(erroiter<=eps):
        return [m,erroiter, count]
    
    m = (a+b)/2
    vfm = func(m)
    if(vfm == 0):
        erroiter = 0

    if(vfm * vfa < 0):
        b = m
    else:
        a = m
        
    return bisec(a,b, erroiter/2, m, vfa, count+1, eps)

