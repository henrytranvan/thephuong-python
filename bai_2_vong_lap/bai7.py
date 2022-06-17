#tra lai 1 neu la so nguyen to con 0 thi khpong phai so nguyen to
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