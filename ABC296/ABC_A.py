from sys import stdin
def func():
    N = int(input())
    S = list(input())
    for i in range(N-1):
        if not ((S[i] == "M" and S[i+1]  == "F") or (S[i] == "F" and S[i+1]  == "M")):
            print("No")
            exit()
            
    print("Yes")
func()
