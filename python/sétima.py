#FOR

"""for variavel in range(10) : - vai de 0 a 9
   print(variavel)"""

"""for variavel in range(1,10) : -  vai do 1 ao 9
    print(variavel)"""

"""for variavel in range(5,11,2) : -  vai do 5 ao 11, de 2 em 2
    print(variavel)"""

soma = 0

for i in range(1,4):
    nota = float(input(f"Informe sua nota {i}: "))

    soma = soma + nota
print(soma/3)