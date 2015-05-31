import math
maxn=1000000
maxn1=100000
phi=[0]*(maxn+1)
prime=[0]*(maxn1)
mark=[False]*(maxn+1)

def comp_phi():#o(maxn*loglogn)
    phi[1]=1
    sz=0
    for i in range(2,maxn+1):
        if mark[i]==False:
            phi[i]=i-1
            prime[sz]=i
            sz+=1
        #print(sz)
        for j in range(0,sz):
            if prime[j]*i>maxn:
                break
            mark[prime[j]*i]=1
            if i%prime[j]==0:
                l=0
                x=i
                while x%prime[j]==0:
                    x=math.floor(x/prime[j])
                    l+=1
                m=1
                for k in range(0,l):
                    m*=prime[j]
                phi[i*prime[j]]=phi[x]*m*(prime[j]-1)
                break;
            else:
                phi[i*prime[j]]=phi[i]*(prime[j]-1)

def primes(n):
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if all( d % od != 0 for od in divisors if od != d ) ]

def another(k):
    pr=primes(k)
    if pr.__len__()==0:
        return k-1
    else:
        ph=k
        for x in pr:
            ph=(ph/x)*(x-1)
        return ph


def main():
    comp_phi()
    t=int(input())
    for i in range(0,t):
        k=int(input())
        if k<=maxn:
            print(phi[k])
        else:
            print(int(another(k)))

main()
