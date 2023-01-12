card = [2,3,4,5,6,7,8,9,10,11,12,13,1]
A,B = map(int,input().split())
A=card.index(A)
B=card.index(B)
if A==B:print("Draw")
if A>B:print("Alice")
if A<B:print("Bob")
Alice、Bobが勝つならBobを、引き分けならを
