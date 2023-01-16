N,K = map(int,input().split())
people = list(map(int,input().split()))
div = K//N
mod = K%N
people = [[i,p,div] for i,p in enumerate(people)]
people.sort(key=lambda x:x[1])

for i in range(mod):
    people[i][2] += 1

people.sort(key=lambda x:x[0])
for person in people:
    print(person[2])
    

