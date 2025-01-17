# 22. Write programs to print the following series. 100,200,300........10000

for i in range(100,1000+1,100):
    print(i,end="")
    if( i != 1000):
        print(",",end="")