from sys import stdin
import collections
N,K,Q = map(int,stdin.readline().split())
answers = []
for _ in range(Q):
    answers.append(input())
answers = collections.Counter(answers)
leg_cut = Q-K+1
for i in range(1,N+1):
    # print(leg_cut, answers[str(i)])
    if  answers[str(i)] >=  leg_cut:
        print("Yes")
    else:
        print("No")
# print(answer)
