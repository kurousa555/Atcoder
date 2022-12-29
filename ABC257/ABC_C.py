from collections import Counter
N = int(input())
S = list(input())
W = list(map(int,input().split()))
S_W =  tuple(zip(S,W))
minors = [s_w for s_w in S_W if s_w[0]=="0"] 
minors_max = max(minors)[1]
children = [s_w for s_w in S_W if s_w[1] <= minors_max] 
adult = [s_w for s_w in S_W if s_w[1] > minors_max] 


print(Counter(children))
print(Counter(adult))
