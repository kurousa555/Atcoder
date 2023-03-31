import itertools
S=[input() for _ in range(9)]
ans=0

for x1,y1,x2,y2 in itertools.product(range(9), repeat=4):
  if x2>x1 and y2>=y1 and S[y1][x1]=="#" and S[y2][x2]=="#":
    dx=x2-x1
    dy=y2-y1
    x3=x2+dy
    y3=y2-dx
    x4=x3-dx
    y4=y3-dy
    if 0<=x3<9 and 0<=y3<9 and 0<=x4<9 and 0<=y4<9 and S[y3][x3]=="#" and S[y4][x4]=="#":
      ans+=1
print(ans)
