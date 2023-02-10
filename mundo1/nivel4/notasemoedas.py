m100,m1 = (int(valor) for valor in input().split("."))
n100 = m100//100
m100 %= 100
n50 = m100//50
m100 %= 50
n20 = m100//20
m100 %= 20
n10 = m100//10
m100 %= 10
n5 = m100//5
m100 %= 5
n2 = m100//2
m100 %= 2
m50 = m1//50
m1 %= 50
m25 = m1//25
m1 %= 25
m10 = m1//10
m1 %= 10
m5 = m1//5
m1 %= 5
print(f"NOTAS:\n{n100} nota(s) de R$ 100.00\n{n50} nota(s) de R$ 50.00\n{n20} nota(s) de R$ 20.00\n{n10} nota(s) de R$ 10.00\n{n5} nota(s) de R$ 5.00\n{n2} nota(s) de R$ 2.00")
print(f"MOEDAS:\n{m100} moeda(s) de R$ 1.00\n{m50} moeda(s) de R$ 0.50\n{m25} moeda(s) de R$ 0.25\n{m10} moeda(s) de R$ 0.10\n{m5} moeda(s) de R$ 0.05\n{m1} moeda(s) de R$ 0.01")