import math
X = int(input())
ans = 1
for num in range(X):
    for exp in range(2,10):
        if num**exp > X:break
        ans = max(ans,num**exp)
        # print(num,exp)
print(ans)
