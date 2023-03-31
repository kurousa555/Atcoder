def func():
    A,B,C = map(int,input().split())
    if C%2==0:C=2
    else:C=1

    if pow(A,C)>pow(B,C):
        print(">")
    if pow(A,C)<pow(B,C):
        print("<")
    if pow(A,C)==pow(B,C):
        print("=")


func()
func()
func()
