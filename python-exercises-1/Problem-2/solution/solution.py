R,C = map(int, input().split()) 
apple=1
for i in range(1,R+1):
  for j in range(1,C+1):
    if(j==C):
      print(apple)
    else:
      print(apple,end=' ')
    apple+=1