dishes = []
time = 0
for _ in range(5):
    dish = list(input())
    if dish[-1] == "0":
        time  += int("".join(dish))
    else:
        dishes.append(dish)

if len(dishes) >= 1:
    dishes = sorted(dishes, reverse=True,key=lambda x :x[-1])
    for i in range(len(dishes)-1):
        t = int("".join(dishes[i]))
        time += t + (10-t%10)
    print(time + int("".join(dishes[-1])))

else:
    print(time)

