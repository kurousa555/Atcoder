N = int(input())
cnt = 0
for i in range(1,N+1):
    octed = oct(i)[2:]
    if ("7" not in tuple(octed)) and ("7" not in str(i)):
        cnt += 1

print(cnt)
