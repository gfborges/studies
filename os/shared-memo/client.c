#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <stdlib.h>
#define MAX 27

void err(char* s) {
    perror(s);
    exit(1);
}

int main() {
    int shmid;
    char *shm, *s;
    /*
     * chave para acessar memória compartilhada
     * NÃO MUDAR
     * */
    const key_t key = 5678;

    /*
     * Pega o id da memória compartilhada
     * NÃO MUDAR O 0666 !
     * Isso é estabelecido pelo código do servidor
     * */
    if ((shmid = shmget(key, MAX, 0666)) < 0) {
        err("shmget");
    }
    /*
     * Traz a memória para o espaço desse processo
     * */
    if((shm = shmat(shmid, NULL, 0)) == (char *) -1) {
        err("shmat");
    }
    /* 
     * Coloca o alfabeto no espaço compartilhado
     * */
    for(s = shm; *s != '\0'; s++) {
        putchar(*s);
    }
    putchar('\n');
    /*
     * sinal para servidor para terminar de mandar a mensagem
     * */
    *shm = '*';

    exit(0);
}
