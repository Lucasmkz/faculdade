#include <stdio.h>

int main() {
    int valorsaque;
    int notas50;
    int troco;

    printf("Valor do saque (R$): ");
    scanf("%d", &valorsaque);

    notas50 = valorsaque / 50;
    troco = valorsaque % 50;

    printf("\n--- Dispenser ---\n");
    printf("Notas de 50: %d\n", notas50);
    printf("Resto: %d\n", troco);

    return 0;
}