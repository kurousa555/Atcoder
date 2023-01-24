n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
total = 0


dis =  []
for i in range(len(a)-1):
    total += abs(a[i+1]-a[i])
    dis.append(abs(a[i+1]-a[i]))
# print(total)
# print(a)
# print(dis)
# for i in range(1,len(a)-1):
# print(dis)
for i in range(n):
    # print((dis[i]+dis[i+1]) , abs(a[i+2]-a[i]))
    ans = total - (dis[i]+dis[i+1]) + abs(a[i+2]-a[i])
    print(ans)
    # print("="*30)
