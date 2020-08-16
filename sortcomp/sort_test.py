#!/usr/bin/python3 -tt
import sorting
import pandas as pd
from copy import deepcopy
from searches import bin, seq
from typing import Callable
from random import shuffle, randint
from time import time

ALGS=[sorting.selection, sorting.insertion, sorting.quicksort, sorting.mergesort, sorted]
def names(algs):
	return list(map(lambda x: x.__name__, ALGS))

def rand_list(n:int) -> list:
    """
    
    Generate a random list of numbers from 0 to n-1 
    Example:
    >>> rand_list(6)
    [5,4,2,3,0,1]

    """
    v = list(range(n))
    shuffle(v)
    return v

def timeit(f:Callable, args:list) -> (float, float):
    """
    
    Time the execution of a function
    
    args:
    f:Callable    function to be exetuted
    args:list     function arguments
    
    return: (avg, s)
    t:float       time of the N executions

    Example:
    >>> v = [5,4,2,3,0,1]
    >>> timeit(sorted, [v])
    3.334e-06

    """
    t = time()
    f(*args)
    return time() - t

def test(alg:Callable, v: list, N: int)-> (float, int):
    """
    
    Test the binary and sequential search using the given sort algorhitm

    args:
    alg:Callable        sort function
    v:list              list to be sorted and searched
    N:int		number of times to run timeit function 
    
    return: (n, talg, salg)
    talg: float         time of execution of alg(v) (see args)
    salg: float			std. deviation of all N run of alg(v)
    n:int               number of searches requiered to use binary
                        search instead of sequencial

    Example:
    >>> test(sorted, rand_list(100))
    (2.1457, 12)

    """
    print(f"sorting list of {len(v)} numbers with {alg.__name__}")
    vs = v.copy()
    runs = [timeit(alg, [v.copy()]) for i in range(N)]
    talg = sum(runs) / N
    salg = sum([(r - talg)**2 for r in runs])**0.5
    vb = sorted(v.copy())
    tb = talg
    ts = 0
    n = 0
    print("counting searches")
    # count the necessary number of searches to
    # it takes to worth using binary search
    while ts < tb:
        x = randint(0, len(v))
        ts += timeit(seq, [vs, x])
        tb += timeit(bin, [vb, x])
        n  += 1
    return (n, talg, salg)

def compare(n: int, algs: list=ALGS, N: int = 1):
    """
    
    Executes test for all fuction in test and returns the results
    
    args:
    n:int              	size of the list generated
    algs:list          	list of functions to execute(default in the varible ALGS)
    N:int				how many times to run the test

    return:
    result<(n, t, s)> 	list of tuples returned by test
    n:int         		number of search
    t:float            	avg. time of execution
    s:float				std. deviation of each search
    
    Example:
    >>> import sorting
    >>> algs = [sorting.insert_bin, sorting.insertion]
    >>> compare(5000, algs=algs)
    [(0.10381, , 483), (1.4772, 7110)]

    """
    result = []
    v = rand_list(n)
    for alg in algs:
        r = test(alg, v, N)
        result.append(r)
    return result

def comparison_table(info=0, algs=ALGS, N=1, limit=30, start=5000, increment=5000):
    t = 0
    n = start
    algs_name = names(algs)
    table = [pd.DataFrame(columns = algs_name) for i in range(3)]
    while t <= limit:
        print(f"calculating {n}")
        result = compare(n, algs=algs, N=N)
        rounder = lambda x: round(x, 3)
        result = list(map(lambda r: [rounder(x) for x in r], result))
        for i in range(3):
            row = [r[i] for r in result]
            table[i].loc[n] = row
        t = sum([r[1] for r in result])
        n += increment
    return table[info] if info < 3 else table

if __name__ == "__main__":
    print(*ALGS_NAMES, sep="\t\t")
    t = 0
    n = 5000
    while t <= 30:
        result = compare(n, N= 3)
        round_result = lambda r: (round(r[0], 2), round(r[1], 2), r[2])
        result = list(map(round_result, result))
        t = sum([r[0] for r in result])
        print(*result, sep="\t")
        n += 5000

