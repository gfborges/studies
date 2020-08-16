#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#define N_THREADS 5

void hello(int tid){
    // printa olá e número da thread 
    printf("hello from thread %d\n", tid);
    // printa número de 0 a 4
    for(int i = 0; i < 5; i++){
        printf("%d\n", i);
    }
    // saindo da thread
    pthread_exit(NULL);
}

int main(int argc, char* argv[]){
    // vetor com as N_THREADS que serão criadas
    pthread_t thrs[N_THREADS];
    // ponteiro para função hello 
    void (* func)(int) = &hello;
    // loop para criar as N_THREADS no vetor thr
    for(int i =0; i < N_THREADS; i++){
        // cria a thread na função hello (func) passado o argumento i
        int status = pthread_create(&thrs[i], NULL,func, i);
        // lidando com erros
        if(status != 0){
            perror("pthread_create");
            exit(1);
        }
    }
}
