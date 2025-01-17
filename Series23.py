# 23. Write programs to print the following series. 5^2, 7^2,9^2.....25^2

for i in range(5,26):
    if(i%2 ==1):
        print(i,"^2",end="")
    if(i != 25 and i%2==1):
        print(",",end=" ")