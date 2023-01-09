N  =  int(input())
cnt = 0

for i in range(1,N+1):
    cnt  += (i/N)*10000
print(int(cnt))

