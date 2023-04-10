# from sys import stdin
# def func():
#     N,M = map(int,stdin.readline().split())
#     quest = []
#     putting = []
#     ans = 0

#     for _ in range(M):
#         a,b = map(int,stdin.readline().split())
#         quest.append([a,b])

#     K = int(input())
#     for _ in range(K):
#         c,d = map(int,stdin.readline().split())
#         putting.append([c,d])

#     for num  in  range(2**K):
#         put = []
#         tmp_ans = 0
#         for shift in range(K):
#             if num>>shift & 1 == 1:
#                 put.append(putting[shift][0])
#             else:
#                 put.append(putting[shift][1])

#         for i in range(M):
#             a,b  = quest[i][0],quest[i][1]
#             # print(put,a,b)
#             if a in put and b in put:tmp_ans+=1
            
#         ans = max(ans,tmp_ans)
#     print(ans)
#     return
# func()
import itertools
N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0
for balls in itertools.product(*choice):
    balls = set(balls)
    cnt = sum([A in balls and B in balls for A,B in cond])
    ans = max(ans,cnt)
print(ans)
