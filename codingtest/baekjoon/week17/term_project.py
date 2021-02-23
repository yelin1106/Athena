# 텀 프로젝트
# https://www.acmicpc.net/problem/9466

# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8
from collections import deque


def dfs(i, result):
  visited[i]=True
  cycle.append(i)
  number=numbers[i]

  if visited[number]:
    if number in cycle:
      result+=1
    return
  else:
    dfs(number)


t=int(input())

for _ in range(t):
  n=int(input())
  numbers=[0]+list(map(int, input().split()))
  visited=[True]+[False]*n
  result=0

  for i in range(1, n+1):
    if not visited[i]:
      cycle=[]
      result+=dfs(i, 0)
  print(result)

