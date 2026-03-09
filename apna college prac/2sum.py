def twosum(a,target):
    seen={}
    for i in range(len(a)):
        complement = target-a[i]
        if complement in seen:
            return [seen[complement],i]
        seen[a[i]]=i
s=[2,7,11,15]
y=9
twosum(s,y)