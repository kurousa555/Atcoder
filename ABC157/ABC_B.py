from sys import stdin
A = [list(stdin.readline().split()) for _ in range(3)]
# print(A)
N  = int(input())
for _  in range(N):
    b = input()
    for i in range(3):
        for  j in range(3):
            if A[i][j]==b:A[i][j]=True




for i in range(3):
    
    if A[i]==[True]*3:
        # print(1)
        print("Yes")
        exit()

    ver = [a[i] for a in A]
    if ver==[True]*3:
        print("Yes")
        exit()

diag1 = [A[0][0],A[1][1],A[2][2]]
diag2 = [A[0][2],A[1][1],A[2][0]]

if diag1==[True]*3 or diag2==[True]*3:
    print("Yes")
    exit()


print("No")
