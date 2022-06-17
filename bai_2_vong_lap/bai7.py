def songuyento(n) :
    f = 1
    if (n <2):
        f = 0
        return f 
    for p in range(2, n):
        if n % p == 0:
            f = 0
            break
    return f