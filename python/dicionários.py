#criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {"nome" :"Mariana", "idade" : 27, "altura" : 1.77}

print(dicionario)
print(dicionario["idade"])

#adicionar elementos

dicionario ["Programadora"] = True
print(dicionario)

#se já exister um conteúdo, ele é sobrescrito

dicionario["altura"] = 2
print(dicionario)

#Iterando sobre um dicionário - percorre as chaves

for chave in dicionario:
    print(chave, dicionario[chave])

#Testando se uma chave já existe

print("peso" in dicionario)
print("altura" in dicionario)