#include <string.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void swap(int * x, int * y){
    int t = *x;
    *x = *y;
    *y = t;
}

void printv(int *v,int size){
    for(int i = 0; i < size; ++i){
        if(i > 0){
            printf(" ");
        }
        printf("%d", v[i]);
    }
    printf("\n");
}

void selection(int * v, int size){
    // também conenhcico como bubblesort
    // a cada iteração procura o menor valor trocando
    // com sempre com um menor  
    for(int i = 0; i< size; ++i){
        for(int j = i + 1; j< size; ++j){
            if(v[i] > v[j]){
                swap(&v[i], &v[j]);
            }
        }
    }
}


int pivot(int * v, int start, int end, int p) {
    // muda o p com o último valor e grava o valor de v[p]
    swap(&v[p], &v[end]);
    p = end;
    int pv = v[p];
    // itera sobre as duas pontas procurando valores
    // que deveriam estar na outra ponta
    // valores MAIORES que deveriam estar a DIREITA
    // valores MENORES que deveriam estar a ESQUERDA
    int l = start, r = end;
    while(l< r){
        // procura por valores maiores a esquerda
        while(v[l] < pv && l < r){
            l++;
        }
        // procura por valores menores a direita
        while(v[r] >= pv && r > l){
            r--;
        }
        // troca os dois valores de posição
        swap(&v[l], &v[r]);
    }
    // troca o valor p para o seu lugar
    //  na frente de todos menores e atrás de todos os maiores
    swap(&v[l], &v[p]);
    return l;
}

void quicksort(int *v, int start, int end) {
    // para quando o subvetor quando for 1 (já está ordenado)
    if((end - start) <= 1){
        return;
    }
    // seleciona e mediana entre o primeiro, ultimo e valor do meio
    int mid = (end - start) / 2;
    int p;
    if( (v[mid] < v[start]) == (v[start] <= v[end]) ) {
        p = start;
    } else if( (v[start] <= v[mid]) == (v[mid] < v[end]) ) {
        p = mid;
    } else {
        p = end;
    }
    // função que insere p no lugar correto
    // separando os valores que são menores que ele dose que são maiores
    p = pivot(v, start, end, p);
    // ordena os valores menores e maiores que p
    quicksort(v, start, p - 1);
    quicksort(v, p + 1, end );

}


void merge(int *v1, int *v2, int s1, int s2, int * t){
    int i = 0, j = 0, k = 0;
    // une dois vetores v1 e v2 (ordenados) em um vetor t também ordenado
    // itera por enquanto que as o dois vetores não estão "vazios"
    while(i < s1 && j < s2){
        if(v1[i] < v2[j]){
            t[k++] = v1[i++];
        } else {
            t[k++] = v2[j++];
        }
    }
    // adiciona o restante
    if(i < s1){
        memcpy(&t[k], &v1[i],(s1-i) * sizeof(int)); 
    } else {
        memcpy(&t[k], &v2[j],(s2-j) * sizeof(int));
    }
}

void mergesort(int *v, int start, int end){
    // para quando estive ordenado
    // tamanho == 1
    int size = end - start;
    if((size) <= 0) {
        return;
    }
    // calcula a metade do vetor e seus tamanhos
    int mid = start + size / 2;
    int s1 = mid-start + 1;
    int s2 = end - mid;
    // chama o mergesort para as duas metades
    mergesort(v, start, mid);
    mergesort(v, mid+1, end);
    // cria um vetor auxiliar e une os dois vetores ordenados
    int t[s1+s2];
    merge(&v[start], &v[mid+1], s1, s2, t);
    // copia o valores do vetor auxilar (ordenados) para o vetor de fato
    memcpy(&v[start], t, (s1+s2) * sizeof(int));

}

void insertion(int * v, int size) {
    // itera sobre o vetor v
    for(int i = 1; i < size; ++i) {
        // se estiver em ordem adiona
        //  se não procura a posição correta e adiona
        if(v[i-1] > v[i]){
            // procura por sucessor e copia v[i]
            int t = v[i], j = 0 , s = i;
            while(v[j] < v[i]){
                j++;
                s--;       
            }
            // empurra os valores do vetor apartir
            // de onde será inserido t 1 casa
            memcpy(&v[j+1], &v[j], s * sizeof(int));
            // insere o valor de v[i] no lugar correto
            v[j] = t;
        }
    }
}

// ESTÁ UM LIXO, LENTO DEMAIS. MAS FUNCIONA 
void heapfy(int *v, int start, int end, int left, int right) {
    // condição para evitar segfault
    if(left >= start  && right <= end) {
        // loop de 2 em 2 comparando com o do lado
        for(int i = right; i > left; i-=2) {
            // pai do nó atual
            int p = (i - (2-i%2))/2;
            // irmão do nó atual
            int sib = 2*p + (1 + i%2);
            // seleciona o maior irmão
            int x = i;
            // evita segfault
            if(sib > start && sib <= end) {
                if(v[sib] > v[i]) {
                    x = sib;
                }
            }
            // compara o maior irmão com o pai
            if(p >= start && p < end){
                // troca se for necessario
                if(v[x] > v[p]){
                    swap(&v[p], &v[x]);
                    // 2 filho do no atual
                    int y = 2*y + 2;
                    y = (end < y)? end: y;
                    // compara os filho e seleciona o maior 
                    // condições para evitar segfault
                    int x1 = 0;
                    if(2*x + 1 <= end){
                        int x1 = 2*x + 1;
                    }
                    if(2*x + 2 <= end){
                        x1 = (v[x1] > v[2*x+2])? x1 : 2*x + 2;
                    }
                    // chama heapfy de novo só se o filho for menor que o pai
                    if(x1 > 0 && v[x] < v[x1]) {
                        heapfy(v, start, end, x, y);
                    }
                }
            }
        }
    }
}

void heapsort(int *v, int start, int end) {
    for(; end > start; end--) {
        heapfy(v,start, end,start, end);
        swap(&v[start], &v[end]);
    }
}


void insert_bin(int * v, int size) {
    // itera o vetor
    // começa de 1 porque o elemento 0 já está ordenado
    for(int i  = 1; i < size; ++i) {
        // se o próximo estiver em ordem simplismente adiciona
        // se não procura o seu lugar e adiciona ele
        if(v[i-1] > v[i]){
            // copia o valor do que vai ser inserido
            int t = v[i];
            int l = 0, r = i-1, m = 0;
            // busca binária por succesor na parte ordenada
            while(l < r){
                m = l + (r-l) / 2;
                if(v[m] <= t){
                    l =  m + 1;
                } else {
                    r = m;
                }
            }
            // empurra a partir do indice onde t será inserido 1 casa
            memcpy(&v[r+1], &v[r], (i-r)*sizeof(int));
            // insere i
            v[r] = t;
        }
    }
}
int issorted(int v[], int size){
    for(int i = 1; i < size; i++){
        if(v[i-1] > v[i]){
            return 0;
        }
    }
    return 1;
}

int main() {
    srand(time(NULL));
    int v[10000];
    for(int i = 0; i < 10000; i++){
        v[i] = rand() % 101;
    }
    clock_t tc = clock();
    mergesort(v, 0, 9999);
    tc = clock() - tc;
    double t = (double) tc / CLOCKS_PER_SEC;
    t *= 1000;
    printf("%d %lf\n", issorted(v, 10000), t);

}
