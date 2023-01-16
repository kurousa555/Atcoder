def judge():
    if S == T:  
        return True

    N = len(S)

    for i in range(N - 1):
        L = list(S)  
        L[i], L[i + 1] = L[i + 1], L[i] 
        print(L[i], L[i + 1])
        print(L)
        S2 = ''.join(L)
        if S2 == T:
            return True
    return False


S = input()
T = input()
print('Yes' if judge() else 'No')
