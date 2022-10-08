# Questao 3
# import das bibliotecas utilizadas
import math

# Variaveis globais
maxvalue_eulerone = 16
maxvalue_eulertwo = 20
j_initial_value = 1
k_initial_value = 0
euler_initial_Value = 0

# Primeiro calculo de euler
def eulerValueOneRecursive(j):
  if (j > maxvalue_eulerone):
    return
  n = 10**j
  finalresult = (1 + (1 / n))**n
  print("j = {}, n= {}, Euler = {}\n".format(
    j, n, finalresult))
  return eulerValueOneRecursive(j + 1)

#Segundo calculo de euler
def eulerValueTwoRecursive(euler, k):
  if (k > maxvalue_eulertwo):
    return euler
  euler += 1 / math.factorial(k)
  print("m = {}, Euler= {}\n".format(k, euler))
  return eulerValueTwoRecursive(euler, k + 1)

def finalResult():
  print("---------- Questao A -----------\n")
  eulerValueOneRecursive(j_initial_value)
  
  print("---------- Questao B -----------\n")
  eulerValueTwoRecursive(euler_initial_Value, k_initial_value)