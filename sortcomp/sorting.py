from typing import Callable, Iterable
def selection(v: Iterable) -> Iterable:
    """
        default insertion sort
    """
    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v

def insertion(v: Iterable) -> Iterable:
    """
        default selection sort
    """
    for i in range(1, len(v)):
        t = v[i]
        j = i
        while(j > 0 and v[j-1] > t):
            v[j] = v[j-1]
            j -= 1
        v[j] = t
    return v

def insert_bin(v: Iterable) -> Iterable:
    """
        a binary version of insertion sort
    """
    i  = 1
    while(i < len(v)):
        t = v[i]
        l, r = 0 , i-1
        if v[r] > v[i]:
            while(l < r):
                m = l + (r-l) // 2
                if v[m] <= t:
                    l = m + 1
                else:
                    r = m
            v[r+1:i+1] = v[r:i]
            v[r] = t
        else:
            i += 1
    return v

def merge(v1: Iterable, v2: Iterable) -> Iterable:
    m = []
    ls = len(v1)
    rs = len(v2)
    while(ls > 0 and rs > 0 ):
        if(v1[0] < v2[0]):
            m.append(v1.pop(0))
            ls -= 1
        else:
            m.append(v2.pop(0))
            rs -= 1
    if(ls == 0):
        m.extend(v2)
    else:
        m.extend(v1)
    return m

def mergesort(v: Iterable) -> Iterable:
    """
        default mergesort
    """
    mid = len(v) // 2
    if mid == 0:
        return v

    m1 = mergesort(v[:mid])
    m2 = mergesort(v[mid:])
    
    v = merge(m1, m2)
    return v

def mergesort_thread(v:Iterable) -> Iterable:
    pass

def pivot(v: Iterable, p:int) -> (Iterable, int):
    """
        quicksort auxiliar function. Seperates the smaller values
        on the right and the larger values  on the left 
        args:
            v (Iterable): iterable to be separated
            p (int) : position of the pivot
        return:
            v (Iterable) : Iterable with the previous pth value now in place
            l (int) : new position of the previuos pth value
    """
    v[p], v[-1] = v[-1], v[p]
    pv = v[-1]
    l,r = 0, len(v) -1
    while(l < r):
        while(v[l] < pv and l < r):
            l += 1
        while(v[r] >= pv and r > l):
            r -= 1
        v[l], v[r] = v[r], v[l]
    v[l], v[-1] = v[-1], v[l]
    return v, l

def quicksort(v: Iterable) -> Iterable:
    """
        quicksort where the pivot is the median of 
        first, middle and last element

        args:
            v (Iterable) : Iterable of any basic type (int, str, float...)
        return:
            v (Iterable) : sorted Iterable
    """
    if len(v) <= 1:
        return v[:]
    l = [v[0], v[len(v)//2], v[-1]]
    if max(l) != l[0] and min(l) != l[0]:
        p = 0
    elif max(l) != l[1] and min(l) != l[1]:
        p = len(v) // 2
    else:
        p = len(v) - 1
    v, p = pivot(v, p)
    v[:p] = quicksort(v[:p])
    v[p+1:] = quicksort(v[p+1:])
    return v

def sorttest(sort: Callable) -> str:
    from random import randint
    result = ""
    for i in range(5):
        v = [randint(0, 100)  for i in range(10)]
        v = sort(v)
        vs = (v[i-1] <= v[i] for i in range(1, len(v)))
        if all(vs):
            result += "1"
        else:
            result += "0"
    
    if "0" in result:
        print("FALIED!", sort.__name__,"is not working properly")
        print(result)
    else:
        print("OK! Congratulation", sort.__name__, "is working properly")
    return result

if __name__ == "__main__":
    sorttest(mergesort)
    sorttest(quicksort)
    sorttest(selection)
    sorttest(insertion)
    sorttest(insert_bin)

