# Problema 2087 - Conjuntos Bons e Ruins @ Beecrowd
# Laço de repetição infinito, considerando que a quantidade de tentativas não é informada como um valor de entrada.
while True:
  # Lê e armazena a quantidade de elementos que serão incluídas no conjunto.
  qtd = int(input())
  # Verifica se a quantidade de elementos é igual a 0. Neste caso, o código é encerrado.
  if qtd == 0:
    break
  # Criação da lista que armazenará o conjunto a ser informado.
  conjunto = []
  # Criação da variável booleana que será utilizada na verificação de conjunto bom ou ruim.
  prefixo = False
  # Laço de repetição para a leitura e armazenamento dos elementos do conjunto de acordo com a quantidade de elementos informados pelo usuário.
  for i in range(qtd):
    # Lê e adiciona os elementos dentro do conjunto.
    conjunto.append(input())
  # Ordena o conjunto alfabeticamente, visto que os elementos são do tipo str.
  conjunto.sort()
  # Laço de repetição para realizar a verificação dos elementos do conjunto considerando o tamanho do conjunto.
  for p in range(len(conjunto)-1):
    # Verifica se o elemento atual do conjunto é igual ao seu antecessor ou ao seu sucessor.
    if ((conjunto[p].find(conjunto[p+1])==0) or(conjunto[p+1].find(conjunto[p])==0)):
      # Define a variável prefixo como verdadeira e encerra a execução do código.
      prefixo = True
      break
  # Se prefixo for verdadeiro, o código retorna "Conjunto Ruim".
  if prefixo:
    print("Conjunto Ruim")
  # Se prefixo não for verdadeiro, o código retorna "Conjunto Bom".
  else:
    print("Conjunto Bom")
# Codificado e disponibilizado por Emanuel Guedes