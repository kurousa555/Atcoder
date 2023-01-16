N = int(input())
ST =  [list(input().split()) for _ in range(N)]
ST.sort(reverse=True,key=lambda x:int(x[1]))
print(ST[1][0])
