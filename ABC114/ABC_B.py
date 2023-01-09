S = tuple(input())

abs_list = []
for i in range(len(S)-2):
    num = int("".join((S[i:i+3])))
    abs_list.append(abs(753-num))
print(min(abs_list))
