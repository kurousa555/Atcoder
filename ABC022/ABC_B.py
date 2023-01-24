import collections,math
N = int(input())
A = [int(input()) for _ in range(N)]
A  = collections.Counter(A)
# print(A.items())

# print(A.values())
# more_two = [a[1] for a in A.items() if a[1]>=2]
more_two = [a[1]-1 for a in A.items()]
# print(more_two)
# def nCr(n):
#     return math.factorial(n)//math.factorial(2)//math.factorial(n-2)
# more_two = list(map(nCr,more_two))
print(sum(more_two))
