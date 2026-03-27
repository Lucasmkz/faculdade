#Escreva um algoritmo que receba a potência de um aparelho (em watts),
#O número de horas que ele fica ligado por dia
#E o número de dias de uso no mês.
#Calcule e mostre o consumo mensal em kWh.

potencia_aparelho = float(input("Escreva o gasto do seu aparelho em Watts: "))
horas_ligado = float(input("Escreva o numero de horas que o aparelho fica ligado por dia: "))
uso_por_dias = float(input("Escreva o numero de dias de uso no mês: "))

consumo_kWh = (potencia_aparelho * horas_ligado * uso_por_dias) / 1000

print("Seu consumo é de:", consumo_kWh, "kWh mensal!")

