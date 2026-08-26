#include <stdio.h>

 int main() {
        int idade;
        char inicial;
        float altura;

        printf("Qual é a sua altura? ");
        scanf("%f", &altura);
        printf("Qual é a sua idade? ");
        scanf("%d", &idade);
        printf("Qual é a inicial do seu nome? ");
        scanf(" %c", &inicial);

        printf("\n--- Ficha ---\n");
        printf("Altura: %.2f\n", altura);
        printf("Idade: %d\n", idade);
        printf("Incial: %c\n", inicial);
        printf("--- Ficha ---\n");
        
        
        return 0;
    }