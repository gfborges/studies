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
5000 | 9368 | 7760 | 95 | 126 | 4
10000 | 18411 | 14621 | 85 | 159 | 5
15000 | 26458 | 21163 | 109 | 197 | 4
#### Tabela de tempo médio de procura 
![search-chart](https://raw.githubusercontent.com/gfborges/studies/master/sortcomp/search-chart.png)
N | selection | insertion | quicksort | mergesort | sorted
--- | --- | --- | --- | --- | ---
5000 | 1.843 | 1.497 | 0.021 | 0.03 | 0.001
10000 | 7.449 | 5.983 | 0.041 | 0.069 | 0.002
15000 | 16.752 | 13.287 | 0.065 | 0.124 | 0.003
#### Tabela de desvio padrão do tempo de ordenação
![time-chart](https://raw.githubusercontent.com/gfborges/studies/master/sortcomp/time-chart.png)
N | selection | insertion | quicksort | mergesort | sorted
--- | --- | --- | --- | --- | ---
5000 | 0.013 | 0.012 | 0.004 | 0.003 | 0.0
10000 | 0.041 | 0.033 | 0.002 | 0.001 | 0.0
15000 | 0.188 | 0.041 | 0.005 | 0.002 | 0.0

![stdev-chart](https://raw.githubusercontent.com/gfborges/studies/master/sortcomp/stdev-chart.png)






  
