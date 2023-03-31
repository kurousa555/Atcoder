from sys import stdin
sx,sy,gx,gy = map(int,stdin.readline().split())

sloop = (-gy-sy)/(gx-sx)
coordinate = sy - sloop*sx
ans = coordinate/(-sloop)
# print(coordinate)
# print(sloop)
print(ans)
