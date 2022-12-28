nome = input("Qual é o seu nome ?")
n = float(input("Olá {} ! Escreva um número: ".format(nome)))
if n == 0:
    print("Este número é igual a 0.")
if n > 0:
    print("Este número({}) é maior que 0, ou seja, ele é um número POSITIVO !".format(n))
if n < 0:
    print("Este número({}) é menor que 0, ou seja, ele é um número NEGATIVO !".format(n))
    