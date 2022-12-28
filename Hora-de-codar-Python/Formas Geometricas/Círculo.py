print("Círculo")
r = float(input("Escreva o raio de um círculo: "))
a = 3.14 * (r * r)
if r > 0:
  print("A area deste círculo é igual a: {}.".format(a))
elif r <= 0:
    print("ERRO ! INFORME MAIOR QUE 0")
