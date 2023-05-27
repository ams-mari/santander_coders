#LISTAS

#Criando listas

""" lista = []
lista =list()
lista =[]
lista = [26,'Mariana', 3.14, False]
lista_de_lista = [10, [1,2,3]]

"""

#INDEXAÇÃO E SLICES

lista = [26,'Mariana', 3.14, False]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4]) - out of range
#print(lista[-1]) - de tras para frente

#Slices

lista = [10,50,30,40,25,60,5]
print(lista[0:3]) #começa no index 0 e vai até menor que o 3 
print(lista[3:6]) 
print(lista[3:])  #vai até o final
print(lista[2:6:2]) # começa no 3, até o 6, de 2 em 2


#Iterações com FOR

#1  Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

#2 Utilizando tamanho da lista

print("Comprimento da lista:", len(lista))

for i in range(len(lista)) :
    print(i)