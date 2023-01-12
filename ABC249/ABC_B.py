S = list(input())

all_different = False
upcase = False
lowercase = False

if len(S)  == len(set(S)):all_different=True
for s in S:
    if s.islower():lowercase=True
    if s.isupper():upcase=True

if all([all_different,upcase,lowercase]):
    print("Yes")
else:
    print("No")
