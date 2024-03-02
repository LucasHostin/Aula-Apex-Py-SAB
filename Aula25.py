#for c in range(10,0,-1):
#    print(c)


from time import sleep

#### bloco 1 
# variavel recebendo dados:
nome = input("Digite o seu nome -> ")
sobrenome = input("Digite o seu sobrenome -> ")
idade = int(input("Digite a sua idade -> "))

### bloco 2
## recebendo as notas 

lista_nota = []

for lista in range(0,4):
    nota = float(input("Digite a sua nota -> "))
    lista_nota.append(nota)

### bloco 3
### fazendos a media 

media = sum(lista_nota) / len(lista_nota)

###
for c in range(0, 10):
            print("*")
            sleep(1)

