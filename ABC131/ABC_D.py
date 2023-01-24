N = int(input())
tasks = [list(map(int,input().split())) for _ in range(N)]
tasks.sort(key=lambda  x:x[1])
time = 0
for i in range(N):
    time +=  tasks[i][0]
    if time > tasks[i][1]:
        print("No")
        exit()
print("Yes")
