# 분해합

n=int(input())

ans_list=[]
num_sum=0
for i in range(n):
  num=str(i)
  num_sum=i
  for j in num:
    num_sum+=int(j)
  if num_sum==n:
    ans_list.append(i)
ans_list.append(0)
print(ans_list[0])
print(ans_list)