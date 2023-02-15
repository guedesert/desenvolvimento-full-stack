# Problema 1021 - Notas e Moedas @ Beecrowd
# Recebe um valor decimal que será separado em 2 valores distintos de forma que os 2 passarão a serem considerados inteiros, sendo o valor de reais armazenado em m100 e o valor de centavos armazenado em m1.
m100,m1 = (int(valor) for valor in input().split("."))
# Calcula o número de notas de R$ 100,00 presentes no número informado a partir de uma divisão exata por 100.
n100 = m100//100
# Calcula quantos reais sobram após serem retiradas as notas de R$ 100,00.
m100 %= 100
# Calcula o número de notas de R$ 50,00 presentes em m100 a partir de uma divisão exata por 50.
n50 = m100//50
# Calcula quantos reais sobram após serem retiradas as notas de R$ 50,00.
m100 %= 50
# Calcula o número de notas de R$ 20,00 presentes em m100 a partir de uma divisão exata por 20.
n20 = m100//20
# Calcula quantos reais sobram após serem retiradas as notas de R$ 20,00.
m100 %= 20
# Calcula o número de notas de R$ 10,00 presentes em m100 a partir de uma divisão exata por 10.
n10 = m100//10
# Calcula quantos reais sobram após serem retiradas as notas de R$ 10,00.
m100 %= 10
# Calcula o número de notas de R$ 5,00 presentes em m100 a partir de uma divisão exata por 5.
n5 = m100//5
# Calcula quantos reais sobram após serem retiradas as notas de R$ 5,00.
m100 %= 5
# Calcula o número de notas de R$ 2,00 presentes em m100 a partir de uma divisão exata por 2.
n2 = m100//2
# Calcula quantos reais sobram após serem retiradas as notas de R$ 2,00, que irá diretamente corresponder à quantidade de moedas de R$ 1,00.
m100 %= 2
# Calcula o número de moedas de R$ 0,50 presentes no número informado a partir de uma divisão exata por 50.
m50 = m1//50
# Calcula quantos centavos sobram após serem retiradas as moedas de R$ 0,50.
m1 %= 50
# Calcula o número de moedas de R$ 0,25 presentes em m1 a partir de uma divisão exata por 25.
m25 = m1//25
# Calcula quantos centavos sobram após serem retiradas as moedas de R$ 0,25.
m1 %= 25
# Calcula o número de moedas de R$ 0,10 presentes em m1 a partir de uma divisão exata por 10.
m10 = m1//10
# Calcula quantos centavos sobram após serem retiradas as moedas de R$ 0,10.
m1 %= 10
# Calcula o número de moedas de R$ 0,05 presentes em m1 a partir de uma divisão exata por 5.
m5 = m1//5
# Calcula quantos centavos sobram após serem retiradas as moedas de R$ 0,05, que irá diretamente corresponder à quantidade de moedas de R$ 0,01.
m1 %= 5
# Impressão do resultado contendo as quantidades de cada nota separadas por uma quebra de linha feita com "\n".
print(f"NOTAS:\n{n100} nota(s) de R$ 100.00\n{n50} nota(s) de R$ 50.00\n{n20} nota(s) de R$ 20.00\n{n10} nota(s) de R$ 10.00\n{n5} nota(s) de R$ 5.00\n{n2} nota(s) de R$ 2.00")
# Impressão do resultado contendo as quantidades de cada moeda separadas por uma quebra de linha feita com "\n".
print(f"MOEDAS:\n{m100} moeda(s) de R$ 1.00\n{m50} moeda(s) de R$ 0.50\n{m25} moeda(s) de R$ 0.25\n{m10} moeda(s) de R$ 0.10\n{m5} moeda(s) de R$ 0.05\n{m1} moeda(s) de R$ 0.01")
# Codificado e disponibilizado por Emanuel Guedes