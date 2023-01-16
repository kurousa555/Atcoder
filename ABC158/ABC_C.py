A,B =  map(int,input().split())
for num  in range(1,1251):
    if (int(num*0.08)==A) and  (int(num*0.1)==B):
        print(num)
        exit()
print(-1)
