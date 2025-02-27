#print count 0 to 100
count=0
while count<=100:
    print(count)
    count+=1
#--------------------------------------------------------------------------------#

#print number from 100 to 1
count =100
while count>=1:
  print(count)
  count-=1
#--------------------------------------------------------------------------------#

#print the multiplication of the number n

n=int(input("Enter the number : ")
i=1
while i <=10:
  print(i*n)
  i+=1
#------------------------------------------------------------------------------#

#print the element of a list using while loop
lst=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(lst):
  print(lst[i])
  i+=1

#------------------------------------------------------------------------------#

#search a number x in a tuple using while loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=9
i=0
while i<len(tup):
  if(tup[i]==x):
    print("element found at index :",i)
    break
  i+=1
else:
    print("element not found")
  












