N = int(input())
S = list(input())

for i in range(1,N): #飛び飛びの幅
    tmp=0
    for j in range(N): #飛ぶ出発点
        if  i+j>=N:break #飛んだ到着店がout of rangeだったらbreak

        if S[j]==S[i+j]:
            break

        else:
            tmp+=1

    print(tmp)

