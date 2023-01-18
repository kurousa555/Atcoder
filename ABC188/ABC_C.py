N = int(input())
A = list(map(int,input().split()))
newA = []
for i in range(2**N):
    newA.append([A[i],True,i+1])

if len(newA)==2:
    newA.sort(key=lambda x:x[0])
    print(newA[0][2])
    exit()

for _ in range(N):
    for i in range(0,len(newA),2):
        if newA[i][0] > newA[i+1][0]:newA[i+1][1]=False
        elif newA[i][0] < newA[i+1][0]:newA[i][1]=False
    newA = [a for a in newA if a[1]==True]

    if len(newA)==2:
        newA.sort(key=lambda x:x[0])
        print(newA[0][2])
        exit()
