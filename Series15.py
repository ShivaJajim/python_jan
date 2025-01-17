# 15. Print following series 2*3,3*4,4*5,......16*17 (Print in two ways – patter
# & multiplied value)
print("enter the two values")
start=int(input())
end=int(input())

for i in range (start,end):
    print(i,"*",(i+1),end=" ")
    if(i != end-1):
        print(",",end=" ")

