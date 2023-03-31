from sys import stdin
def func():
    a,b,x = map(int,stdin.readline().split())
    length = b-a
    if length==0:
        ans = 0
    else:
        ans = length//x

    if a!=0 and a%x == 0:ans+=1
    return ans
print(func())
