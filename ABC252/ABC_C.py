N = int(input())
S = [list(map(int,input())) for _ in range(N)]

answers = []
for  i  in range(10):
    time = [True]*10*N
    tmp_ans = []
    for j  in range(N):
        time_tmp = S[j].index(i)
        if time[time_tmp]==False:
            while True:
                time_tmp+=10
                if time[time_tmp] == True:
                    time[time_tmp] = False
                    break
        elif time[time_tmp] == True:
            time[time_tmp] = False
        # print(time_tmp)
        tmp_ans.append(time_tmp)
    # print("="*30)
    answers.append(max(tmp_ans))
print(min(answers))
# print(answers)

