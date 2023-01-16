N = int(input())
sec = 0
AB = []
for _ in range(N):
    A,B = map(int,input().split())
    sec += A/B
    AB.append([A,B])
sec /= 2
ans  = 0


for i in range(N):
    A,B = AB[i][0],AB[i][1] 
    if A/B < sec:
        ans += A
        sec -= A/B

    elif A/B >= sec:
        ans += sec*B
        break



print(ans)
