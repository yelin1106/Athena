# 곱하기 혹은 더하기
# 난이도 1
# 풀이시간 12분/30분

data=input()

result=1
for i in range(len(data)):
  num=int(data[i])
  if num==0:
    result+=num
  else:
    result*=num
print(result)