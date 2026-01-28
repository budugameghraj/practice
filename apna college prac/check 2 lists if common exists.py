list1 = [1, 2, 3, 4]
list2 = [ 5, 6, 7, 8]
# a=set(list1)
# b=set(list2)
# if a.intersection(b):
#     print("Common Elements exist.")
# else:
#     print("common elements are not present.")
count=0
for i in list1:
    for j in list2:
        if i==j:
            count+=1
if count!=0:
    print("Common elements exist.")
else:
    print("Common elements do not exist.")