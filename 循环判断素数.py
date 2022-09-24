num1=int(input("其输入大于2的任意整数"))
for a in range(1,num1+1):
    for b in range(2,a):
        if a%b==0:
            print(a,'可被',b,"整除")
            break 
    else :
        print(a,'是素数')
        
    
    