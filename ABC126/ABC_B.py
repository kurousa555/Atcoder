S = input()
first  = S[:2]
second = S[2:]
ans = 0

# print(first,second)
if 0<=int(first)<=99 and 1<=int(second)<=12:
    if 1<=int(first)<=12 and 0<=int(second)<=99:
        print("AMBIGUOUS")
        exit()

if 0<=int(first)<=99 and 1<=int(second)<=12:
    # if not (0<=int(first)<=12 and 0<=int(second)<=99):
    print("YYMM")
    exit()

if 1<=int(first)<=12 and 0<=int(second)<=99:
    # if  (0<=int(first)<=12 and 0<=int(second)<=99):
    print("MMYY")
    exit()

print("NA")
# print(first,second)
