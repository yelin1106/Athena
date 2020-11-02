# 볼링공 고르기
# 난이도 1
# 풀이시간 8분/30분
n, m=map(int, input().split())
data=list(map(int, input().split()))
cnt=0
for i in range(len(data)):
  for j in range(i+1,len(data)):
    if data[i]!=data[j]:
      cnt+=1
print(cnt)
