W,a,b = map(int,input().split())
if a<=b<=a+W or b<=a<=b+W:
    print(0)
else:
    if b>a+W:
        print(b-a-W)
    elif a>b+W:
        print(a-b-W)
