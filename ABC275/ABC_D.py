

N =  int(input())
from functools import lru_cache
@lru_cache()
def func(n):
    if n==0:
        return 1
    else:
        return func(n//2)+func(n//3)

print(func(N))
