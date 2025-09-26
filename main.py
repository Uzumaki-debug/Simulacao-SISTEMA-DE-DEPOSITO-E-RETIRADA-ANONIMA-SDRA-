print("ACESSO REQUERIDO")
print("NÉCESSÁRIO A INSERÇÃO DA SENHA DE ACESSO")

senha = int(input("Insira a senha do usuário: "))

if (senha == "12345"):
    print("ACESSO CONCEDIDO")
else:
    print("ACESSO RECUSADO")

if ("ACESSO CONCEDIDO"):
    print("INFORME O SEU CPF, POR GENTILEZA")
    cpf = int(input("Insira o seu CPF: "))
    print("CPF VÁLIDO")

if ("CPF VÁLIDO"):
    print("INFORME O SEU NOME, POR GENTILEZA")
    nome = str(input("Insira o seu nome: "))
    print("SEJA BEM VINDO(A) AO SISTEMA DE DEPÓSITO E RETIRADA ANÔNIMO (SDRA) ", nome)

if ("SEJA BEM VINDO(A) AO SISTEMA DE DEPÓSITO ANÔNIMO (SDRA) "):
    print("VOCÊ DESEJA REALIZAR UM DEPÓSITO OU UMA RETIRADA?")
    escolha = str(input("Digite DEPÓSITO ou RETIRADA: "))

if (escolha == "DEPÓSITO"):
    print("VOCÊ ESCOLHEU DEPÓSITO")
    valor_deposito = float(input("Digite o valor que você deseja depositar: R$ "))
    print("VOCÊ DEPOSITOU O VALOR DE R$ ", valor_deposito, " NO SISTEMA SDRA, O VALOR DEPOSITADO SERÁ ENVIADO EM ALGUNS INSTANTES")

if (escolha == "RETIRADA"):
    print("VOCÊ ESCOLHEU RETIRADA")
    valor_retirada = float(input("Digite o valor que você deseja retirar: R$ "))
    print("VOCÊ RETIROU O VALOR DE R$ ", valor_retirada, " NO SISTEMA SDRA, OBRIGADO POR ESCOLHER UTILIZAR OS NOSSOS SERVIÇOS, VOLTE SEMPRE!")