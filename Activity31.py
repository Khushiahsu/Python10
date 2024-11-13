#Write a program to check if the number entered by the user is an Armstrong number or not?

ar1 = int(input('Enter a random number'))





ar2 = 0
ar3 = ar1
while ar3>0:
    ar4 = ar3%10
    ar2 += ar4**3
    ar3 //= 10
if ar1 == ar2:
    print('It is an armstrong number')
else:
    print('It is not an armstrong number')
