#print the length of the list using function and take the list as the paramaeter

def length_lst(lst):
    a=len(lst)
    print(a)
    return a
abhi=["recitent","benovolent","beliver"]
jai=["recitent","benovolent","beliver","jhfdsbgs","sihdbd","ksbd"]


length_lst(abhi)
length_lst(jai)

#-----------------------------------------------------------------------------#

#waf to print the element of the list in a single line

def single_line(listt):
    for i in range(len(listt)):
        print(listt[i],end=" ")

jai=["recitent","benovolent","beliver","jhfdsbgs","sihdbd","ksbd"]

single_line(jai)

#--------------------------------------------------------------------------#

#waf to print the factorial of a number and take the input of the number from the user

def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    print(fact)
    return fact
    
n=int(input("Enter a number : "))
factorial(n)

#------------------------------------------------------------------------#

#waf to convert the USD into INR
def currency_convert(USD):
    INR= USD*86.266
    print("the converted currency in INR is : ",INR)
    return INR

n=float(input("enter the USD to bs converterd : "))
currency_convert(n)

#---------------------------------------------------------------------#

#WAF to check whether the number is even or odd

def even_or_odd(n):
    if n%2==0:
        print("EVEN")
    else:
        print("ODD")

n=int(input("Enter the number : "))
even_or_odd(n)

#---------------------------------------------------------------------#




















