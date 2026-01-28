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
    if action=="A":
        name=set()
        add_name=input("Enter student name : ")
        name.add(add_name)
        dict.update({name})
        print(dict)
        

# new_name="Veer"
# marks=10
# dict.update({new_name:marks})
# print(dict)

# up_name="Ram"
# dict.update({up_name:9})
# print(dict)
