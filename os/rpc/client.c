#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "calc.h"

void menu(int* op, in* val) {
    printf("+----- Menu -----+\n");
    printf("|1 - Somar       |\n");
    printf("|2 - Multiplicar |\n");
    printf("|3 - Dividir     |\n");
    printf("|4 - Máximo      |\n");
    printf("|5 - Mínimo      |\n");
    printf("Escolha uma opção: ");
    scanf("%d", op);
    printf("Numeros da operação\n");
    printf("A: ");
    scanf("%d", &val->a);
    printf("B: ");
    scanf("%d", &val->b);
}

void result(int* res){
    if(res == NULL) {
        printf("connection error\n");
        return;
    }
    printf("resultado: %d\n", *res);
}

int main(int argc, char* argv[]) {
    CLIENT *con;
    char *server;
    in val;
    int *res;
    int op;
    // dealing with wrong executions
    if(argc < 2) {
        fprintf(stderr,"usage: %s hostname\n", argv[0]);
        exit(0);
    }

    server = argv[1];
    // client handler
    con=clnt_create(server,RPC_SERVER,CALCULADORA,"udp");
    if(con == NULL) {
        printf("connection with host %s falied\n", server);
        exit(2);
    } 
    while(op >= 0) {
        menu(&op, &val);
        switch(op){
            case(1):
                res = soma_1(&val, con);
                result(res);
                break;
            case(2):
                res = mult_1(&val, con);
                result(res);
                break;
            case(3):
                res = div_1(&val, con);
                result(res);
                break;
            case(4):
                res = max_1(&val, con);
                result(res);
                break;
            case(5):
                res = min_1(&val, con);
                result(res);
                break;
            default:
                op = 6;
                menu(&op, &val);
                break;
        }
    }
}

