#6 - Escreva um algoritmo que solicite ao usuário o nome de um produto,
#o preço desse produto 
#e o valor em dinheiro entregue ao vendedor. 
#Em seguida, deve ser mostrada uma mensagem baseada no seguinte exemplo: 
# "Você comprou um produto (Mouse) por R$ 185,00 e entregou ao vendedor R$ 200,00 em dinheiro. 
# Você vai receber R$ 15,00 de troco. Volte sempre!".

nome_produto = (input("Escreva a seguir o nome do produto desejado: "))
preco_produto = float(input("Escreva a seguir o valor do produto desejado: "))
valor_dinheiro = float(input("Escreva o valor em reais entregue ao vendedor: "))

troco = valor_dinheiro - preco_produto

print("Você comprou", nome_produto,"por",preco_produto,"e entregou",valor_dinheiro,"você irá receber",troco, "R$ de troco")

