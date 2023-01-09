N = int(input())
A = list(map(int,input().split()))
new_A = []
for i, a in enumerate(A):
    new_A.append((i,a))

new_A =  sorted(new_A,reverse=True,key=lambda x:x[1])
print(new_A[1][0]+1)
