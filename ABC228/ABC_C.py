N,K  = map(int,input().split())
students = []
for i in range(N):
    P = list(map(int,input().split()))
    sumP = sum(P)
    students.append([i,sumP]) 
sort_students = sorted(students,reverse=True,key=lambda x:x[1])
boder = sort_students[K-1][1]
# print(sort_students)
# print(boder)
for s in students:
    if s[1]+300 >= boder:
        print("Yes")
    else:
        print("No")



