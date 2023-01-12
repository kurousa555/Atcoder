import collections
N = int(input())
node = []
for i in range(N-1):
    a,b = map(int,input().split())
    node.append(a)
    node.append(b)
node_count  = collections.Counter(node)
node_count = sorted(node_count.items(), key=lambda x:x[1])
if  node_count[-1][1] == N-1:
    print("Yes")
else:
    print("No")
print(284-111)

