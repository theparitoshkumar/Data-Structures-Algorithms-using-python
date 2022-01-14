#Find the factors of a number using while loop

num = int(input("Enter the number: "))

print(1,end = " ")

factor = 2
while factor <= num/2:
    if num % factor == 0:
        print(factor,end = " ")
        factor += 1 
print (num, end=' ')