H, W= map(int,input().split())
R, C= map(int,input().split())
R, C  = R-1,C-1
cnt = 0
if R != H:cnt+=1
if R != 0:cnt+=1
if C != W:cnt+=1
if C != 0:cnt+=1

print(cnt)
