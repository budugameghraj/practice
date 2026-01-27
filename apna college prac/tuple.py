a=(3,2,1,5,6,7,9,8)
b=()
c=()
d=list(b)
e=list(c)
for i in a:
    if i%2==0:
        d.append(i)
    else:
        e.append(i)
print(tuple(d))
print(tuple(e))