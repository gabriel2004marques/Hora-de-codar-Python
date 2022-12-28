print("Paralelogramo")
b = float(input("Escreva a base de um paralelogramo: "))
if b <= 0:
    print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
elif b > 0:
    h = float(input("Agora escreva a altura desse paralelogramo: "))
    if h <= 0:
        print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
    elif h > 0:
      r = b*h
      print("A area deste paralelogramo é igual a: {}".format(r))
