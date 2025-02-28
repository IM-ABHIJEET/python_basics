# WAP to print the number fron n to 0

def show(n):
  if n==-1:
    return
  print(n)
  show(n-1)

n=5
show(n)

#-------------------------------------------------------------------------#

# WAP to print the factorial of a number using recursion

def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return (n*factorial(n-1))

n=int(input("Enter the number : "))
abs=factorial(n)
print(abs)

#--------------------------------------------------------------------------#

#WAP to print the fibonacci series upto the n numbers

def fibb(n):
    if n==0:
        print("invalid input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)
n=int(input("enter the number : "))
fibb(n)
for i in range (1,n+1):
    print(fibb(i),end=" ")

#----------------------------------------------------------------------------#

#WAP to find the sum of n natural number

def sum(n):
  if n==0:
    return 0
  else:
    return n+sum(n-1)

n=int(input("enter the number : "))
print(sum(n))

#-------------------------------------------------------------------------------#












