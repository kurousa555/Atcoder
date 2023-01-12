# 入力の受け取り
N=int(input())
S=list(map(int, input().split()))
T=list(map(int, input().split()))

# 1週目
for i in range(N):
    # 次のすぬけ君の番号。i=N-1のとき、次のすぬけ君の番号=Nではなく=0とするため%Nとする。
    next=(i+1)%N
    print(next)
    # 高橋君からもらうのが早いか、左隣のすぬけ君からもらうのが早いか
    T[next]=min(T[next], T[i] + S[i])

# 2周目
for i in range(N):
    # 次のすぬけ君の番号。i=N-1のとき、次のすぬけ君の番号=Nではなく=0とするため%Nとする。
    next=(i+1)%N
    # 高橋君からもらうのが早いか、左隣のすぬけ君からもらうのが早いか
    T[next]=min(T[next], T[i] + S[i])

# 答えの出力
# for ans in T:
#   print(ans)
