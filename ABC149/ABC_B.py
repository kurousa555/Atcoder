from sys import stdin
A,B,K = map(int,stdin.readline().split())

if A>=K:
    A-=K
elif A<K:
    K-=A
    A = 0
    if B>=K:
        B -= K
    elif B<K:
        B = 0
print(A,B)
# S,T = input().split()
# print("".join((T,S)))
