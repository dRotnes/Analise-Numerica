#Importacao das bibliotecas necessárias para auxiliar nos testes
import questao2 as q2
import questao3 as q3
import questao1 as q1

# Questao 1
print("-------- Resultados Questão 1 --------\n")
epsilon = q1.run_epsilonMachine()
print("Epsilon da biblioteca sys: {} \n".format(epsilon['epsilon_sys']))
print("Epsilon da função: {} \n".format(epsilon['epsilon_func']))

# Questao 2
print("-------- Resultados Questão 2 (a e b já inclusos) --------")
q2.finalResult()

# Questao 3
print("\n-------- Resultados Questão 3 --------\n")
q3.finalResult()
