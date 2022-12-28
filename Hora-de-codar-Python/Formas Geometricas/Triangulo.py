print("Triangulo")
b = float(input("Escreva a base de um triangulo: "))
if b <= 0:
    print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
elif b > 0:
    h = float(input("Agora escreva a altura deste triangulo: "))
    if h <= 0:
        print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
    elif h > 0:
        r = (b * h) / 2
        print("A area deste triangulo é igual a: {}".format(r))
        