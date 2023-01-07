a,b = map(int,input().split())
if a not in (1,10):
    if ((a+1) == b) or ((a-1) == b):
        print("Yes")
        exit()
if a == 1: 
    if b in (2,10):
        print("Yes")
        exit()
if a == 10:
    if b  in (1,9):
        print("Yes")
        exit()
print("No")
