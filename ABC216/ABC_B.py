N = int(input())
names = tuple(tuple(input().split()) for _ in range(N))

if len(names) !=  len(set(names)):
    print("Yes")
else:
    print("No")
