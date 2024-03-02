
idadeteste = input("Digite a sua idade: ")

idade = int(idadeteste)

#idade = 70 

if idade > 18 and idade < 60:
    print("Voce é adulto")
elif idade < 18 and idade > 12:
    print("voce é adolecente")
elif idade < 12:
    print("voce é uma crianca")
elif idade >= 18:
    print("voce tem 18 anos")
else: 
    print("voce é idoso")

#if 
#elif
#else
    