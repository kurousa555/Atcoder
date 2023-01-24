# 入力の受け取り
N,X,Y=map(int,input().split())

# 繋がっている頂点の記録
# connect[1]=[2,3,4]なら頂点1から頂点2,3,4へ行ける
connect=[[] for i in range(N+1)]

# (N-1)回
for i in range(N-1):
    # 入力の受け取り
    U,V=map(int,input().split())
    # 繋がっている頂点の記録
    connect[U].append(V)
    connect[V].append(U)

# 頂点Xからの距離
Dist=[-1]*(N+1)
# 頂点Xの距離は0
Dist[X]=0
print(connect)
# print(Dist)

# キューを用意
# インポート
from collections import deque
que=deque()

# (1)Xをキューへ追加
que.append(X)

# (4)キューが空になるまで(2)~(3)を繰り返す
while 0<len(que):
    # (2)キューの左端(先頭)から頂点を取り出す(今いる頂点)
    Now=que.popleft()

    # (3)今いる頂点から行ける頂点について
    # to：今いる頂点から行ける頂点
    for to in connect[Now]:
        # ・距離が更新されていないならば(まだ到達していない頂点ならば)
        if Dist[to]==-1:
            # 距離を記録(今いる頂点の距離+1)
            Dist[to]=Dist[Now]+1
            # キューへ追加
            que.append(to)
print(Dist)
# 答え
ans=deque()

# 頂点Yの距離
Count=Dist[Y]

# 今いる頂点
Now=Y

# Countが1以上の間
while 0<Count:
    # 答えの左端(先頭)に今いる頂点を追加
    ans.appendleft(Now)
    print(Count,ans,Now)
    # 今いる頂点から行ける頂点
    for to in connect[Now]:
        # 距離が(Count-1)である頂点を見つけたら
        if Dist[to]==Count-1:
            # Countをマイナス1
            Count-=1
            # その頂点へ移動
            Now=to

# 答えの先頭にXを追加
ans.appendleft(X)

# 答えの出力(*をつけるとカッコなしで出力できる)
print(*ans)
