N = int(input())
commands = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j  in  range(i+1,N):

        command, l1, r1 = commands[i][0],commands[i][1],commands[i][2]
        # if   command == 1:
        # elif command == 2:list1 = [i for i in range(l,r)]
        # elif command == 3:list1 = [i for i in range(l+1,r+1)]
        # elif command == 4:list1 = [i for i in range(l+1,r)]
        command, l2, r2 = commands[j][0],commands[i][1],commands[i][2]
        if   command == 1:list1 = [i for i in list1 if l<=i<=r]
        # elif command == 2:
        #     if list1[-1] == r:list1 = [i for i in list1 if l<=i<=r]
        #     if list1[-1] != r:list1 = [i for i in list1 if l<=i<r]
        # elif command == 3:
        #     if list1[0] == l:list1 = [i for i in list1 if l<=i<=r]
        #     if list1[0] != l:list1 = [i for i in list1 if l<i<=r]
        # elif command == 4:
        #     if list1[-1] == r:list1 = [i for i in list1 if l<=i<=r]
        #     if list1[-1] != r:list1 = [i for i in list1 if l<=i<r]
        #     if list1[0] == l:list1 = [i for i in list1 if l<=i<=r]
        #     if list1[0] != l:list1 = [i for i in list1 if l<i<=r]

        # print(list1)
        # print("====="*2)
# print(len(list1))
