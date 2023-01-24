import collections
N = int(input())
A = list(map(int,input().split()))
A = collections.Counter(A)
rectangle = [a[0] for a in A.items() if 2<=a[1]<=3]
rectangle.sort(reverse=True)
square = [a[0] for a in A.items() if a[1]>=4]
square.sort(reverse=True)

print(rectangle)
print(square)
if len(square)==0 and len(rectangle)<2:
    print(0)
elif len(rectangle)<2:
    print(square[0]**2)
elif  len(square)==0:
    print(rectangle[0]*rectangle[1])
elif len(rectangle)>=2 and len(square)>0:
    print(max(square[0]**2,rectangle[0]*rectangle[1]))
else:
    print(0)
