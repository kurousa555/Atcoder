N = int(input())
names = [tuple(input().split()) for _ in range(N)]
# print(names)
for i in range(N):
    s,t = names[i][0],names[i][1]
    s_judge = True
    t_judge = True

    for j in range(i+1,N):
        if s in names[j]:
            # print("s",i,j)
            s_judge = False
        if t  in names[j]:
            t_judge = False
            # print("t",i,j)
    
    if (s_judge == False) and (t_judge == False):
        print("No")
        exit()

print("Yes")
