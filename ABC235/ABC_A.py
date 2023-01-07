N = list(input())
ans = 0

ans += int("".join(N))

N.append(N[0])
del N[0]
ans += int("".join(N))

N.append(N[0])
del N[0]
ans += int("".join(N))

print(ans)
