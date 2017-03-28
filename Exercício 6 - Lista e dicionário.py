'''
Feito por: Rennan Rocha 27/03/2017
'''

rodando = True

turmas = {"1AINF":{}, "1BINF":{}}

def calcularMedia(lista):
  x = 0
  
  for i in range(len(lista)):
    x = x + int(lista[i])
    
  if(len(lista) == 0):
    return 0
    
  return x / len(lista)
  
def adicionarTurma(chave):
  if(chave in turmas):
    print("Esta turma já existe.")
  else:
    turmas[chave] = {}
  
def adicionarAlunoNotas(turma, matricula, notas):
  if(not turma in turmas):
    print("Esta turma não existe.")
  else:
    turmas[turma][matricula] = notas
  
def Menu ():

  print("Opções:\n 1-Adicionar Turma \n 2-Adicionar Aluno e Notas \n 3-Calcular média de um Aluno \n 4-Calcular média de uma Turma \n 5-Sair ")
  
  escolha = int(input("Digite o número da opção que você deseja: "))
  
  if(escolha == 1):
    t = input("Digite a chave identificadora da turma: (Ex: 1BINF)")
    adicionarTurma(t)
  
  elif(escolha ==  2):
    t = input("Digite a identificação da turma: ")
    m = int(input("Digite a matrícula do aluno: "))
    n = input("Digite as notas em sequência do aluno: (Ex: 50.7 70.3 80) ");

    adicionarAlunoNotas(t, m, n.split(' '))
    
  elif(escolha == 3):
    t = input("Digite a identificação da turma do aluno: ")
    m = int(input("Digite a matrícula do aluno: "))
    
    print("A média do aluno", m, "é: ", calcularMedia(turmas[t][m]))
    
  if(escolha == 4):
    t = input("Digite a identificação da turma: ")
    if(not t in turmas):
      print("Esta turma não existe.")
    else:
      notas = []
      
      for a in turmas[t].values():
        for n in range(len(a)):
          notas.append(a[n])
      
      print("A média da turma é:", calcularMedia(notas))
  if(escolha == 5):
    print("Programa sendo finalizado.")
    global rodando
    rodando = False
   
while(rodando):
  Menu()
