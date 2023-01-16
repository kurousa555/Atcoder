def judge():
    N = list(input())
    right=0
    left=0
    reN = N[::-1]

    for r in reN:
        if r=="0":right+=1
        else:break
    for l in N:
        if l=="0":left+=1
        else:break
    #そもそも回文
    if N==reN:return True
    
    #左に0を付与して回文。最初の左0の数が右0の数より多いとダメ
    if right>left:
        newN = N[left:-right]
        if newN == newN[::-1]:return True


    return False
    
print('Yes' if judge() else 'No')
