# Importacao das bibliotecas utilizadas
import math
from msilib.schema import Error

# Definicao das variaveis globais
range_start = 8
range_end = 17 # 16 + 1 por causa das especificações da função range
initial_values_factorial = [0,1] #soma, k
initial_values_nonFactorial = [0,0.5,1] #soma, primeiro termo do somatório, k
abs_error = (math.pi**2)

# Definicao recursiva do somatorio com fatorial
def sumFactorial(epsilon, sum, k):
  try:
    ak = ((math.factorial(k - 1))**2) / (math.factorial(k * 2))
    initial = ak
    if initial >= epsilon:
      sum += initial
      return sumFactorial(epsilon, sum, k + 1)
    else:
      return [k, 18 * sum]
  except:
    return  Error("Out of bounds")

# Definicao recursiva do somatorio sem fatorial
def sumNonFactorial(epsilon, sum, ak, k):
  try:
    initial = ak
    if initial * 4/3 >= epsilon:
      ak *= ((k**2) / ((2 * k + 2) * (2 * k + 1)))
      k+=1
      sum += initial
      return sumNonFactorial(epsilon,sum, ak, k)
    else:
      return [k, 18 * sum]
  except:
    return  Error("Out of bounds")

# Funcao principal que recorre às de somatório questao 3.a
def finalResult():
  for i in range(range_start,range_end):
    # Epsilon varia de 10^-8 a 10^-16
    epsilon = 10**(-i)
    print("\nEpsilon = {}".format(epsilon))
    
    print("Resultados com fatorial")
    # Chama a função com fatorial
    finalresult_factorial = sumFactorial(
      epsilon, 
      initial_values_factorial[0], 
      initial_values_factorial[1]
    )
    # Calcula o valor do erro absoluto para o com fatorial
    abserror_factorial = abs(abs_error - finalresult_factorial[1])

    # Printa para cada valor de Epsilon o número de fatores somados, 
    # valor de S final e o valor do erro absoluto
    print("k = {}, S = {}, abs = {}".format(
      finalresult_factorial[0], 
      finalresult_factorial[1], 
      abserror_factorial
      )
    )

    print("Resultados sem fatorial")
    # Chama a função com fatorial
    finalresult_nonFactorial = sumNonFactorial(
      epsilon,
      initial_values_nonFactorial[0],
      initial_values_nonFactorial[1], 
      initial_values_nonFactorial[2]
    )
    # Calcula o valor do erro absoluto para o sem fatorial
    abserror_nonFactorial = abs(abs_error - finalresult_nonFactorial[1])

    # Printa para cada valor de Epsilon o número de fatores somados, 
    # valor de S final e o valor do erro absoluto
    print("k = {}, S = {}, abs = {}".format(
      finalresult_nonFactorial[0], 
      finalresult_nonFactorial[1],
       abserror_nonFactorial
       )
    )
  