#include<stdio.h>


    int main(){
        int saldo = 1000;
        int valorsaque = 300;

        if (saldo >= valorsaque) {

            saldo = saldo - valorsaque;
            printf("Saque realizado! Novo saldo: %d\n", saldo);

        }
        
        printf("Obrigado por usar o banco.\n");







    return 0;

}