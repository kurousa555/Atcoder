N = int(input())
A = list(map(int,input().split()))
colors = [False]*8
god = 0

for a in A:
    if 1<=a<=399    :colors[0]=True
    if 400<=a<=799  :colors[1]=True
    if 800<=a<=1199 :colors[2]=True
    if 1200<=a<=1599:colors[3]=True
    if 1600<=a<=1999:colors[4]=True
    if 2000<=a<=2399:colors[5]=True
    if 2400<=a<=2799:colors[6]=True
    if 2800<=a<=3199:colors[7]=True
    if 3200<=a     :god+=1

colored = colors.count(True)
if colored >= 1:
    maximum = colored + god
    minimum = colored
if colored == 0:
    maximum = god
    minimum=1
print(minimum,maximum)
