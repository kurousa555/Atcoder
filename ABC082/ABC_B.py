s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
# print(s,t)
if "".join(s) < "".join(t):
    print("Yes")
else:
    print("No")
