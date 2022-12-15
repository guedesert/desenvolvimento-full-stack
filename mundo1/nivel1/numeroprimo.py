# Problema 1165 - Número Primo @ Beecrowd
# Entrada do número de tentativas.
N=int(input())
# Loop que funcionará até acabar o número de tentativas informado, N.
for i in range(N):
  # Entrada do número a ser testado.
  X=int(input())
  # Criação da variável que vai armazenar o número de divisores encontrados para X.
  divisores=0
  # Loop que será utilizado para realizar os cálculos de testagem de divisores iniciando em 1, pois divisão por 0 não é matematicamente possível, até o valor de X, informado anteriormente, que corresponde ao número a ser testado.
  for d in range(1,X):
    # Verifica se a divisão de X por d resta 0.
    if(X%d==0):
      # Se o resto da divisão é 0, ele soma o valor de divisores encontrados com o valor de d, que também serve como contador neste loop, e atribui à variável divisores.
      divisores+=d
  # Se a quantidade de divisores é maior do que 2, o código encerra e imprime a informação de que o número não é primo.
  if(divisores>2):
    print(X,"nao eh primo")
  # Se a quantidade de divisores é menor ou igual a 2, o código encerra e imprime a informação de que o número é primo.
  else:
    print(X,"eh primo")