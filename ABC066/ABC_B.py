S =  list(input())
# print(S)
for i in range(len(S)):
    if len(S)%2==0:
        first  = S[:len(S)//2]
        second  = S[len(S)//2:]
        # print(first,second)
        if first==second:
            if i!=0:
                print(len(S))
                break
    del S[-1]
    # print(S)
