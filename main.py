print("BEM VINDO AO GABINETE DO SEU LUIZ!", "a merceária onde tudo de mais útil e variado pode ser encontrado")

print("Aqui temos as seguintes categorias de produtos disponíveis: ")
print("Bebidas, Comidas, Frutas, Vegetais, Sobremesas, Frios, Produtos de limpeza, Itens diversos\n")

escolha = str(input(("Qual dos itens citados você está procurando?: ")))

if escolha == "Bebidas":
    print("Você escolheu bebidas!")
    ("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_bebidas = ["Refrigerante", "Suco", "Água", "Cerveja", "Vodka", "Whisky", "Vinho", "Energético", "Chá", "Café", "Leite", "Iogurte", "Água de coco"]#Lista dos produtos: Bebidas
    print(lista_bebidas[0])
    print(lista_bebidas[1])
    print(lista_bebidas[2])
    print(lista_bebidas[3])
    print(lista_bebidas[4])
    print(lista_bebidas[5])
    print(lista_bebidas[6])
    print(lista_bebidas[7])
    print(lista_bebidas[8])
    print(lista_bebidas[9])
    print(lista_bebidas[10])
    print(lista_bebidas[11])
    print(lista_bebidas[12])
    escolha_bebida = str(input("Qual bebida você deseja comprar?: "))

elif escolha == "Comidas":
    print("Você escolheu comidas!")
    print("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_comidas = ["Pão", "Bolo", "Bolacha", "Pizza", "Lasanha", "Macarrão", "Arroz", "Feijão", "Carne", "Frango", "Peixe"]#Lista dos produtos: Comidas
    print(lista_comidas[0])
    print(lista_comidas[1])
    print(lista_comidas[2])
    print(lista_comidas[3])
    print(lista_comidas[4])
    print(lista_comidas[5])
    print(lista_comidas[6])
    print(lista_comidas[7])
    print(lista_comidas[8])
    print(lista_comidas[9])
    print(lista_comidas[10])
    escolha_comida = str(input("Qual comida você deseja comprar?: "))

elif escolha == "Frutas":
    print("Você escolheu frutas!")
    print("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_frutas = ["Maçã", "Uva", "Banana", "Kiwi", "Pitaya", "Melancia", "Abacaxi", "Manga", "Carambola", "Caju", "Laranja", "Pêra", "Ameixa", "Morango", "Limão"]#Lista dos produtos: Frutas
    print(lista_frutas[0])
    print(lista_frutas[1])
    print(lista_frutas[2])
    print(lista_frutas[3])
    print(lista_frutas[4])
    print(lista_frutas[5])
    print(lista_frutas[6])
    print(lista_frutas[7])
    print(lista_frutas[8])
    print(lista_frutas[9])
    print(lista_frutas[10])
    print(lista_frutas[11])
    print(lista_frutas[12])
    print(lista_frutas[13])
    print(lista_frutas[14])
    escolha_fruta = str(input("Qual fruta você deseja comprar?: "))

elif escolha == "Vegetais":
    print("Você escolheu vegetais!")
    print("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_vegetais = ["Alface", "Tomate", "Cenoura", "Batata", "Cebola", "Alho", "Brócolis", "Couve-flor", "Espinafre", "Abobrinha", "Berinjela", "Pepino", "Pimentão", "Vagem"]#Lista dos produtos: Vegetais
    print(lista_vegetais[0])
    print(lista_vegetais[1])
    print(lista_vegetais[2])
    print(lista_vegetais[3])
    print(lista_vegetais[4])
    print(lista_vegetais[5])
    print(lista_vegetais[6])
    print(lista_vegetais[7])
    print(lista_vegetais[8])
    print(lista_vegetais[9])
    print(lista_vegetais[10])
    print(lista_vegetais[11])
    print(lista_vegetais[12])
    print(lista_vegetais[13])
    escolha_vegetal = str(input("Qual vegetal você deseja comprar?: "))

elif escolha == "Sobremesas":
    print("Você escolheu sobremesas!")
    print("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_sobremesas = ["Sorvete", "Pudim", "Torta", "Chocolate", "Picolé", "Brigadeiro", "Beijinho", "Mousse", "Gelatina", "Cupcake", "Churros"]#Lista dos produtos: Sobremesas
    print(lista_sobremesas[0])
    print(lista_sobremesas[1])
    print(lista_sobremesas[2])
    print(lista_sobremesas[3])
    print(lista_sobremesas[4])
    print(lista_sobremesas[5])
    print(lista_sobremesas[6])
    print(lista_sobremesas[7])
    print(lista_sobremesas[8])
    print(lista_sobremesas[9])
    print(lista_sobremesas[10])
    escolha_sobremesas = str(input("Qual sobremesa você deseja comprar?: "))

elif escolha == "Frios":
    print("Você escolheu frios!")
    print("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_frios = ["Mortadela","Queijo", "Mussarela", "Presunto", "Salame", "Peito de peru", "Requeijão"]#Lista dos produtos: Frios
    print(lista_frios[0])
    print(lista_frios[1])
    print(lista_frios[2])
    print(lista_frios[3])
    print(lista_frios[4])
    print(lista_frios[5])
    print(lista_frios[6])
    escolha_frio = str(input("Qual frio você deseja comprar?: "))

elif escolha == "Produtos de limpeza":
    print("Você escolheu produtos de limpeza!")
    print("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_limpeza = ["Detergente", "Sabão em pó", "Água sanitária", "Desinfetante", "Esponja", "Vassoura", "Pá", "Rodo", "Balde", "Limpador multiuso", "Desengordurante", "Amaciante"]#Lista dos produtos: Produtos de limpeza
    print(lista_limpeza[0])
    print(lista_limpeza[1])
    print(lista_limpeza[2])
    print(lista_limpeza[3])
    print(lista_limpeza[4])
    print(lista_limpeza[5])
    print(lista_limpeza[6])
    print(lista_limpeza[7])
    print(lista_limpeza[8])
    print(lista_limpeza[9])
    print(lista_limpeza[10])
    print(lista_limpeza[11])
    escolha_limpeza = str(input("Qual produto de limpeza você deseja comprar?: "))

elif escolha == "Itens diversos":
    print("Você escolheu itens diversos!")
    print("Temos as seguintes opções disponíveis em nossa merceária: ")
    lista_diversos = ["Pilhas", "Lâmpadas", "Fósforos", "Velas", "Sacos de lixo", "Papel alumínio", "Filme plástico", "Papel toalha", "Guardanapos", "Canetas", "Cadernos", "Lápis"]#Lista dos produtos: Itens diversos
    print(lista_diversos[0])
    print(lista_diversos[1])
    print(lista_diversos[2])
    print(lista_diversos[3])
    print(lista_diversos[4])
    print(lista_diversos[5])
    print(lista_diversos[6])
    print(lista_diversos[7])
    print(lista_diversos[8])
    print(lista_diversos[9])
    print(lista_diversos[10])
    print(lista_diversos[11])
    escolha_diversos = str(input("Qual item diverso você deseja comprar?: "))

else:
    print("Opção inválida ou inexistente! Por favor, escolha uma categoria válida.")#Caso nenhum dos itens acima seja selecionado

if escolha in ["Bebidas", "Comidas", "Frutas", "Vegetais", "Sobremesas", "Frios", "Produtos de limpeza", "Itens diversos"]:#Valor, quantidade e total da compra
    print("Por favor, informe a quantidade desejada do produto: ")
    quantidade = int(input())
    print("Por favor, informe o valor unitário do produto escolhido: ")
    valor_unitario = float(input())
    valor_total = quantidade * valor_unitario
    print("O valor total da sua compra é: R$", valor_total)
    
entrega=input("Você deseja vir buscar seu(s) produto(s) na merceária ou prefere que entreguemos eles em sua casa?\n")
if entrega=="Buscar":
    print("Perfeito! O seu produto estará pronto para ser retirado em até 30 minutos")#Retirada na merceária
else:
    input("insira seu endereço para a entrega de seu(s) produto(s): ")#Endereço de entrega

print("Obrigado por escolher comprar no gabinete do Seu Luiz! Volte sempre!")#Finalização