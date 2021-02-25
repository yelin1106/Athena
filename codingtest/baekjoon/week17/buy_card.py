# 카드 구매하기
# https://www.acmicpc.net/problem/11052

# 4
# 1 5 6 7

n=int(input())
p=[0]+list(map(int, input().split()))

dp=[0]*(n+1)
# dp[1]=p[1]
# dp[2]=max(p[1]+p[1], p[2])
for i in range(1, n+1):
  for j in range(1, i+1):
    # if i%j==0:
    #   dp[i]=max(dp[i],i//j*p[j])
    dp[i]=max(dp[i],dp[i-j]+p[j])
print(dp)
print(dp[n])
