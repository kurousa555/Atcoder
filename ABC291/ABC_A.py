from sys import stdin
S = list(input())
for i in range(len(S)):
    if S[i].isupper():
        print(i+1)
