# #方針
# 無限に続かない場合はシンプルに、現在位置から入力内容に沿って進めれば良い。
# しかし無限に続く場合、それがどんな入力なのかを考えなければいけない。
# 無限に続く場合
# 1.右左右左.....と続く
# 2.上下上下.....と続く
# 3.右下左上.....と輪のように続く
# 4.左下右上.....3の逆回転で進む
# 以上の4つがある。
# なので、入力内容に沿って実行する時に今向いてる方向を記録する。
# （directions = [右,左,上,右,右......]のように）
# 特定のタイミングで1,2,3,4 の条件のいずれかに該当してしまった場合は-１を出力する。
#1との比較、2との比較は処理短縮のためsetを用いる
#3,4の比較は、可読性のためにあらかじめダメな配列として作成しておく

H,W = map(int,input().split())
G = [list(input()) for _ in range(H)]
directions = []
h,w = 0,0 #現在の位置"
taboo  = [["R","D","L","U"],["D","L","U","R"],["L","U","R","D"],["U","R","D","L"],
            ["R","U","L","D"],["U","L","D","R"],["L","D","R","U"],["D","R","U","L"]]
Progress = True

def add_direction():
    if  (len(directions) == 0) or (directions[-1] != G[h][w]):
        directions.append(G[h][w])
        
while Progress==True:
    if G[h][w] == "U":
        if (h-1) == -1:
            print(h+1,w+1)
            break
        else:
            add_direction()
            h -= 1
    elif G[h][w] == "D":
        if (h+1) == H:
            print(h+1,w+1)
            break
        else:
            add_direction()
            h += 1
    elif G[h][w] == "L":
        if (w-1) == -1:
            print(h+1,w+1)
            break
        else:
            add_direction()
            w -= 1
    elif G[h][w] == "R":
        if (w+1) == W:
            print(h+1,w+1)
            break
        else:
            add_direction()
            w += 1
    if set(directions[-2:]) in [set(["D","U"]), set(["R","L"])]:
        print(-1)
        break
    elif directions[-4:] in taboo:
        print(-1)
        break
