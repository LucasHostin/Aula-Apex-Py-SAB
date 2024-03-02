
# Conceitos de importacao otimizada.

# Esse comando "from math import" deve ser dada para buscar funcoes Ex: sqrt que é a raiz quadrada.
# Raiz quadrada
from math import sqrt 

num = int(input("Digite o numero que voce deseja saber a raiz quadrada"))

soma = sqrt(num)

print(soma)

num1 = int(input ("Digite o primeiro número: "))
num2 = int(input ("Digite o segundo número: "))
num3 = int (input("Digite o terceiro número que vai dividir: "))

resto = num1 + num2 #soma
resto2 = (resto / num3) # dividir 


print ( "a soma entre", num1, "e", num2, "é", resto, " e dividido por ", num3, "o resultado da divisao seria",resto2 )
