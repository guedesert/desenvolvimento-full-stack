class Pedido :
  def __init__(self, cor, tamanho, nome):
    self.cor = cor
    self.tamanho = tamanho
    self.nome = nome
  def __repr__(self):
    return repr((self.cor, self.tamanho, self.nome))
while True:
  pedidofinal = []
  qtd = int(input())
  if qtd == 0:
    break
  else:
    for item in range(qtd):
      nome = input()
      cor,tamanho = input().split()
      if tamanho == "P":
        tamanho = 1
      elif tamanho == "M":
        tamanho = 2
      elif tamanho == "G":
        tamanho = 3
      p = Pedido(cor, tamanho, nome)
      pedidofinal.append(p)
    pedidofinal = sorted(pedidofinal,key=lambda pedido: (pedido.cor, pedido.tamanho, pedido.nome))
    for item in pedidofinal:
      if item.tamanho == 1:
        print(f"{item.cor} P {item.nome}")
      elif item.tamanho == 2:
        print(f"{item.cor} M {item.nome}")
      elif item.tamanho == 3:
        print(f"{item.cor} G {item.nome}")