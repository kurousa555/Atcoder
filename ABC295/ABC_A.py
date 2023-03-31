from sys import stdin
def func():
    check = ["and", "not", "that", "the", "you"]
    N = int(input())
    words = list(stdin.readline().split())

    for word in words:
        if word in check:
            # print(word)
            print("Yes")
            exit()
    print("No")

func()
