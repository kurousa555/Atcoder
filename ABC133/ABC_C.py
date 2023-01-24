L,R = map(int,input().split())
if (0 in  (L,R)) or (R-L>=2019):
    print(0)
else:
    ans =  2018
    for i in range(L,R+1):
        for j in range(i+1,R+1):
            tmp = (i*j)%2019
            if tmp<ans:ans=tmp
            if ans==0:
                print(0)
                exit()
    print(ans)
