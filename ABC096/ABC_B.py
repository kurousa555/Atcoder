from sys import stdin
ABC = list(map(int,stdin.readline().split()))
N = int(input())
ABC.sort()
ABC[2]=ABC[2]*(2**N)
# print(ABC)
print(sum(ABC))
