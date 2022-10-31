#IMPORTS
import bisec
import newt
import itsimp
import time

#VARIAVEIS GLOBAIS
eps = 5*(10**-8)

#BISSECOES SUCESSIVAS
#VARIAVEIS
a = 1.3
b = 1.4
erroiter_bisec = abs(b-a)
m = a
vfa = bisec.func(a)
count_bisec = 0

#CHAMADA
print("\n--------------- BISSECÇÔES SUCESSIVAS ---------------")
bisec_call = bisec.bisec(a, b, erroiter_bisec,m, vfa, count_bisec, eps)
print("\nFINAL RESULT")
print("M: {}, ERROITER: {}, ITERACOES: {}\n" .format(bisec_call[0],bisec_call[1],bisec_call[2]))


#ITERACOES SIMPLES
#VARIAVEIS
x0_itsimp = 1.3
x1_itsimp= itsimp.func(x0_itsimp)
erroiter_itsimp = abs(x1_itsimp-x0_itsimp)
i = 1
count_itsimp = 0

#CHAMADA
print("\n--------------- ITERAÇÕES SIMPLES ---------------")
itsimp_call = itsimp.itsimp(x0_itsimp, x1_itsimp, erroiter_itsimp, count_itsimp, eps)
print("\nFINAL RESULT")
print("M: {}, ERROITER: {}, ITERACOES: {}\n" .format(itsimp_call[0],itsimp_call[1],itsimp_call[2]))


#NEWTON
#VARIAVEIS
x0_newt = 1.3
x1_newt = x0_newt-newt.func(x0_newt)/newt.der_func(x0_newt)
erroiter_newt = abs(x1_newt-x0_newt)
count_newt = 0
#CHAMADA
print("\n--------------- NEWTON ---------------")
newt_call = newt.newt(x0_newt, erroiter_newt, count_newt, eps)
print("\nFINAL RESULT")
print("M: {}, ERROITER: {}, ITERACOES: {}\n" .format(newt_call[0],newt_call[1],newt_call[2]))

