# 5. Declare & initialize a number. Check whether the number is in range 0-100
# or not. If not in range print invalid input. Else – if the number is in range 90-
# 100 then print Super Smart, 80-90 print Smart,70-80 print smart enough,
# 60-70 print just smart, 35-60 print no smart, 0-35 print dump.

num =int(input("enter the number "))
print(num)
if(num>=0 and num<=100):
    if(num>=90 and num<=100):
        print("Super Smart")
    elif(num>=80 and num<90):
        print("Smart")
    elif(num>=70 and num<80):
        print("smart enough")
    elif(num>=60 and num<70):
        print("Just smart")
    elif(num>=35 and num<60):
        print("No smart")
    else:
        print("dump")
else:
    print("Invalid input")