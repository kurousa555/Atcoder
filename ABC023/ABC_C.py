N = int(input())
S = list(input())

if len(S)==1:
    if S[0] != "b":
        print(-1)
        exit()
    elif S[0] == "b":
        print(0)
        exit()

center_idx = (N-1)//2
center = S[center_idx]

first = S[:center_idx]
first.reverse()
second = S[center_idx+1:]


if center != "b" or len(S)%2==0 or len(first)!=len(second):
    print(-1)
    exit()

for i in range(center_idx):
    # print(i,(i+1)%3)
    if (i+1)%3 == 1:
        if first[i] != "a" or second[i] != "c":
            print(-1)
            exit()
    if (i+1)%3 == 2:
        if first[i] != "c" or second[i] != "a":
            print(-1)
            exit()
    if (i+1)%3 == 0:
        if first[i] != "b" or second[i] != "b":
            print(-1)
            exit()



if   first[-1] != "a" and second[-1] != "c":print(len(first))
elif first[-1] != "c" and second[-1] != "a":print(len(first))
elif first[-1] != "b" and second[-1] != "b":print(len(first))
else:print(-1)
