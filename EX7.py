
from random import choice 

nome1 = input("Digite seu nome > ")
nome2= input("Digite seu nome > ")
nome3 = input("Digite seu nome > ")
nome4 = input("Digite seu nome > ")

lista = [
    nome1,
    nome2,
    nome3,
    nome4
]

sorteio = choice(lista)

print ("#"*10, sorteio, "#"*10)

# if else ou for 

# trazendo o uma frase com o ganhador

#o nome sorteado foi o primeiro nome da lista! 
#que é o ....
# 6 nomes 

# DEPOIS DO PRIMEIRO PASSO PRONTO:

# incluir 3 notas e fazer um sistema de aprovado ou reprovado usando o FOR e IF. 


lista_alunos_notas = []

for i in range(0,2):
    lista_alunos = []
    lista_alunos.append(input(f'Digite o nome do aluno {i+1}:'))
    lista_notas = []
    for n in range(0,4):
        lista_notas.append( float(input(f'Digite a nota {n+1}:')) )  
    lista_alunos.append(lista_notas)
    lista_alunos_notas.append(lista_alunos)

for aluno_nota in lista_alunos_notas:    
    notas_aluno = aluno_nota[1]
    media = (notas_aluno[0]+ notas_aluno[1] + notas_aluno[2]+ notas_aluno[3])/4
    resultado = 'Reprovado'
    if media >=7:
        resultado = 'Aprovado'
    print(f'Aluno: {aluno_nota[0]} - média={media} - Resultado: {resultado}')

print(lista_alunos_notas)
