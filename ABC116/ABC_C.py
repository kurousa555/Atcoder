from sys import stdin
import collections
def func():
    N = int(input())
    H = list(map(int,stdin.readline().split()))
    que = collections.deque()
    que.append(H)
    while len(que)!=0:
        nxt =  que.popleft()
        if len(list(set(nxt)))==0:continue
        print(que,nxt)
        ans = 0
        start = 0
        for end in range(N):
            print(start,end,nxt)
            if nxt[end] == 0:que.append(nxt[start:end+1])
        else:que.append([num-1 for num in nxt[start:end+1]])

        print(que,len(que))
    
    print()
    return
func()
