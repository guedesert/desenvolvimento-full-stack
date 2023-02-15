# Problema 1019 - Conversão de Tempo @ Beecrowd
# Leitura e armazenamento do número inteiro de segundos
segundos = int(input())
# Cálculo do número de minutos que representam o tempo em segundos informado, retornando somente números inteiros.
minutos = segundos//60
# Verifica se sobram segundos após a conversão em minutos.
segundos %= 60
# Cálculo do número de horas  que representam o o tempo em minutos calculado anteriormente, retornando somente números inteiros.
horas = minutos//60
# Verifica se sobram minutos após a conversão em horas.
minutos %= 60
# Imprime o resultado no formato H:M:S.
print(f"{horas}:{minutos}:{segundos}")
# Codificado e disponibilizado por Emanuel Guedes