//Até 12 anos: Categoria Infantil
//De 13 a 17 anos: Categoria Juvenil
//De 18 a 59 anos: Categoria Adulto
//60 anos ou mais: Categoria Sênior
#include<stdio.h>

int main(){
    int idade;
    printf("Qual eh a idade do atleta? \n");
    scanf("%d", &idade);
    if (idade <= 12 ) {
        printf("Categoria Infantil");
    } else if (idade <= 17) {
        printf("Categoria Juvenil");
    } else if (idade <= 59) {
        printf("Categoria adulto");
    } else {
        printf("Categoria senior");
    }


    return 0;
}