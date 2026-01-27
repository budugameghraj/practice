dict={"Ram":10,
      "Raj":9,
      "Surya":11,
      "Arun":8,
      }
Game=True
while Game == True:
    action=input("Press the following to perform actions accordingly : \n" \
    "'A' to add new student and marks\n"
    "'B' to update marks\n"
    "'C' to search student\n"
    "'D' to display the table\n" )

if action!="A" or "B" or "C" or "D":
    Game=False
# new_name="Veer"
# marks=10
# dict.update({new_name:marks})
# print(dict)

# up_name="Ram"
# dict.update({up_name:9})
# print(dict)

# search_name="Rahul"
# length=0
# index=0
# for i in dict:
#     length+=1
# for name in dict:
#     if name!=search_name:
#         index+=1
#     else:
#         break
# if index<length-1:
#     print(f"The student name is present at the index {index}.")
# else:
#     print("Student not present in the table")

# if input=="D":
#     print(dict)