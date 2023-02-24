numero = int(input("Entre com um número inteiro:\n"))
soma = 0
n = 0
while n <= numero:
  soma += n
  n += 1
print(f"A soma de todos os números menores ou iguais a {numero} é igual a {soma}.")