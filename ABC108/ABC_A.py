K = int(input())
cnt = 0
for i in range(1,K+1):
    for  j in range(i+1,K+1):
        if (i%2==0 and j%2==1) or (i%2==1 and j%2==0):
            cnt += 1
print(cnt)
