# N =int(input())
# X = [int(input()) for _ in  range(N)]

# ans = sum(X) - max(X)//2
# print(ans)

N = int(input())
for cake in range(100):
    for donuts in range(100):
        if cake*4 + donuts*7 == N:
            print("Yes")
            exit()
print("No")
