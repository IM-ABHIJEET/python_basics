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
