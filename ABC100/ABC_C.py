N = int(input())
A = list(map(int,input().split()))
cnt = 0

while True:
    div_2 = False
    for i in range(len(A)):
        if A[i] != None:
            if A[i]%2 != 0:
                A[i] = None
                cnt += 1
            elif A[i]%2 == 0:
                A[i] //=2
                cnt += 1
                div_2 = True
    if (div_2==False):
        break
print(cnt - N)
