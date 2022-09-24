def sushu(num1):
    for a in range(2,num1):
        if num1%a==0:
            print(num1,"为合数")
            break
    else:
       print(num1,"为素数")

num1=int(input("输入数字"))
for a in range(1,num1+1):
   sushu(a)
print(num1)