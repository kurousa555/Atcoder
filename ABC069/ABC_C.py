N = int(input())
A = list(map(int,input().split()))
A = [a%4 for a in A]
all_count = len(A)
two_count = len([a%4 for a in A if a%4==2])
zero_count =len([a%4 for a in A if a%4==0])
# print(two_count,all_count)
if two_count >=1:all_count = all_count - two_count+1
# print(all_count,zero_count,two_count)

if  zero_count >=  all_count-zero_count-1:
    print("Yes")
else:
    print("No")
