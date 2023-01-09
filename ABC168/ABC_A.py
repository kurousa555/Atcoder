N = input()
if N[-1] in ("2","4","5","7","9"):print("hon")
elif N[-1] in ("0","1","6","8"):print("pon")
elif N[-1] in ("3"):print("bon")

N の 1 の位が 2,4,5,7,9 のとき hon
N の 1 の位が 0,1,6,8 のとき pon
N の 1 の位が 3 のとき bon
