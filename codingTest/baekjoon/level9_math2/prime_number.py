# 소수

m=int(input())
n=int(input())

end=int(n**0.5)+1
temp_list=[True]*(n+1)
temp_list[0]=False
temp_list[1]=False # 10000보다 작은 자연수라고 했지 1보다 크다는 조건이 없으므로...... 1을 바꿔줘야함...어이업네....
for i in range(2,end):
  if temp_list[i]==True:
    for j in range(i+i, n+1, i):
      temp_list[j]=False

prime=list(i for i in range(m,n+1) if temp_list[i]==True)
if prime:
  print(sum(prime))
  print(prime[0])
else:
  print(-1)