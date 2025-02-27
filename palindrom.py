n=5
lst=[]
for i in range(n):
    lst.append(input("enter the element of the list :"))
print(lst)

lstc=lst.copy()

lstc.reverse()

if lst==lstc:
    print("list is palindrom")
else:
    print("not a palindrom")

