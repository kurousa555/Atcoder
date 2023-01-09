A,B = input().split()
S,T = map(int,input().split())
U = input()
if U==A:
    print(S-1,T)
if U==B:
    print(S,T-1)
