h1,h2,h3,w1,w2,w3 = map(int,input().split())
range_max =  max(h1,h2,w1,w2)
cnt = 0

for i in range(1,max(h1,w1)):#[1][1]
    for j in range(1,max(h2,w1)):#[2][1]
        for k in range(1,max(h1,w2)):#[1][2]
            for l in range(1,max(h2,w2)):#[2][2]
                if (i+k < h1):
                    if (j+l < h2) :
                        if (i+j < w1):
                            if (k+l < w2):
                                if ((h1-(i+k)) + (h2-(j+l)) < w3) and ((w1-(i+j)) + (w2-(k+l)) < h3):
                                    if (w1-(i+j)) + (w2-(k+l)) + (w3 - (h1-(i+k)) - (h2-(j+l))) == h3:
                                        # if (h1-(i+k)) + (h2-(j+l)) + (h3 - (w1-(i+j)) - (w2-(k+l))) == w3:
                                            cnt += 1
print(cnt)

