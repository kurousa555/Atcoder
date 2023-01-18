N = int(input())
S = list(input())
first = S[:N]
second = S[N:]
Q = int(input())
# print(first,second)
for _ in range(Q):
    T,A,B = map(int,input().split())
    if T==1:
        if A<=N and B<=N:
            first[A-1],first[B-1] = first[B-1],first[A-1]
        if A<=N and B>N:
            first[A-1],second[(B)%N-1] = second[(B)%N-1],first[A-1]    
        if A>N and B<=N:
            first[(A)%N-1],second[B-1] = second[B-1],first[(A)%N-1]    
        if A>N and B>N:
            second[(A)%N-1],second[(B)%N-1] = second[(B)%N-1],second[(A)%N-1]    
    if T==2:
        first,second = second,first
    # print(T,first,second,A,B)
print("".join(first)+"".join(second))
