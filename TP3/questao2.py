#IMPORTACOES
from coeficientes import final_res

#VARIAVEIS
MAX = 11
pontos=[
    (1,8.6),
    (2,7.0),
    (3,6.4),
    (4,4.0),
    (5,2.8),
    (6,1.8),
    (7,1.8),
    (8,2.1),
    (9,3.2),
    (10,4.7),
    (11,6.2),
    (12,7.6)
    ]

h=[1,1,1,1,1,1,1,1,1,1,1,1]

#FUNCOES
def q2a():
    print("\n------------ QUESTAO 2-A ------------")
    final_res(h, pontos, MAX)
    