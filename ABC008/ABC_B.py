import collections
N  =  int(input())
candi_dict = collections.defaultdict(list)
for _ in range(N):
    name = input()
    candi_dict[name].append(1)

maxi=0
for candi in candi_dict.items():
    if len(candi[1])>maxi:
        maxi=len(candi[1])
        ans =  candi[0]
print(ans)
