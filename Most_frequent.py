def most_frequent(s,j):
    num=s.count(j)
    return num
s=input('Enter a string:')
lst=[]
for i in s:
    if i not in lst:
        lst.append(i)
dic={}
for j in lst:
    count=most_frequent(s,j)
    dic[j]=count
for elem in sorted(dic.items(),reverse=True,key=lambda x:x[1]):
    print(elem[0],":{0:02d}".format(elem[1]))