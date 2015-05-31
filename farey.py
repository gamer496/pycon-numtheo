def Farey_r(limit, start=(0, 1), stop=(1, 1)):
    '''recursive definition of a Farey sequence generator'''
    n, d = start
    N, D = stop
    mediant_d = d + D
    if mediant_d <= limit:
        mediant = (n + N), mediant_d
        for pair in Farey_r(limit, start, mediant): yield pair
        for pair in Farey_r(limit, mediant, stop): yield pair
    else:
        yield start


def farey(limit):
    '''Fast computation of Farey sequence as a generator'''
    # n, d is the start fraction n/d (0,1) initially
    # N, D is the stop fraction N/D (1,1) initially
    pend = []
    n = 0
    d = N = D = 1
    while True:
        mediant_d = d + D
        if mediant_d <= limit:
            mediant_n = n + N
            pend.append((mediant_n, mediant_d, N, D))
            N = mediant_n
            D = mediant_d
        else:
            yield n, d
            if pend:
                n, d, N, D = pend.pop()
            else:
                break


def main():
    k=int(input())
    l=farey(k)
    for x in l:
        print x
main()
