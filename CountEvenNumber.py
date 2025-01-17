# 12. Write a Program to print the count of the even numbers between the given
# range?
print("Enter the range ")
n1 = int(input())
n2 = int(input())
count=0
for i in range(n1,n2+1):
    if(i%2==0):
        count=count+1

print(count)



