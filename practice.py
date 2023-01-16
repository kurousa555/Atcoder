N,L = map(int,input().split())
features = [list(input().split()) for _ in range(N)]
mimimum = []

for _ in range(N+4):
    for k in range(N):
        features[k].append(features[k][0])
        del features[k][0]

    for j in range(1,L+2):
        feature = []
        for i in range(N):
            feature.append("".join(features[i][0:j]))
        if len(feature)  ==  len(set(feature)):
            mimimum.append(j)
            break

print(min(mimimum))
