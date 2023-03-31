import collections
import  difflib
S = tuple(input())
T = tuple(input())
que1 = collections.deque()
que2 = collections.deque()

for i in range(-len(T),0):
    que1.append([S[i],False])

rigth_false=0
for i in range(len(T)):
    if que1[i][0] == T[i]:que1[i][1]=True
    else if que1[i][0] == "?" or T[i] == "?":que1[i][1]=True
    else rigth_false+=1

for i in range(len(T)):
    que1.pop()
    que2.append([S[i],False])
    if que2[]

