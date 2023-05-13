lst=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    r=int(input("Enter elements of list:")) 
    lst.append(r)
print("The given list is:",lst)
print("The positive numbers in list are : ",end='')
for i in lst:
    if(i>=0):
        print(i,end=',')
        