from sys import stdin
def func():
    N,M = map(int,stdin.readline().split())
    ans = []
    s_c  = [[] for _ in range(N)]
    for _ in range(M):
        s,c = map(int,stdin.readline().split())
        s_c[s-1].append(c)
    # print(s_c)
    for num  in range(10**(N-1),10**N):
    # for num  in range(110, 112):
        s_num = str(num)
        # print(s_num)
        judge = True
        for i in range(N):
            # print(s_num[i], s_c[i])
            if (int(s_num[i]) in s_c[i]) or len(s_c[i])==0 and len(s_c[0])!=0:
                pass
            else:
                judge = False
                # print(1)
        if  judge == True:ans.append(num)
    # print(ans)
    if len(ans)==0:print(-1)
    else:print(ans[0])
func()
func()
func()
