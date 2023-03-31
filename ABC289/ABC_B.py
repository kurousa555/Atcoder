from sys import stdin
N,M = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
graph = []

# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
 
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
 
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 
 
    def same(self,a,b):
        return self.leader(a) == self.leader(b)
 
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])
 
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

UF = UnionFind(N+1)
# UF.merge(1,2)
for a in A:
    UF.merge(a,a+1)
for g in UF.groups():
    if g != [0]:
        print(*g[::-1],end=" ")
print()
