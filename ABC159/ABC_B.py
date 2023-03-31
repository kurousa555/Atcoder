def func():
  S = input()
  N = len(S)
  first = []
  second = []
  for i in range(N//2):
    first.append(S[i])
    second.append(S[-i-1])
    if S[i]!=S[-i-1]:
      print("No")
      exit()
    
  for i in range(len(second)//2):
    if first[i]!=first[-i-1] or second[i]!=second[-i-1]:
      # print(first[i],first[-i-1],second[i],second[-i-1])
      print("No")
      exit()

  print("Yes")

func()
# func()
# func()
