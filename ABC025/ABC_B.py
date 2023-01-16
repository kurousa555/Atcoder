N,A,B = map(int,input().split())
ans = 0
for _ in range(N):
    s,t = input().split()
    t = int(t)
    if s=="East":
        if A<=t<=B:ans+=t
        elif t>B:ans+=B
        elif t<A:ans+=A
    elif s=="West":
        if A<=t<=B:ans-=t
        elif t>B:ans-=B
        elif t<A:ans-=A

if ans>0:print("East",abs(ans))
elif ans<0:print("West",abs(ans))
elif ans==0:print(0)
