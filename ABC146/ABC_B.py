from sys import stdin
N = int(input())
S = list(input())
alph = [chr(i) for i in range(ord("A"),ord("Z")+1)]
# print(len(alph))

for s in S:
    idx_s = ord(s)-ord("A")
    print(alph[(idx_s+N)%26],end="")
    # print(alph[ord(s)%26])
print()
