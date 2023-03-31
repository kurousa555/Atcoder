S =  input()
Q = int(input())

reverse = False
for i in range(Q):
    query = tuple(input().split())
    if len(query)==1:
        if reverse==True:reverse=False
        elif reverse==False:reverse=True

    else:
        if reverse==True:
            if query[1]=="1":
                S = query[2]+S
            elif query[1]=="2":   
                S = S+query[2]

        elif reverse==False:
            if query[1]=="1":
                S = S+query[2]
            elif query[1]=="2":    
                S = query[2]+S                

    # print(S)
if reverse==False:
    for i in range(len(S)-1,-1,-1):
        print(S[i],end="")
if reverse==True:
    for s in S:
        print(s,end="")
print()
