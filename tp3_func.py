# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# esperando ...
def wait():
  i = 0
  x = 10000
  while (x>i):
    print("/", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("-", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("|", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("-", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("\\", end="\r", flush=True)
    print("", end="\r", flush=True)
    i = i +1

#Questão 1 - TP3
def questao1():

  valor = input("Digite o valor da conta: ")
  valor = float(valor.replace (",","."))
  pessoas = int(input("Digite quantas pessoas irão dividir a conta: "))

  dezporcentro = valor * 0.1
  val_pessoa = round((valor+dezporcentro)/pessoas, 2)

  print("O total da conta ficou em: ", valor+dezporcentro)
  print("Valor por pessoa é: ", val_pessoa)

#Questão 2 - TP3
def questao2():

  valor = input("Digite o valor da conta: ")
  valor = float(valor.replace (",","."))
  pessoas = int(input("Digite quantas pessoas irão dividir a conta: "))

  dezporcentro = valor * 0.1
  val_pessoa = round((valor+dezporcentro)/pessoas, 2)

  print("O valor da conta de consumo é: ", valor)
  print("O total da conta com os 10 % ficou em: ", valor+dezporcentro)
  print("Valor por pessoa é: ", val_pessoa)

#Questão 3 - TP3
def questao3():
  nome = input("Digite o nome da pessoa: ")
  idade = input("Digite a idade dessa pessoa: ")
   
  try:
    idade = int(idade)
  except ValueError:
    print("Valor digitado para idade inválido! Favor digitar um valor numérico e inteiro.")
    print("\t")
    questao3()

  idade = int(idade)
  if idade < 16:
    print("\t")
    print(nome," ainda não pode votar!")
  elif idade >= 18 and idade <= 65:
    print("\t")
    print(nome, " é obrigado a votar!")
  else:
    print("\t")
    print (nome, "é eleitos facultativo!")

#Questão 4 - TP3
def questao4():
  nota_vence = 0
  i = 0
  while i < 10:
    nome = input(f"Digite o nome do(a) participante número {i+1}: ")
    nota = input("Digite a nota do participante: ")
    nota = nota.replace(",",".")
    
    try:
      nota = float(nota)
    except ValueError:
      print("Valor digitado para nota inválido.")
      print("Tente novamente.")
      continue

    nota = float(nota)
    i += 1  
    if nota > nota_vence:
      nota_vence = nota
      nome_vence = nome
  
  clear()
  wait()
  print("Com a nota ", nota_vence, "o vencedor é", nome_vence)
