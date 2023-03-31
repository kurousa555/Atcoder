S = list(input())
yes_nums = set()
even_nums = set()
no_nums = set()
for i in range(10):
    if S[i] in ("o"):yes_nums.add(str(i))
    if S[i] in ("?"):even_nums.add(str(i))
    if S[i] in ("x"):no_nums.add(str(i))

ans = 0
for num in range(10000):
    str_nums = str(num).rjust(4,"0")
    list_nums = set((str_nums))
    if list_nums & yes_nums == yes_nums:
        if len(list_nums & no_nums) == 0:
            ans +=1
    

print(ans)
