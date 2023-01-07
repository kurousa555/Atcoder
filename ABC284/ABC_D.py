import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

T = int(input())
for i in range(T):
    num = int(input())
    pf = prime_factorize(num)
    pf = collections.Counter(pf)
    q = [k for k, v in pf.items() if v == 2]
    p = [k for k, v in pf.items() if v == 1]
    print(*q,*p)
