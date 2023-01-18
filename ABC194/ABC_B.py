import  copy
N  = int(input()) 
AB = [list(map(int,input().split())) for _ in range(N)]
pattern1 =  list(map(sum,AB))
pattern1 = min(pattern1)

pattern2_AB = AB.copy()
A_min_person = min(pattern2_AB,key=lambda x:x[0])
A_min_value = A_min_person[0]
pattern2_AB.remove(A_min_person)
B_min_person = min(pattern2_AB,key=lambda x:x[1])
B_min_value = B_min_person[1]
pattern2 = max(A_min_value,B_min_value)

pattern3_AB = AB.copy()
B_min_person = min(pattern3_AB,key=lambda x:x[1])
B_min_value = B_min_person[1]
pattern3_AB.remove(B_min_person)
A_min_person = min(pattern3_AB,key=lambda x:x[0])
A_min_value = A_min_person[0]
pattern3 = max(A_min_value,B_min_value)
print(min(pattern3,pattern1,pattern2))
