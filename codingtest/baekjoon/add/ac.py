# AC
# https://www.acmicpc.net/problem/5430

# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []
from collections import deque

t=int(input())
for _ in range(t):
  p=list(input())
  n=int(input())
  nums=deque(map(int,input().split()))
  cnt=0
  for c in p:
    if c=="R":
      cnt+=1
    if c=="D":
      if not nums:
        print("error")
        break
      if cnt%2:
        nums.sort(reverse=True)
        cnt=0
      nums.popleft()
  print(nums)