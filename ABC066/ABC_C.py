from sys import stdin
n =  int(input())
A = list(map(int,stdin.readline().split()))

# head=A[1::2]
# tail=A[0::2]
# print(A)
if n%2==1:
    head=A[1::2]
    tail=A[0::2]
    tail.reverse()
    print(*tail+head)
if n%2==0:
    head=A[0::2]
    tail=A[1::2]
    # print(head,tail)
    tail.reverse()
    # print(head)
    print(*tail+head)

# print(head,tail)
# rev = False
# for i in range(n):
#     if i%2==1:rev =  not rev
