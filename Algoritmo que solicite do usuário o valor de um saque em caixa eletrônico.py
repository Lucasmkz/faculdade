# 1. Entrada
valor = int(input("Digite o valor do saque: "))


# 2. Notas de 100
n100 = valor // 100
valor = valor % 100  # atualiza o restante


# 3. Notas de 50
n50 = valor // 50
valor = valor % 50


# 4. Notas de 20
n20 = valor // 20
valor = valor % 20


# 5. Notas de 10
n10 = valor // 10
valor = valor % 10


# 6. Notas de 5
n5 = valor // 5
valor = valor % 5


# 7. Saída
print("Cédulas de 100:", n100)
print("Cédulas de 50:", n50)
print("Cédulas de 20:", n20)
print("Cédulas de 10:", n10)
print("Cédulas de 5:", n5)