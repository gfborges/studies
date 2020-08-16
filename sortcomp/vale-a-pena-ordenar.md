# Vale a pena ordenar ?
---
## Gabriel Fr. Borges - FATEC SJC - Estrutura de Dados - Fernando Masanori

Este trabalho tem o objetivo de comparar diferentes algoritimos de ordenação. O método utilizado foi contar quantas buscas binárias são nessecesárias para que valha a pena ordernar o vetor e fazer buscas binárias ao invés de buscas sequenciais. Os algoritmos selecionado foram:
* Insersão
* Seleção
* Quicksort
* Mergesort
* Timsort(nativo do python)
_Para detalhes de implementação veja o [código fonte utilizado](https://github.com/gfborges/studies/tree/master/sortcomp)_
---
### Detalhes de implementação
1. Gerar uma lista aletória de tamanho N (com números de 0 até n-1)
2. Cronometrar o tempo de ordenação da lista
  * Cronometrar 3 execuções
  * Ordenar um cópia da lista em cada execução
  * Devolver a média das 3 execuções
3. Cronometrar buscas de um número aleatório na lista
  * Número aleatório entre 0 e N inclusive
  * Busca sequencial _(O(n))_
  * Busca binária _(O(log n))_
  * O tempo de búsca também é uma média de 3 execuções
4. Somar os tempos de busca e contar a quantidade de buscas binárias feitas
5. Parar quando o tempo acumulado das búsca binárias + tempo de ordenação for menor que o tempo acumulado de buscas sequenciais
### Tabela dos resultados obitidos
Estes foram os resultados dos testes descritos acima.

#### Tabela de numero de buscas 
N | selection | insertion | quicksort | mergesort | sorted
--- | --- | --- | --- | --- | ---
5000 | 9594 | 7309 | 96 | 123 | 8
10000 | 18266 | 13815 | 89 | 155 | 6
15000 | 26589 | 20588 | 104 | 205 | 6
#### Tabela de tempo médio de procura 
N | selection | insertion | quicksort | mergesort | sorted
--- | --- | --- | --- | --- | ---
5000 | 1.88 | 1.479 | 0.02 | 0.029 | 0.001
10000 | 7.44 | 5.836 | 0.04 | 0.07 | 0.002
15000 | 17.028 | 13.12 | 0.064 | 0.13 | 0.003
#### Tabela de desvio padrão do tempo de ordenação
N | selection | insertion | quicksort | mergesort | sorted
--- | --- | --- | --- | --- | ---
5000 | 0.033 | 0.018 | 0.001 | 0.002 | 0.001
10000 | 0.078 | 0.043 | 0.001 | 0.003 | 0.0
15000 | 0.304 | 0.067 | 0.004 | 0.006 | 0.0







  
