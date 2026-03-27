#Escreva um algoritmo que receba a distância total percorrida por um carro (em km)
#A quantidade de combustível gasta (em litros), e calcule:  
# a) o consumo médio do veículo (km/l) 
# b) o custo total da viagem, sabendo que o preço do litro de combustível também deve ser informado pelo usuário.

distancia_total = float(input("Escreva a distancia total percorrida (Em KM): "))
quantidade_cosbustivel = float(input("Escreva a quantidade de cobustivel gasta (Em litros): "))
preco_litro = float(input("Escreva a cotação do combustivel atualmente: "))

consumo_medio = distancia_total / quantidade_cosbustivel
custo_total = consumo_medio * preco_litro

print("O consumo médio do seu veículo foi de:", consumo_medio, "e o custo total da sua viagem foi de", custo_total, "R$")

