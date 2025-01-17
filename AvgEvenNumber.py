# 18. Write a program to find the average of 24,26,28,.....100.

sum=0
count=0

for i in range(24,101):
    if(i%2==0):
        sum=sum+i
        count=count+1

avg=int(sum/count)
print(avg)