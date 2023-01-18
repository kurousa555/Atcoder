import math
N,K = map(int,input().split())
A = list(map(int,input().split()))
print(math.ceil((N-1)/(K-1)))
# min_idx = A.index(min(A))
# first = len(A[:min_idx])
# second = len(A[min_idx+1:])
# if second//(K-1)==0 and first//(K-1)==0:pass
# elif second//(K-1)==0:first -= second%(K-1)
# elif first//(K-1)==0:second -= first%(K-1)
# print(math.ceil(first/(K-1)) + math.ceil(second/(K-1)))

