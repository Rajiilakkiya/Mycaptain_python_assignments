def most_frequent(s,j):
    num=s.count(j)
    print(j,"= {0:02d}".format(num))
s=input('Enter a string:')
lst=[]
for i in s:
    if i not in lst:
        lst.append(i)
for j in lst:
    most_frequent(s,j)
    
    