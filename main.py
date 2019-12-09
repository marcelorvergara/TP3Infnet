from tp3_func import *
import time

i = 0 
while i < 1:
  print("Lógica, Computação e Algoritmos")
  print("Teste de Performance - TP3")
  print("\t")
  print ("Escolha uma opção: ")

  print("\t")
  print("Opçao 1 - QUESTÃO 1 - Conta do Restaurante")
  print("Opçao 2 - QUESTÃO 2 - Conta do Restaurante 2")
  print("Opçao 3 - QUESTÃO 3 - Situação Eleitor")
  print("Opçao 4 - QUESTÃO 4 - Concurso de Fantasias")
  print("\t")
  opcao = input("Digite aqui a opção escolhida: ")
  
  if opcao.isdigit() == False:
    opcao = 6
  
  opcao = int(opcao)
  
  if opcao == 6:
    print("  ")
    print("***Comando inválido. Digite valores de 1 a 4 ou 5 para sair***")
    time.sleep(5)
    clear()
  elif opcao == 1:
    questao1()
    wait()
    time.sleep (5)
    clear()
  elif opcao == 2:
    questao2()
    wait()
    time.sleep (5)
    clear()
  elif opcao == 3:
    questao3()
    wait()
    time.sleep (5)
    clear()
  elif opcao == 4:
    questao4()
    wait()
    time.sleep (5)
    clear()
  elif opcao == 5:
    print("\t")
    print("\t\tInté!")
    i = 2
  else:
    print("  ")
    print("***Comando inválido. Digite valores de 1 a 4 ou 5 para sair***")
    wait()
    time.sleep(5)
    clear()
