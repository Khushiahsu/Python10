#Write a program to find the sum of natural numbers.

nat1 = 1  #begining the work or initialising the variable
nat2 = int(input('Enter the numbers you want the sum of:'))
sum=0
while nat1<=nat2:  #condition
    sum=sum + nat1   #body of the loop
    nat1=nat1+1      #incrementing before the next iteration
print(sum)