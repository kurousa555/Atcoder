import itertools
import string
S = list(input())
lenS = len(S)
ans = 0
print(lenS)
for i in range(1,lenS):
    ans +=  (26**i)

alphabet = list(string.ascii_uppercase)
dic = list(itertools.product(alphabet, repeat=len(S)))
ans += dic.index(tuple(S))+1
print(ans)
