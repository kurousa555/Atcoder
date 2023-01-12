import string
alphabet = list(string.ascii_lowercase)
P = map(int,input().split())
for p in P:
    print(alphabet[p-1],end="")
print()
