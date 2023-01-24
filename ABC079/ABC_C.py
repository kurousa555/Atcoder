S =  list(map(int,input()))
for num in range(1<<3):
    op = []
    for shift in range(3):
        if  (num>>shift) & 1  == 1:
            op.append("+")
        elif  (num>>shift) & 1  !=  1:
            op.append("-")
    
    tmp = S[0] 
    # print(S)
    for i in range(3):
        if    op[i]=="+":tmp+=S[i+1]
        elif  op[i]=="-":tmp-=S[i+1]
    if tmp==7:
        ans = [None]*7
        ans[::2]=S
        ans[1::2]=op
        ans = map(str,ans)
        print("".join(ans)+"=7")
        exit()


