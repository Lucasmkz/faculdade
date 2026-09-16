#include <stdio.h>

int main() {
    int escolha;
    int num1;
    int num2;
    float resultado;

    printf("Escolha as opcoes:\n");
    printf("[1] Somar\n");
    printf("[2] Subtrair\n");
    printf("[3] Multiplicar\n");
    printf("[4] Divisao\n");

    printf("Digite sua escolha: ");
    scanf("%d", &escolha);

    printf("Digite N1 e N2 (Com espaco): ");
    scanf("%d%d", &num1, &num2);

    switch (escolha) {
        case 1:
            printf("Voce escolheu a soma!\n");

            resultado = num1 + num2;

            printf("O resultado da soma eh: %.2f\n", resultado);
            break;

        case 2:
            printf("Voce escolheu a subtracao!\n");

            resultado = num1 - num2;

            printf("O resultado da subtracao eh: %.2f\n", resultado);
            break;

        case 3:
            printf("Voce escolheu a multiplicacao!\n");

            resultado = num1 * num2;

            printf("O resultado da multiplicacao eh: %.2f\n", resultado);
            break;

        case 4:
            printf("Voce escolheu a divisao!\n");

            if (num2 == 0) {
                printf("Numero invalido: nao e possivel dividir por zero!\n");
            } else {
                resultado = (float)num1 / num2;

                printf("O resultado da divisao eh: %.2f\n", resultado);
            }

            break;

        default:
            printf("Opcao invalida!\n");
            break;
    }

    return 0;
}