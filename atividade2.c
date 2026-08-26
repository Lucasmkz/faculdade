#include<stdio.h>

int main(){
    float kg;
    float metro;
    float calculo;


    printf("Digite seu peso atual: \n");
    scanf("%f", &kg);
    printf("Digite sua altura em metros: \n");
    scanf("%f", &metro);

    calculo = kg / (metro * metro);
    
    printf("\n===Clinica Medica===\n");
    printf("Seu IMC Calculado e: %.2f\n",  calculo);
    printf("====================\n");

    
    
    
    
    return 0;

}