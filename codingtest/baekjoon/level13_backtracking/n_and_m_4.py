# N과 M (4)

def dfs(n, m, nums, check, ans):
  if len(ans)==m:
    print(" ".join(map(str, ans))) 
    return
  for i in range(n):
    if check[i]: continue
    ans.append(nums[i])
    dfs(n, m, nums, check, ans) 
    ans.pop()
    check[i]=True
    for j in range(i+1, n):
      check[j]=False
  return

n, m=map(int,input().split())
nums=[i for i in range(1, n+1)]
check=[False]*n
ans=[]
dfs(n, m, nums, check, ans)