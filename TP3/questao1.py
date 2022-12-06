#IMPORTACOES
from coeficientes import final_res
from sympy import diff, Symbol, sin

#VARIAVEIS
MAX = 7
pontos=[
    (-1, 1.27941550), 
    (-0.71428571, 1.42055103), 
    (-0.42857143, -0.356096713), 
    (-0.14285714, -0.73556720), 
    (0.14285714, 0.77638353), 
    (0.42857143, 0.72344365), 
    (0.71428571, -0.40014286), 
    (1, 0.72058450)
    ]
h=[
    0.28571429,
    0.28571428,
    0.28571429,
    0.28571428,
    0.28571429,
    0.28571428,
    0.28571429,
    0.28571428
    ]

def f(x):
    return x**2+sin(6*x)
    
x=Symbol('x')
dif1 = diff(f(x),x,4)
dif2 = diff(f(x),x,8)
    
#FUNCOES
def q1():
    print("------------ QUESTAO 1-B ------------")
    final_res(h, pontos, MAX)
    print("------------ QUESTAO 1-C ------------")
    print("----------- RESULTADO FINAL ----------")
    print("Diferenciação 1 = {}".format(dif1))
    print("Diferenciação 2 = {}".format(dif2))


