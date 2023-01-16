def func():
    N,M = map(int,input().split())
    A = [list(input()) for _ in range(2*N)]
    # print(A)
    A = [list(a) for a in zip(*A)]
    # print(A)
    players = [[i+1,0] for i in range(N*2)] #[[選手1,得点],[選手2,得点]....[選手2*N,得点]]

    for i in range(M):#ラウンド
        for j in range(1,N+1):
            playerA = players[2*j-2][0]
            playerB = players[2*j-1][0]
            junken_A = A[i][playerA-1]
            junken_B = A[i][playerB-1]
            if (junken_A == "G" and  junken_B == "C"):players[2*j-2][1] += 1
            if (junken_A == "P" and  junken_B == "G"):players[2*j-2][1] += 1
            if (junken_A == "C" and  junken_B == "P"):players[2*j-2][1] += 1
            if (junken_B == "G" and  junken_A == "C"):players[2*j-1][1] += 1
            if (junken_B == "P" and  junken_A == "G"):players[2*j-1][1] += 1
            if (junken_B == "C" and  junken_A == "P"):players[2*j-1][1] += 1
        players.sort(reverse=True, key=lambda x: (x[1],-x[0]))

    for player in players:
        print(player[0])

func()
