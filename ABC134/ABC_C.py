import sys
N = int(input())
A =  list(int(sys.stdin.readline()) for _ in range(N))

sortd_A =  set(sorted(A,reverse=True))
if  len(sortd_A) == 1:
    max_num = tuple(sortd_A)[0]
    second_num = tuple(sortd_A)[0]
else:
    max_num = tuple(sortd_A)[0]
    second_num = tuple(sortd_A)[1]


if A.count(max_num) >= 2:
    for i in range(N):
        print(max_num)
else:    
    for i in range(N):
        if A[i] == max_num:
            print(second_num)
        else:
            print(max_num)
        
