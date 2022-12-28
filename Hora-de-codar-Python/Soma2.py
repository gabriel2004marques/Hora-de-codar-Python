nome = input("Qual é o seu nome ? ")
n1 = float(input("Olá {} ! Escreva um número: ".format(nome)))
if n1 <= 0:
    print("{}, escreva um número maior que 0.".format(nome))
elif n1 > 0:
    n2 = float(input("{}, agora escreva outro número: ".format(nome)))
    if n2 <= 0:
        print("{}, escreva um número maior que 0.".format(nome))
    elif n2 > 0:
        r = n1 + n2
        print("{}, a soma entre os números {} e {} é igual a: {}".format(nome , n1 , n2 , r))
        