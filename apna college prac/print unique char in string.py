# string=input("Enter a string : ")
# seen=set()
# for x in string:
#     seen.add(x)
# print(seen)
# print(len(seen))

string = input("Enter a string: ")

unique_chars = []
for ch in string:
    if ch not in unique_chars:
        unique_chars.append(ch)

print(unique_chars)
print(len(unique_chars))
