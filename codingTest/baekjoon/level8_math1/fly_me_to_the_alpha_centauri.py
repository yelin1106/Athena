#Fly me to the Alpha Centauri

t=int(input())

for _ in range(t):
  x, y=map(int,input().split())
  cnt=0
  remain=y-x
  i=1
  while remain>=i*2:
    remain-=i*2
    cnt+=2
    i+=1
    print(f'while {remain} {cnt} {i}')
  if remain==i:
    remain-=i
    cnt+=1
  if remain != 0:
    #i-=1
    #print(i)
    while remain>0:
      remain-=i
      cnt+=1
      i-=1
      print(f'2end while {remain} {cnt} {i}')
  print(cnt)