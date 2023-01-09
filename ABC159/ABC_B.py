S = input()
N = len(S)
T = (N-1)//2
# print(S)
# print(S[::-1])
print(S[:T])
print(S[T+1:])  
A = S
B = S[::-1]
C = S[:T]
D = S[T+1:]
if A == B and C == D:
  print('Yes')
else:
  print('No')
  