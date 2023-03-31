def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())

ans = 0
for X in range(1,N//2+1):
    Y = N-X
    # print(X,Y)
    AB =  make_divisors(X)
    CD = make_divisors(Y)
    # print(AB)
    # print(CD)
    if  X!=Y:ans += len(AB)*len(CD)*2
    else:ans += len(AB)*len(CD)
print(ans)
