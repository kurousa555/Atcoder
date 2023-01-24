import collections
N = int(input())
S = [input() for _ in range(N)]
S = collections.Counter(S)
# print(S)
print("AC x "+str(S["AC"]))
print("WA x "+str(S["WA"]))
print("TLE x "+str(S["TLE"]))
print("RE x "+str(S["RE"]))
