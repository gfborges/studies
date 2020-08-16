def seq(v, x):
    for i,y in enumerate(v):
        if x  == y:
            return i
    return -1

def bin(v, x):
    length = len(v)
    l,r = 0, length - 1
    while l <= r:
        m = (l + r)//2
        if v[m] == x:
            return m 
        elif v[m] > x:
            r = m - 1
        else:
            l = m + 1
    return -1

def test(f, sort=False, size=10):
    from random import shuffle
    v = list(range(size+1))[:-1]
    shuffle(v)
    error = f"FAILED! {f.__name__} returned an unexpected answer"
    if sort: v.sort()
    for x in range(size+1):
        i = f(v, x)
        if i > 0 and v[i] != x:
            print(error + f"(v[{i}] != {v[i]})")
            return False
        elif i < 0 and x in v:
            print(f"FAIlED! {f.__name__} returned an unexpected answer ({x} is in v)")
            return False
    print(f"OK! {f.__name__} is working properly")
    return True

if __name__ == "__main__":
    test(seq)
    test(bin, sort = True)

