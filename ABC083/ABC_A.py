import math
a,b,c,d = map(int,input().split())
if (a+b)>(c+d):print("Left")
if (a+b)==(c+d):print("Balanced")
if (a+b)<(c+d):print("Right")
