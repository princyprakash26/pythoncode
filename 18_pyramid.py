
n = 5


for i in range(n):
    for j in range(n-i):   
        print('0',end='')
    for j in range(2*i+1):
        print("*",end='')
    for j in range(n-i):    
        print('0',end='')
    print('\n')
  