
def func():
    s = list(input())
    ans = [s[0]]
    now  = s[0]
    cnt =  0
    for i in range(len(s)):
        if s[i] !=  now:
            now = s[i]
            ans.append(str(cnt))
            ans.append(now)
            cnt = 1
            
        elif s[i] ==  now:
            cnt += 1
    ans.append(str(cnt))
    print("".join(ans))

func()
func()
func()
