a= [1, 2, 3, 4, 2 , 3]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# for k in range(len(a)-1):
#     if a[k]==a[k+1]:
#         print(a[k])
seen = set()
duplicates = set()
for x in a:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(duplicates)