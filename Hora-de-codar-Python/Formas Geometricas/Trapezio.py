print("Trapezio")
dm = float(input("Escreva a base menor de um trapezio: "))
if dm <= 0:
    print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
elif dm > 0:
    dM = float(input("Agora escreva a base Maior deste trapezio: "))
    if dM <= 0:
        print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
    elif dM > 0:
        h =  float(input("Agora escreva a altura deste trapezio: "))
        if h <= 0 :
            print("ERRO ! ESCREVA UM NÚMERO MAIOR QUE 0")
        elif h > 0:
            r = (dm * dM) * h / 2
            print("A area deste trapezio é igual a : {}".format(r))
            