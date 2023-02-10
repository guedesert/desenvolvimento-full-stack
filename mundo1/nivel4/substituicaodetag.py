while True:
  try:
    tag = input().lower()
    valor = input()
    texto = input()
    tmod = texto.replace("<", ".<").replace(">", ">.").split(".")
    tnovo = ""
    tfinal = ""
    for palavra in tmod:
      p = palavra
      if p != "":
        if p[0] == "<":
          tnovo += p.lower().replace(tag, valor)
        else:
          tnovo += p
    p2 = texto.split(" ")
    p3 = tnovo.split(" ")
    for i in range(len(p3)):
      if p2[i].lower() == p3[i]:
        tfinal += p2[i] + " "
      else:
        tfinal += p3[i] + " "
    print(tfinal[0:len(tfinal) - 1])
  except EOFError:
    break