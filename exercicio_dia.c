#include<stdio.h>
//Exercício 3 Conversor de Temperatura
// F =  (C x 1.8) + 32
    int main(){
        float celsius, farenheit;
        printf("Digite a temperatura em graus Celsius: ");
        scanf("%f", &celsius);
        farenheit = (celsius * 1.8) + 32;
        printf("A temperatura em farenheit é: " "%.2f", farenheit);








        return 0;

    }