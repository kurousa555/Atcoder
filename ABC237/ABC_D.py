N = int(input())
S =  tuple(input())
left,center,right=[],0,[]

for i  in range(N):
    if S[i]=="R":
        left.append(center)
    elif S[i]=="L":
        right.append(center)
    
    center = i+1
print(*left,center,*list(reversed(right)))
    
