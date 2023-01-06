N = int(input())

cnt = 0
for i in range(1,N+1):
    X = [j for j in range(1,i+1) if i % j == 0]
    if i%2==1  and len(X) == 8:
        cnt += 1
print(cnt)
