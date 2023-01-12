import math
ABC =  list(map(int,input().split()))
ABC = sorted(ABC)

cnt = 0
if ABC[1]==ABC[2]:
    diff = ABC[2]-ABC[0]
    ABC[0] += math.ceil(diff/2)*2
    cnt += math.ceil(diff/2)
    if len(set(ABC))!=1:cnt+=1

elif ABC[1]!=ABC[2]:
    diif = ABC[2]-ABC[1]
    ABC[1]+=diif
    ABC[0]+=diif
    cnt += diif

    diff = ABC[2]-ABC[0]
    ABC[0] += math.ceil(diff/2)*2
    cnt += math.ceil(diff/2)
    if len(set(ABC))!=1:cnt+=1

print(cnt)
