N = int(input())
newN = sum(list(map(int,list(str(N)))))

if N%newN==0:
    print("Yes")
else:
    print("No")

