yobi = tuple(["MON","TUE","WED","THU","FRI","SAT","SUN"])
X = input()
if X == "SUN":print(7)
else:print(6 - yobi.index(X))
