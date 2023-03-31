N,K  = map(int,input().split())
H = list(map(int,input().split()))

if K>=N:
    print(0)
    exit()

H.sort(reverse=True)
# print(H,K)
newH = H[K:]
print(sum(newH))
