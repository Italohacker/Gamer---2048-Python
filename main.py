from random import randint
from os import name, system

matriz = []  

pontuacao = 0
verificarf = True

#Inicializar matriz
def display(matriz, pontuacao):
  limpartela()
  print('Pontuação:', pontuacao)
  for i in range(4):
    x=""
    for j in range(4):
      x += '\t' + str(matriz[i][j])
    x = '[' + x + '\t]'
    print(x)

def adicionarnumero(matriz):
  cond = False
  for i in range(4):
    for j in range(4):
      if matriz[i][j] == 0:
        cond = True
  
  while cond:
    n1 = randint(0,3)
    n2 = randint(0,3)
    if matriz[n1][n2] == 0:
      matriz[n1][n2] = 2
      break

#Limpartela
def limpartela():
  if name == 'nt': # for windows 
    system('cls') 
  else: # for mac and linux
    system('clear')

#Gameloop 
def movimentos(matriz, pontuacao):
  jogada = input("Escolha o movimento: ")
  if jogada == 'W' or jogada == 'w':
    cima(matriz)
    pontuacao = juntarCima(matriz, pontuacao)
    cima(matriz)
  elif jogada == 'A' or jogada == 'a':
    esquerda(matriz)
    pontuacao = juntarEsquerda(matriz, pontuacao)
    esquerda(matriz)
  elif jogada == 'S' or jogada == 's':
    baixo(matriz)
    pontuacao = juntarBaixo(matriz, pontuacao)
    baixo(matriz)
  elif jogada == 'D' or jogada == 'd':
    direita(matriz)
    pontuacao = juntarDireita(matriz, pontuacao)
    direita(matriz)
  return pontuacao
  
def cima(matriz):
  for k in range(3):
    for i in range(1,4):
      for j in range(4):
        if matriz[i-1][j] == 0:
          matriz[i-1][j], matriz[i][j] = matriz[i][j], 0

def direita(matriz):
   for k in range(3):
     for i in range(4):
      for j in range(0,3):
        if matriz[i][j+1] == 0:
          matriz[i][j+1], matriz[i][j] = matriz[i][j], 0

def esquerda(matriz):
   for k in range(3):
     for i in range(4):
      for j in range(0,3):
        if matriz[i][j] == 0:
          matriz[i][j], matriz[i][j+1] = matriz[i][j+1], 0
          
def baixo(matriz):
  for k in range(3):
    for i in range(0,3):
      for j in range(4):
        if matriz[i+1][j] == 0:
          matriz[i+1][j], matriz[i][j] = matriz[i][j], 0

def juntarCima(matriz, pontuacao, teste = True):
  for i in range(0,3):
    for j in range(4):
      if matriz[i][j] == matriz[i+1][j]:
        if teste:
          matriz[i][j] *= 2
          matriz[i+1][j] = 0
          pontuacao += matriz[i][j]
        else:
          return pontuacao, True
  if not teste:
    return pontuacao, False
  else:
    return pontuacao
  
def juntarEsquerda(matriz, pontuacao, teste = True):
  for i in range(4):
    for j in range(0,3):
      if matriz[i][j+1] == matriz[i][j]:
        if teste:
         matriz[i][j+1] = 0
         matriz[i][j] *= 2
         pontuacao += matriz[i][j]
        else:
          return pontuacao, True
  if not teste:
    return pontuacao, False 
  else:
    return pontuacao

def juntarDireita(matriz, pontuacao, teste = True):
  for i in range(4):
    for j in range(0,3):
      if matriz[i][j+1] == matriz[i][j]:
        if teste:
          matriz[i][j+1] *= 2
          matriz[i][j] = 0
          pontuacao += matriz[i][j+1]
        else:
          return pontuacao, True
  if not teste:
    return pontuacao, False
  else:
    return pontuacao
    
def juntarBaixo(matriz, pontuacao, teste = True):
  for i in range(0,3):
    for j in range(4):
      if matriz[i+1][j] == matriz[i][j]:
        if teste:
          matriz[i+1][j] *= 2
          matriz[i][j] = 0
          pontuacao += matriz[i+1][j]
        else:
          return pontuacao, True
  if not teste:
    return pontuacao, False
  else:
    return pontuacao
    
#Finalização do Game
def verificarfinalizacao(matriz, pontuacao):
  pont = 0
  cont = 0
  zeros = 0
  
  for i in range(4):
    for j in range(4):
      if matriz[i][j] == 2048:
        print('Parabéns! Você venceu! :)')
        return False
      elif matriz[i][j] != 0:
        pont, jc = juntarCima(matriz, pontuacao, False)
        pont, jb = juntarBaixo(matriz, pontuacao, False)
        pont, je = juntarEsquerda(matriz, pontuacao, False)
        pont, jd = juntarDireita(matriz, pontuacao, False)
        if jc or jb or je or jd:
          cont += 1
      else:
        zeros += 1
  if cont == 0 and zeros == 0:
    imprimirtudo(matriz)
    print('Não há mais como jogar.Você perdeu:(', cont)
    return False
  else:
    return True

def gameloop(matriz, pontuacao):
  pontuacao = movimentos(matriz, pontuacao)
  return pontuacao
  
def imprimirtudo(matriz):
 print('GAME 2048')
 display(matriz, pontuacao)
 print('W ou w : mover para cima',) 
 print('S ou s : mover para baixo' ,)
 print('A ou a : mover para esquerda',)
 print('D ou d : mover para direita')
 

def instrucoes(matriz):
  print('O objetivo é alcançar um bloco com a soma de 2048. A cada jogada um novo número é adicionado à tela e se você não somar números suficientes a tela vai se encher toda e não haverão mais jogadas possíveis, então você perde. A ideia é tentar encurralar os números grandes em um mesmo canto da tela.')

#Menu
opçao = 0
print('BEM VINDO AO JOGO 2048.')
while opçao != 2:
  print("OPÇÕES:")
  print("1 - JOGAR")
  print("2 - SAIR")
  print("3 - INSTRUÇÕES")
  print("4 - CRÉDITOS")
  opçao= int(input())
  limpartela()
  
  if opçao == 1:
    verificarf = True
    matriz = [[0 for i in range(4)] for j in range(4)]
    pontuacao = 0
    adicionarnumero(matriz)
    while verificarf:
      imprimirtudo(matriz)
      pontuacao = gameloop(matriz, pontuacao)
      adicionarnumero(matriz)
      verificarf = verificarfinalizacao(matriz, pontuacao)
    
  elif opçao == 3:
    instrucoes(matriz)

  elif opçao == 4:
   print("Créditos:")
   print("Desenvolvido por: Ana Beatriz Farias, Élida Medeiros, Ítalo Dantas e Letícia Lucena")