from sys import stdin
def func():
    S = list(input())
    pos = [[],[],[],[],[]]#K,Q,R,B,N
    for i in range(8):
        if S[i] == "K":pos[0].append(i+1)
        if S[i] == "Q":pos[1].append(i+1)
        if S[i] == "R":pos[2].append(i+1)
        if S[i] == "B":pos[3].append(i+1)
        if S[i] == "N":pos[4].append(i+1)
    if (pos[3][0]%2==0 and pos[3][1]%2==1) or (pos[3][0]%2==1 and pos[3][1]%2==0):
        if pos[2][0] < pos[0][0] < pos[2][1]:
            print("Yes")
            exit()
    print("No")

    # print(pos)  
    # print()
    return
func()
