N = int(input())
H = list(map(int,input().split()))
H_list = []

init = 0

for i in range(N-1):
    if H[i] < H[i+1]:
        H_list.append(H[init:i+1])
        init = i+1
else:
    H_list.append(H[init:])
# print(H_list)
H_list = list(map(len,H_list))
print(max(H_list)-1)
