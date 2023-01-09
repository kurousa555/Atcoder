x,y = map(int,input().split())
def func(n):
    if n in (1,3,5,7,8,10,12):n = "A"
    elif n in (4,6,9,11): n = "B"
    else: n = "C"
    return n

if func(x)  == func(y):print("Yes")
else:print("No")
