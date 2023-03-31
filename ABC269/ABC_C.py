# 入力の受け取り
N=int(input())
# Nを2進数へ変換
Nbit=bin(N)
# 「0b」を消す
Nbit=Nbit[2:]
# 反転
Nbit=Nbit[::-1]
 
# xlistへ空の文字列を入れておく
xlist=[""]
print(Nbit)
# i=0~(Nbitの長さ-1)まで
for i in range(len(Nbit)):
    # 新しいxlistのリスト
    Newxlist=[]
    print(i)
    # Nの右からi桁目が「0」ならば
    if Nbit[i]=="0":
        # x：xlistの要素を順に格納
        for x in xlist:
            # 先頭に「0」をつける
            Newxlist.append("0"+x)
   
    # Nの右からi桁目が「1」ならば
    else:
        # # x：xlistの要素を順に格納
        for x in xlist:
            # 先頭に「0」をつける
            Newxlist.append("0"+x)
            # 先頭に「1」をつける
            Newxlist.append("1"+x)
    print(Newxlist)
    # xlistを更新
    xlist=Newxlist
    print(xlist)
    print("*"*30)
 
# xを10進数に変換した数の格納リスト
anslist=[]
 




# # x：xlistの要素を順に格納
for x in xlist:
    # 10進数へ変換して追加
    anslist.append(int(x,2))
 
# 小さい順に並び替え
anslist.sort()
 
# ans：anslistの要素を順に格納
# for ans in anslist:
    # ansを10進数へ変換
    # print(ans)
