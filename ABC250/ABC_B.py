from sys import stdin
def func():
    N,A,B = map(int,stdin.readline().split())
    first = []
    second=[]
    for i in range(N):
        if i%2==0:
            first.append("."*B)
            second.append("#"*B)
        elif i%2==1:
            first.append("#"*B)
            second.append("."*B)

    judge=True
    for i in range(1,A*N+1):
        if judge==True:
            print("".join(first))
        if judge==False:
            print("".join(second))
        if i%A==0:judge=not judge

    # print(first)
func()
# func()
# func()
