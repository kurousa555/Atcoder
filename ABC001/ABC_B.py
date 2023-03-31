m = int(input())
km = m/1000 #kmに変換


if km < 0.1:
    VV = "00"
elif km >= 0.1 and km <=5:
    VV = int(km*10)
    if len(str(VV)) == 1:
        VV = "0"+str(VV) 
elif km >= 6 and km <= 30:
    VV = int(km +50)
elif km >= 35 and km <= 70:
    VV = int((km-30)/5 + 80)
elif km >= 70:
    VV = 89
print(VV)
