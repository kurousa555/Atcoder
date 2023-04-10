from sys import stdin
def func():
    C = [list(map(int,stdin.readline().split())) for _ in range(3)]
    for a1 in range(101):
        for a2 in range(101):
            for a3  in range(101):
                b_list = [set(),set(),set()]
                b_list[0].add(a1-C[0][0])
                b_list[0].add(a2-C[1][0])
                b_list[0].add(a3-C[2][0])
                # print(C[0][0],C[1][0],C[2][0])
                b_list[1].add(a1-C[0][1])
                b_list[1].add(a2-C[1][1])
                b_list[1].add(a3-C[2][1])
                b_list[2].add(a1-C[0][2])
                b_list[2].add(a2-C[1][2])
                b_list[2].add(a3-C[2][2])
                # print(b_list,a1,a2,a3)
                if len(b_list[0]) == 1 and len(b_list[1]) == 1 and len(b_list[2]) == 1:
                    print("Yes")
                    exit()
    print("No")
    return

func()
