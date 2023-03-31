from sys import stdin
def judge():
    N,M = map(int,stdin.readline().split())
    A = list(map(int,stdin.readline().split()))
    condi = sum(A)/4/M
    ans = 0
    for a  in A:
        if a>=condi:ans+=1
    if ans >= M:print("Yes")
    else:print("No")

judge()
# judge()
# judge()
