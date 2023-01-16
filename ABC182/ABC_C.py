N = input()
lenN = len(N)

ans = 100
for num in range(1<<lenN):
    # print(bin(num))
    tmp_num = ""
    tmp_ans = 0
    for shift in range(lenN):
        if (num>>shift) & 1 == 1:
            # print(N[shift])
            tmp_num = N[shift]+tmp_num
        else:
            tmp_ans +=  1

    if tmp_num == "":continue

    if int(tmp_num)%3==0:
        if ans > tmp_ans:
            ans = tmp_ans

if ans == 100:
    ans = -1
print(ans)
