N,S,D = map(int,input().split())
ans = 0
for _ in range(N):
    x,y = map(int,input().split())
    if x<S  and y>D:
        print("Yes")
        exit()
print("No")
