l=[1,2,2,2,4,4,4,4,4,6,6,6,6,6,67,7,7,7,7,77,6,6,4,7,34,3,2,2,1,2,]

# Через множество
print(list(set(l)))

# Через новый список
l1=[]
for i in range (len(l)):
     if (l[i] in l1)==False:
         l1.append(l[i])
print (l1)



