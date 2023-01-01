N =  int(input())
originals = set()
point = 0
submiter = None

for i in range(N):
    S,T = tuple(input().split())
    if S not in originals:
        originals.add(S)
        if int(T) > point:
            point = int(T)
            submiter = i+1


print(submiter)
