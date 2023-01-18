# Problema 1104 - Troca de Cartas @ Beecrowd
# Estrutura de repetição infinita, visto que o problema não solicita números de trocas a seren realizadas.
while True:
    # Leitura e armazenamento da quantidade de cartas de cada uma, considerando a entrada como uma string com 2 números inteiros separados por 1 espaço em branco.
    alice,beatriz = [int(qtd) for qtd in input().split(" ")]
    # Verifica se os valores das quantidades de cartas de cada pessoa é igual a 0 e finaliza o laço encerrando o programa.
    if alice == 0 or(beatriz == 0):
        break
    # Leitura e armazenamento do primeiro conjunto de cartas, considerando a entrada como uma string com N números inteiros separados por 1 espaço em branco, descartando entradas repetidas através do método set().
    cartasalice = set([int(carta) for carta in input().split(" ")])
    # Leitura e armazenamento do segundo conjunto de cartas, considerando a entrada como uma string com N números inteiros separados por 1 espaço em branco, descartando entradas repetidas através do método set().
    cartasbeatriz = set([int(carta) for carta in input().split(" ")])
    # Verifica o tamanho de cada conjunto e executa somente se o primeiro conjunto for maior que o segundo.
    if len(cartasalice) > len(cartasbeatriz):
        # Configura um novo conjunto somente com cartas do primeiro conjunto que não estão listadas no segundo conjunto.
        troca = [carta for carta in cartasbeatriz if carta not in cartasalice]
    else :
        # Configura um novo conjunto somente com cartas do segundo conjunto que não estão listadas no primeiro conjunto.
        troca = [carta for carta in cartasalice if carta not in cartasbeatriz]
    # Imprime o tamanho do conjunto de troca, que corresponde à quantidade de cartas que podem ser trocadas analisando os 2 conjuntos.
    print(len(troca))
# Codificado e disponibilizado por Emanuel Guedes