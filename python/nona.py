"""#MÉTODOS E FUNÇÕES DE LISTAS

lista = [1,3,12,8,2]

#append - adiciona um elemento no final da lista

print("Antes do append: ", lista)

lista.append(3)

print("Depois do append: ", lista)

#insert - adiciona um elemento na posição escolhida

print("Antes do insert: ", lista)

lista.insert(2,10) #2 posição do novo elemento, 10 novo elemento

print("Depois do insert: ", lista)

#extend - juntar duas listas, colocando no final 

lista2 = [1,2,3]

lista.extend(lista2)
print("Depois do extend: ", lista)

#pop - remover o elemento que especificar, se não especificar remove o último

lista.pop()
print("Lista depois do pop: ", lista)
lista.pop(0)
print("Lista depois do pop: ", lista)

#remove - informa-se o elemento a ser removido, e se houver repetições, elimina o primeiro

lista.remove(3)
print("Depois do remove: ", lista)

#count - contar quantas vezes aparece um elemento

print("Quantidade de 2 na lista: ", lista.count(2))

#index - diz o index de um determinado elemento da lista

print("O index do elemento 12: ", lista.index(12))

#sort - ordenar
lista.sort() #ordem crescente

print(lista)

lista.sort(reverse=True) #ordem decrescente
print(lista)

"""
#FUNÇÕES

lista = [1,3,12,8,2]

#LEN - quantos elemetos tem na lista

print(len(lista))

#SUM - soma todos os elementos

print(sum(lista))

#MAX - retorna o maior valor
#MIN - retorna o menor valor

print(max(lista))
print(min(lista))