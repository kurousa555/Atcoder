from sys import stdin
def func():
    S = [list(input()) for _ in range(8)]
    for col in range(8):
        for row in range(8):
            if S[col][row] == "*":
                # print(col,row)
                if row==7:first="h"
                if row==6:first="g"
                if row==5:first="f"
                if row==4:first="e"
                if row==3:first="d"
                if row==2:first="c"
                if row==1:first="b"
                if row==0:first="a"
                print(str(first)+str(8-col))
    return
func()
