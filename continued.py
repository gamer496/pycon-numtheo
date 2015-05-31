def contfrac(p, q):
    while q:
        n = p // q
        yield n
        q, p = p - q*n, q

i=int(input())
j=int(input())
print list(contfrac(i,j))
