from collections import defaultdict
N = int(input())
text = defaultdict(set)
for i in range(N):
    a = input()
    if a[0]=="!":
        text[str("".join(list(a)[1:]))].add(a)
    if a[0]!="!":
        text[a].add(a)      

for text in text.items():
    if len(text[1]) == 2:
        print(text[0])
        exit()
print("satisfiable")
