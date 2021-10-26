def exgcd(p,q):
    if p==0:
        return (q,0,1)
    else:
        (gcd,u,v)=exgcd(q%p,p)
        return (gcd,v-q//p*u,u)

p=26513
q=32321

