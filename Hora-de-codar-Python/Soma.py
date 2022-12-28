n1 = float(input("Escreva um número: "))
n2 = float(input("Escreva outro número: "))
n3 = float(input("Escreva mais um número: "))
if n1 < n2 and n1 < n3:
    soma = n2 + n3
    print("Os maiores números são os números {} e {} e a soma entre ele é igual a: {}".format(n2 , n3 , soma))
if n2 < n1 and n2 < n3:
    soma = n1 + n3
    print("Os maiores números são os números {} e {} e a soma entre ele é igual a: {}".format(n1 , n3 , soma))
if n3 < n1 and n3 < n2:
    soma = n2 + n1
    print("Os maiores números são os números {} e {} e a soma entre ele é igual a: {}".format(n1 , n2 , soma))
    