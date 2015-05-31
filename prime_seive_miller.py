#seive of erastosthenes
from math import sqrt
from random import randint
max_eras=10000000
comp=[False]*max_eras

def eras():
    comp[1]=False
    for i in range(2,int(sqrt(max_eras))):
        if comp[i]==True:
            continue
        for j in range(i*2,max_eras,i):
            comp[j]=True


def miller_rabin(p):
    for k in range(0,3):
        a=randint(1,p-1)
        h=pow(a,p-1,p)
        if h!=1:
            print("Composite")
            break
        else:
            print("Prime")

def main():
    eras()
    print("done")
    t=int(input())
    for i in range(0,t):
        k=int(input())
        if k>=max_eras:
            miller_rabin(k)
        else:
            if comp[k]==True:
                print("Composite")
            else:
                print("Prime")

main()
