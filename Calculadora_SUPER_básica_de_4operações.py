#selecionar operação
operacao = input('Escolha a operação: ')
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num = [num1 , num2]

#definindo as possíveis operações
def soma(num):
  soma = num1 + num2
  print('A resposta é', soma)
  
def subt(num):
  subt = num1 - num2
  print('A resposta é', subt)

def mult(num):
  mult = num1 * num2
  print('A resposta é',mult)

def div(num):
  div = num1 / num2
  print('A resposta é', div)

#dando os resultados
if operacao == 'soma':
  soma(num)

elif operacao == 'subtração':
  subt(num)

elif operacao == 'multiplicação':
  mult(num)

elif operacao == 'divisão':
  div(num)
  
#em caso de uma palavra não esperada ser inserida em operacao
else:
  print('Ops! \nVocê deve ter selecionado a operação errada, tente novamente utilizando os termos "soma", "subtração", "multiplicação" ou "divisão"')