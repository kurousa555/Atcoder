N,M = map(int,input().split())
students = tuple(tuple(map(int,input().split())) for _ in range(N))
points = tuple(tuple(map(int,input().split())) for _ in range(M))


for i in range(N):
    maximum =10000000000
    shortest = None
    for j in range(M):
        dis = abs(students[i][0] - points[j][0]) + abs(students[i][1] - points[j][1])
        if dis<maximum:
            shortest = j+1
            maximum = dis
    print(shortest)
