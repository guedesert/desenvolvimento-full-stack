# Problema 1690 - Soma de Subconjuntos @ Beecrowd
# Leitura e armazenamento da quantidade de testes a serem realizados.
testes = int(input())
# Estrutura de repetição que permanece ativa até finalizar a quantidade de testes.
for teste in range(testes):
  # Leitura e armazenamento no número inteiro que representa o tamanho do conjunto a ser verificado.
  tamanho = int(input())
  # Leitura e armazenamento do conjunto em formato de lista e organizado de forma crescente, considerando que a entrada é composta por números inteiros sepados por 1 espaço simples.
  conjunto = sorted([int(n) for n in input().split(" ")])
  # Caso o menor número do conjunto não seja 1, a resposta será 1, portanto, a variável resposta já inicia com este valor.
  resposta = 1
  # Estrutura de repetição que permanece ativa até finalizar a varredura dos itens do conjunto.
  for numero in conjunto:
    # Verifica se cada um dos números é maior que o valor contido em resposta, caso seja, o laço é encerrado.
    if numero>resposta:
      break
    # Sendo o número menor ou igual ao valor contido em resposta, soma-se o valor de resposta com ele mesmo e o número.
    else:
      resposta += numero
  # Imprime o resultado do menor número possível de ser obtido por meio da soma dos subconjuntos que podem ser formados com o conjunto de entrada.
  print(resposta)
# Codificado e disponibilizado por Emanuel Guedes