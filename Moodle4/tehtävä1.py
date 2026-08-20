# Write a program that uses a while loop to print out all
# numbers divisible by three in the range of 1-1000.

num = 1

while num <= 1000:
    if num % 3 ==0:
        print(num)
    num +=1  