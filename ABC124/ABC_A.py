A,B = map(int,input().split())
cnt = 0
for _ in range(2):
    if A>=B:
        cnt += A
        A-=1
    elif A<=B:
        cnt += B
        B-=1
        
print(cnt)
