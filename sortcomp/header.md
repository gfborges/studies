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
4. Somar os tempos de busca e contar a quantidade de buscas binárias feitas
5. Parar quando o tempo acumulado das búsca binárias + tempo de ordenação for menor que o tempo acumulado de buscas sequenciais
### Tabela dos resultados obitidos
Estes foram os resultados dos testes descritos acima.

#### Tabela de numero de buscas 
<insert-code-here>

#### Tabela de tempo médio de procura 
<insert-code-here>

#### Tabela de desvio padrão do tempo de ordenação
<insert-code-here>








  
