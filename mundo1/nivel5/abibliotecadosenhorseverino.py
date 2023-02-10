while True:
  try:
    qlivros = int(input())
    biblioteca = []
    for livro in range(qlivros):
      biblioteca.append(input())
    biblioteca.sort()
    for livro in biblioteca:
      print(livro)
  except EOFError:
    break