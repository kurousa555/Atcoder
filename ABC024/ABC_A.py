A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
total = A*S + B*T
if (S+T)>=K:dis = C*(S+T)
else:dis=0
print(total-dis)
