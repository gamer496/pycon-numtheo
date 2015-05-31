#power exponentation method for calculating fib numbers in logn
#note that I have further optimized to the point that this function
#has become unreadable so remember to make it readable before showing it

import timeit

fibs={0:0,1:1}
def fib(n):
    if n in fibs:
        return fibs[n]
    if n%2==0:
        fibs[n]=((2*fib((n/2)-1))+fib(n/2))*fib(n/2)
        return fibs[n]
    else:
        fibs[n]=(fib((n-1)/2)**2)+(fib((n+1)/2)**2)
        return fibs[n]

def main():
    t=int(input())
    for i in range(0,t):
        k=int(input())
        start=timeit.default_timer()
        print str(fib(k)).__len__()
        stop=timeit.default_timer()
        print (stop-start)

main()
