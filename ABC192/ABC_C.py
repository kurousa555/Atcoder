N,K = map(int,input().split())
N = list(str(N))
# print(N)
for _  in range(K):
    g1 = int("".join(sorted(N,reverse=True,key=lambda x:int(x))))
    g2 = int("".join(sorted(N,key=lambda x:int(x))))
    N = list(str(g1-g2))
print("".join(N))
