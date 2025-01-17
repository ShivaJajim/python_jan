# 6. Write a program to perform simple math based on the user inputs by using
# Switch condition.(+ , - , * , /)
print("enter the two numbers ")
num1=int(input())
num2=int(input())
print("given two numbers are ",num1,num2)
print("enter the operation + - * /")
op=input()
print(op)

if(op == "+"):
    print(num1+num2)
elif(op=="-"):
    print(num1-num2)
elif(op=='*'):
    print(num1*num2)
elif(op=="/"):
    print(num1/num2)
else:
    print("entert the above mnetioned symblo only")