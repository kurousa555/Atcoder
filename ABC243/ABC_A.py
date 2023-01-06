V,A,B,C= map(int,input().split())
ABC = [A,B,C]
while True:
    for i in range(3):
        if V < ABC[i]:
            if i  == 0:print("F")
            if i  == 1:print("M")
            if i  == 2:print("T")
            exit()                
        V -= ABC[i]
