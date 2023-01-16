def func():
    A,B,C,D = map(int,input().split())
    blue = A
    red = 0

    if C*D<B:
        return -1
    
    ans = 0
    for _ in range(10**5):
        blue += B
        red += C
        ans += 1
        # print(blue,red)
        if blue <= red*2:return ans
        
    # return -1

print(func())
