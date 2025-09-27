operacao = ( input ("Selecione a operação matemática desejada: "))

if (operacao == "soma"):
	valor = int(input("Insira o primeiro valor: "))
	valor2 =  int(input("Insira o segundo valor: "))
	soma = valor + valor2
	print("O resultado da soma é:", soma)


elif (operacao == "subtração"):
	valor3 = int(input("Insira o primeiro valor: "))
	valor4 =  int(input("Insira o segundo valor: "))
	subtração = valor3 - valor4
	print("O resultado da soma é:", subtração)


elif (operacao == "multiplicação"):
	valor5 = int(input("Insira o primeiro valor: "))
	valor6 =  int(input("Insira o segundo valor: "))
	multiplicação = valor5 * valor6
	print("O resultado da multiplicação é:", multiplicação)


elif (operacao == "divisão"):
	valor7 = int(input("Insira o primeiro valor: "))
	valor8 =  int(input("Insira o segundo valor: "))
	divisão = valor7 / valor8
	print("O resultado da divisão é:", divisão)

elif (operacao == "potenciação"):
	valor9 = int(input("Insira o primeiro valor: "))
	valor10 =  int(input("Insira o segundo valor: "))
	potenciação = valor9 ** valor10	
	print("O resultado da potenciação é:", potenciação)

elif (operacao == "radiciação"):
	valor11 = int(input("Insira o valor: "))
	valor12 =  int(input("Insira o índice da raiz: "))
	radiciação = valor11 ** (1/valor12)
	print("O resultado da radiciação é:", radiciação)

else:
	print("Operação inválida. Por favor, selecione uma operação válida: soma, subtração, multiplicação, divisão, potenciação ou radiciação.")