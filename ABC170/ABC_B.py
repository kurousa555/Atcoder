from sys import stdin
def func():
    X,Y = map(int,stdin.readline().split())
    if  Y%2==1:
        print("No")
    elif  2*X <= Y <= 4*X:
        print("Yes")
    else:
        print("No")
func()
func()
func()
