from collections import Counter

def count_happy_substrings(s):
    # 文字列 s の嬉しい列になる部分文字列の個数を求める関数
    n = len(s)
    ans = 0
    cnt = Counter()
    l = 0
    for r in range(n):
        cnt[s[r]] += 1
        while len(cnt) > (r - l + 1) // 2:
            cnt[s[l]] -= 1
            if cnt[s[l]] == 0:
                del cnt[s[l]]
            l += 1
        if len(cnt) == (r - l + 1) // 2:
            ans += 1
    return ans

s = input()  # 文字列 S を入力とする
print(count_happy_substrings(s))
