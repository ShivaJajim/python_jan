# 28. Write programs to print the following series. 1,3, divisible by five, 7,9,
# 11,13, divisible by five,.....21,23, divisible by five
count=0
j=3
for i in range(1,26):
    if(i%2==1):

        if(i%5==0):
            print("divisible by five",end="")
            j=j+1
        else:
            print(i,end="")

        if(i != 25):
             print(",",end="")