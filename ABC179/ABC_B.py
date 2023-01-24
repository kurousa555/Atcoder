N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    if  D[i][0]==D[i][1]:D[i].append(True)
    if  D[i][0]!=D[i][1]:D[i].append(False)

for i in range(N-2):
    range_list = D[i:i+3]
    if range_list[0][2]==range_list[1][2]==range_list[2][2]==True:
        print('Yes')
        exit()
print("No")

