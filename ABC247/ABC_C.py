def func(n):
    if n==1:
        return [1]
    return func(n-1) + [n] + func(n-1)
N =  int(input())
print(*list(func(N)))
