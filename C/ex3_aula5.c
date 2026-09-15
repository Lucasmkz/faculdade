#include <stdio.h>

int main() {
    int escolha;

    printf("Escolha as opcoes:\n");
    printf("[1] Somar\n");
    printf("[2] Subtrair\n");
    printf("[3] Multiplicar\n");
    printf("Digite sua escolha: ");
    scanf("%d", &escolha);

    switch (escolha) {
        case 1:
            printf("Voce escolheu a soma!\n");
            break;

        case 2:
            printf("Voce escolheu a subtracao!\n");
            break;

        case 3:
            printf("Voce escolheu a multiplicacao!\n");
            break;

        default:
            printf("Opcao invalida!\n");
            break;
    }

    return 0;
}
