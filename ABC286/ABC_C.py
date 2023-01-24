def func():
    import copy
    N,A,B = map(int,input().split())
    S = list(input())

    ans  = float("inf")
    for i in range(1,N+1):
        if i==1:tmp = S.copy()
        tmp.append(tmp[0])
        del tmp[0]
        cnt = 0
        # print(tmp,i%N)
        for j in range(N//2):
            if tmp[j] != tmp[-1-j]:cnt+=1
            # print(S[j])
            # print(S[-1-j])
            # print(S[j] != S[-1-j])
        # print((A*(i%N))+cnt*B)
        # print(cnt,A*(i%N),i%N)
        ans = min(ans, (A*(i%N))+cnt*B)
        # print("="*30)
    print(ans)
func()
