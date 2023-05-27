#FUNÇÕES

def saudacao(nome, curso) : 
    print(f"Seja bem vindo(a), {nome}!" )
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")

saudacao("Mariana", "Python")

#Função com parâmetros default - minimiza erros, não obriga os resultados, mas caso não seja preenchido, tem um padrão

def saudacao(nome, curso = "Python") : 
    print(f"Seja bem vindo(a), {nome}!" )
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")

saudacao("Mariana", "Python")

#Funções com retorno

def soma(num1,num2):
    return num1 + num2 #retorna o valor e encerra a função. Só usar no final. 

resultado = soma(5,7)
print(resultado)


def calculadore (num1,num2,operação ="+") :

    if operação == "+" :
        return num1+num2
    elif operação == "-" :
        return num1-num2
    
resultado = calculadore(10,20,"-")
print(resultado)