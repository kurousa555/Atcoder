N = int(input())
before = set()
after  = set()
for _ in range(N):
    s,t = input().split()
    before.add(s)
    after.add(t)

for a,b in zip(after,before):
    if (a not in before) and (b not in after):continue
    if a not in before:
        print("Yes")
        exit()
print("No")
