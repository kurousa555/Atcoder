N = int(input())
contests  =  [111,222,333,444,555,666,777,888,999]
contests.append(N)
contests.sort()
idx =  contests.index(N)
print(contests[idx+1])
