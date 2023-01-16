S = list(input())
if S[0] == "A":
    if S[2:-1].count("C") == 1: 
        C_idx = S[2:-1].index("C")
        del S[C_idx+2]
        del S[0]
        if "".join(S).islower():
            print("AC")
            exit()
print("WA")

# S の先頭の文字は大文字の A である。
# S の先頭から 3 文字目と末尾から 2 文字目の間（両端含む）に大文字の C がちょうど 1 個含まれる。
# 以上の A, C を除く S のすべての文字は小文字である。
