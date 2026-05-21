 #Escreva um programa que alimente uma lista com 5 nomes. Na sequência, solicite um nome ao usuário e mostre uma das seguintes mensagens: "O nome está presente na lista!" ou "O nome não está presente na lista!".

lista = ['Lucas', 'Gabriel', 'Marcos', 'FelipeZePagao', 'Daniel']

buscanome = input("Escreva um nome seu cuzão! ")
if buscanome in lista:
    print(buscanome, "Está na lista!")
else:
    print(buscanome, "não está na lista!")
