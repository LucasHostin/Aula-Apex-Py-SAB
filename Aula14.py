import random

n1 = str(input("Digite um nome:"))
n2 = str(input("Digite um nome:"))
n3 = str(input("Digite um nome:"))
n4 = str(input("Digite um nome:"))

#Array
lista = [n1, n2, n3, n4] 
print(lista)
sorteio = random.choice(lista)

print(sorteio)

# Random é um recurso que ajuda a gerencias numeros ou strings aleatorias 
# Choice é ultilizado para escolher um numero ou uma string aleatoria

