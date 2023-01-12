A,B= map(int,input().split())
res = (A**2-B**2)/(2*A-2*B)
if res.is_integer():
    print(int(res))
else:print("IMPOSSIBLE")
