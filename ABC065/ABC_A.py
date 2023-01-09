X,A,B = map(int,input().split())

if A>=B:print("delicious")
elif A<B and  X>=(B-A):print("safe")
else:print("dangerous")

