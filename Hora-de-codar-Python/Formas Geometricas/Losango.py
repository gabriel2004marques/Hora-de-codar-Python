print("Losango")
dm = float(input("Esccreva a diagonal menor de um losango: "))
if dm <= 0:
    print("ERRO ! INFORME UM NÚMERO MAIOR QUE 0")
elif dm > 0:
    dM = float(input("Agora escreva a diagonal maior deste losango: "))
    if dM <= 0:
        print("ERRO ! INFORME UM NÚMERO MAIOR QUE 0")
    elif dM > 0:
      if dm > dM:
        print("ERRO ! INFORME DIAGONAIS VÁLIDAS (Ex: diagnal menor < diagonal Maior)")
      elif dm < dM:
        r = round((dm * dM) / 2, 1)
        print("A area deste losango é igual a: {}".format(r))
