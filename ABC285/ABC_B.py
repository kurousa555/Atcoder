N = int(input())
S = list(input())
for i in range(1,N-1):
    for l in range(N,-1,-1):
        if i+l <= N:
            l_list = []
            cnt = 0
            for k in range(0,l):
                print(S[k],S[k+i])
                if S[k] != S[k+i]:cnt += 1
            print(cnt)
        print("="*10)
