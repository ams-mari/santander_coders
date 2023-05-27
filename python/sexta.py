numero_sorteado = 15
numero_usuario = int(input("Informe um número entre 1 e 20: "))

while numero_sorteado != numero_usuario :

    print("Você errou! Tente novamente.")

    numero_usuario = int(input("Informe um número entre 1 e 20: "))

print("Parabéns! Você acertou")

#Exemplo 2 - Com contador

contador = 0

while contador < 5 :
    print(contador)
    contador = contador + 1
    