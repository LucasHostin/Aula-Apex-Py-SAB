
venda = int(input("informe o valor da venda"))
lucro = int(input("informe o valor do lucro"))

lucroreal = venda - lucro

print ("o lucro foi de:", lucroreal,"\na venda foi de:", venda)

if venda > 1000:
    print("ganhou bonus")
else:   
    print("nao ganhou bonus")

