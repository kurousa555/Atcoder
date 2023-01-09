N,K = map(int,input().split())
result = [N]
# while True:
for _ in range(10):
    res = abs(N-K)
    print(res,result,N,K)
    if res > result[-1]:
        print(result[-1])
        break
    result.append(res)
    N = K
    K = res
    

    
    

