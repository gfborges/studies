#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX 27

void err(char* s) {
    /*
     * Função para lidar com erros 
     * */
    perror(s);
    exit(1);
}

void send_msg(char* s){
    char* shm = s;
    /*
     * Manda mensgens para a posição compartilhada na memória
     * */
    for(char c = 'a'; c <= 'z'; c++){
        *s++ = c;
    }
    while(*shm != '*'){
        sleep(1);
    }
}

int main(){
    int shmid;
    char *shm;
    /*
     * chave comunicação entre os processos
     * */
    key_t key = 5678;
    /*
     * shmget: id da memória que será criada de tamanho MAX
     * a flag IPC_CREAT especifíca a crição
     * ver: man shmget
     * */

    if((shmid = shmget(key, MAX, IPC_CREAT | 0666)) < 0) {
        err("shmget");
    }
    /*
     * Traz o segmento de memória para o espaço do processo 
     * ver: man shmat
     * */
    if((shm = shmat(shmid, NULL, 0)) == (char*) -1) {
        err("shmat");
    }

    /*
     * loop eterno para colocar o alfabeto no 
     * segmento de meória compartilhada
     * 
     * */
    while(1) {
        *shm = 'a';
        send_msg(shm);
    }

}
