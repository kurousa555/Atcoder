N =  int(input())
if len(set(list(map(int,input().split())))) == N:
    print("YES")
else:
    print("NO")
