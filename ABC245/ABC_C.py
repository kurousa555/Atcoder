
# #解説AC
# #入力
# N,K = list(map(int,input().split()))
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# #DP
# dp = [True]+[False]*(N-1)
# ep = [True]+[False]*(N-1)
# print(dp)
# print(ep)

# #初期値
# #if abs(A[0]-A[1])<=K or abs(A[0]-B[1])<=K:
# #  dp[0] = True
# #if abs(B[0]-A[1])<=K or abs(B[0]-B[1])<=K:
# #  ep[0] = True
  
# #遷移
# for i in range(N-1):
#   if not dp[i] and not ep[i]:
#     break
#   if dp[i]:
#     if abs(A[i+1]-A[i])<=K:
#       dp[i+1]=True
#     if abs(B[i+1]-A[i])<=K:
#       ep[i+1]=True 
      
#   if ep[i]:
#     if abs(A[i+1]-B[i])<=K:
#       dp[i+1]=True
#     if abs(B[i+1]-B[i])<=K:
#       ep[i+1]=True

# print('Yes') if dp[N-1] or ep[N-1] else print('No')
