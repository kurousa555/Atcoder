from sys import stdin
def func():
    mod = 1000000007
    S = list(input())
    dp = [0]*9
    # dp = [0]*len(S)
    for s in S:
        if s  == "c":dp[1]+=1
        if s  == "h":dp[2] += dp[1]%mod
        if s  == "o":dp[3] += dp[2]%mod
        if s  == "k":dp[4] += dp[3]%mod
        if s  == "u":dp[5] += dp[4]%mod
        if s  == "d":dp[6] += dp[5]%mod
        if s  == "a":dp[7] += dp[6]%mod
        if s  == "i":dp[8] += dp[7]%mod
        # print(dp)
    return dp[-1]%mod
print(func())
# print(func())
