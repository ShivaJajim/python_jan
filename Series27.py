# 27. Write programs to print the following series. 1,2,factor of three,4,5,factor
# of three, 7,8,factor of three,..........22,23,factor of three.

for i in range(1,24):
    print(i,",",i+1,"factor of three",end="")
    if(i !=23):
        print(",",end="")