#100_quilowatts custa um sétimo do salário minímo escreva um algoritmo que receba o valor do salário mínimo e a
# quantidade de quilowatts gasta por uma residência e mostre na tela: a) o valor em reais de cada quilowatt e b) o valor total a ser pago.

salario_minimo = float(input("Escreva o valor do salário minímo atual: "))
qntd_quilowatts = float(input("Escreva o valor de quilowatts gastos na sua casa: "))

valor_100kw = salario_minimo / 7
valor_1kw = valor_100kw / 100

valor_total = qntd_quilowatts * valor_1kw

print("Valor de cada quilowatt: R$", valor_1kw)
print("Valor total a pagar: ", valor_total)