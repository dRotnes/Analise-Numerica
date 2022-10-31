# Importacao das bibliotecas utilizadas
import sys

# Definicao das variáveis globais
epsilon_func_initial = 1.0

# Definicao da função recursiva para calculo do epsilon máquina
def epsilon_machine(epsilon_func):
  if(epsilon_func + 1 <= 1):
    return epsilon_func * 2
  epsilon_func = epsilon_func / 2
  return epsilon_machine(epsilon_func)

# Funcao principal a ser chamada no arquivo analisenumericap1.py
def run_epsilonMachine():
  # Primeira maneira de encontrar Epsilon Máquina (biblioteca sys)
  epsilon_sys = sys.float_info.epsilon
  
  # Segunda maneira de calcular Epsilon Máquina (função epsilon_machine)
  epsilon_func = epsilon_machine(epsilon_func_initial)
  
  # Retorna ambos os valores em um objeto
  return {'epsilon_sys':epsilon_sys,'epsilon_func': epsilon_func}

