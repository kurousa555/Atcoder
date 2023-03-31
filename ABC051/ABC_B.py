from sys import stdin
def func():
    K,S = map(int,stdin.readline().split())
    nums =  []
    ans = 0
    for x in range(S+1):
        for y in range(x,S+1):
            z = S-x-y
            # print(x,y,z)
            if 0<=x<=K and 0<=y<=K and 0<=z<=K and x<=y<=z:
                # print(x,y,z)
                if len(set([x,y,z])) == 3:ans+=6
                if len(set([x,y,z])) == 2:ans+=3
                if len(set([x,y,z])) == 1:ans+=1


    return ans
print(func())
