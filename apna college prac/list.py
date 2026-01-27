l1=[3,1,2]
l2=[6,5,4]
for i in l2:
    l1.append(i)
for j in range(len(l1)):
    for k in range(j+1,len(l1)):
        if l1[j]>l1[k]:
            l1[j],l1[k]=l1[k],l1[j]
print(l1)