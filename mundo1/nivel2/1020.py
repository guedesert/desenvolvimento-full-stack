# Problema 1020 - Idade em Dias @ Beecrowd
# Leitura e armazenamento do número de dias.
dias = int(input())
# Cálculo do número de anos que representam o número de dias informado, considerando o ano com 365 dias, retornando somente números inteiros.
anos = dias//365
# Verifica se sobram dias após a conversão em anos.
dias %= 365
# Cálculo do número de meses que representam o número de dias restantes, considerando o mês com 30 dias, retornando somente números inteiros.
meses = dias//30
# Verifica se sobram dias após a conversão em meses.
dias %= 30
# Imprime o resultado em anos, meses e dias com quebra de linha entre eles.
print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
# Codificado e disponibilizado por Emanuel Guedes