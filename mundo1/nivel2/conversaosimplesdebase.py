# Problema 1199 - Conversão Simples de Base @ Beecrowd
# Estrutura de repetição infinita, visto que o problema não solicita números de conversões a serem realizadas.
while True:
  # Leitura e armazenamento do número que será convertido.
  n = input()
  # Estrutura condicional que verifica se o número informado contém o símbolo -, que representaria um número negativo.
  if "-" in n:
    # Caso seja averiguado que o número é negativo, o programa se encerra.
    break
  # Verifica se o número entrado realmente é composto somente por números, a fim de diferenciar entre um número decimal e um número hexadecimal, visto que, neste caso, o hexadecimal inicial com 0x.
  if n.isdigit():
    # Converte o número contido em N para inteiro, para, logo após, convertê-lo em hexadecimal pelo método hex().
    n = hex(int(n))
    # Reformula o resultado da conversão garantindo que os 2 primeiros algarismos do resultado permaneçãm em minúsculo, 0x, e que os demais algarismos sejam formatados em maiúsculo, de acordo com a solicitação de saída do problema.
    n = n[:2] + n[2:].upper()
# Caso entre com um número hexadecimal, o if anterior entenderá que o valor não era numérico, tratando-se então de um número hexadecimal por conta de seu início, 0x.
  else:
    # Converte o número hexadecimal por meio do método int() informando a base do número recebido, 16, por se tratar de um número hexadecimal.
    n = int(n, 16)
  # Imprime o resultado do número convertido para a base oposta.
  print(n)
# Codificado e disponibilizado por Emanuel Guedes