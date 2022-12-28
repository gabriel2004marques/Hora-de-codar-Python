print("Quadrado")
lado = float(input("Escreva um lado de um quadrado: "))
if lado <= 0:
    print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
elif lado > 0:
    r = lado * lado
    print("A area deste quadrado é igual a: {}".format(r))
    