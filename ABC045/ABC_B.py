ABC = [list(input()) for _ in range(3)]

player =  ["A","B","C"]
nxt = 0
# print(player,nxt)
# print(ABC)
for _ in range(300):
    if len(ABC[nxt])==0:break
    tmp = ABC[nxt].pop(0)
    
    # print(ABC,nxt,tmp)
    if tmp=="a":nxt=0
    elif tmp=="b":nxt=1
    elif tmp=="c":nxt=2
    # print(ABC,nxt,tmp)
    # print(ABC)
print(player[nxt])
