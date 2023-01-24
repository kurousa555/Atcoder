N,K = map(int,input().split())
H = list(map(int,input().split()))
newH = [h for h in H if h>=K]
print(len(newH))
