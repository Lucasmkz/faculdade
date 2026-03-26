latas_350 = int(input("Escreva a quantidade de latas compradas: "))    #a quantidade de latas deverá ser convertida para litros (X * 350) / 1000)
garrafas_600 = int(input("Escreva a quantidade de garrafas 600ml foram compradas: ")) #a quantidade de garrafas deverá ser convertida para litros (y * 600) / 1000)
garrafas_2l = int(input("Escreva a quantidade de garrafas 2L compradas: "))    #a quantidade de garrafas já está em litros (não deverá ser convertida)

litros_latas = (latas_350 * 350) / 1000
litros_garrafas600 = (garrafas_600 * 600) / 1000
litros_garrafas2L = garrafas_2l5 * 2

total_litros = litros_latas + litros_garrafas600 + litros_garrafas2L 

print("Total de litros compradas: ", total_litros)