# 큰수의 법칙

n, m, k=map(int, input().split())
nums=list(map(int, input().split()))

nums.sort()
div=m//(k+1)
remain=m%(k+1)
ans=nums[-1]*((div*k)+remain)+nums[-2]*(div)
print(ans)