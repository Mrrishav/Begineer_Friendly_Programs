n=int(input("Enter a 4-digit number\n"))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
d=n
sum=a+b+c+d
print("sum of digits=", sum)
