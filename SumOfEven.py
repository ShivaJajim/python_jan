# 16. Write a program to sum all even numbers between 382 and 582.
print("Enter the range teo numbers")
n1=int(input())
n2=int(input())
sum=0
for i in range(n1,n2+1):
    if(i%2==0):
        sum=sum+i
print(sum)