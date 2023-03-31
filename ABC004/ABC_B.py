C = [list(input().split()) for _ in range(4)]
for i in range(3,-1,-1):

    tmp = list(reversed(C[i]))
    print(*tmp)

# print(C)
