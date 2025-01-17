# 19. Write programs to sum of the following Series. 52 + 62 + 72
# +..........+1022.
start =int(input())
end=int(input())

for i in range(start,end+1,10):
        print(i, end =" ")
        if(i != end):
            print(",",end="")