N = int(input()) 
A = list(map(int,input().split()))
X = int(input())
total = 0
cnt = 0

sumA = sum(A)
block = (X//sumA)
# print(block)

cnt += block*len(A)
total += block*sumA
while True:
    for a in A:
        total += a
        cnt += 1
        # print(total,cnt)
        if total > X:
            print(cnt)
            exit()
