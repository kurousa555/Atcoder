def judge(): 
    import math
    P = int(input())
    cnt = 0
    for i in range(int(math.sqrt(P)),0,-1):
        if math.factorial(i) <= P:
            div = P//math.factorial(i)
            P -= div*math.factorial(i)
            cnt += div
    return cnt

print(judge())
