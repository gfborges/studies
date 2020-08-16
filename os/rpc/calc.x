/*
Procedimentos RPC
soma - soma dois numeros
mult - multiplica dois numeros
div  - divide dois numeros
max  - retorna maior numero
min  - retorna menor numero
*/
struct in {
    int a;
    int b;
};

program RPC_SERVER {      /* Nome do programa remoto*/
    version CALCULADORA { /* Declaração da versão*/
        int soma(in) = 1; /* proc. num1*/
        int mult(in) = 2; /* proc. num2*/
        int div(in)  = 3; /* proc. num3*/
        int max(in)  = 4; /* proc. num4*/
        int min(in)  = 5; /* proc. num5*/
    } = 1; /* definicao da versão */
} = 0x3012225; /* numeto do programa remoro (unico) */


