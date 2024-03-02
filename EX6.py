#--- Exercício - Dicionários
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: Nome, Posicao, Numero, PernaBoa
#--- Crie um dicionario para armazenar os dados
#--- Imprima todos os jogadores e seus dados
#-- E ultilizando o FOR     

lista_jogadores = []
for i in range(3):
    nome=input("Digite o nome do Jogador: ")
    posicao=input("Digite o posicao do Jogador: ")
    numero=input("Digite o numero do Jogador: ")
    PernaBoa=input("Digite a perna boa do Jogador: ")

dicionario = {
    "nome": nome,
    "posicao": posicao,
    "numero":numero,
    "PernaBoa":PernaBoa
}

lista_jogadores.append(dicionario)

for dicionario in lista_jogadores:

    print(f"Nome={dicionario['Nome']},")

