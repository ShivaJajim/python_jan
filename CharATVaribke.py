# 17. Write a Program to print the all alphabets by using character Variable?
# ord funtion will convert the A to assic value
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end=" ")
print(" ")
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=" ")