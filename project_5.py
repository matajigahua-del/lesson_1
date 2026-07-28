students={"rahul":"maths","sadie":"english","Karan":"social","farah":"hindi"}
print("Original Dictionary:", students)
print("Subject of Rahul")
print(students.get("rahul"))
print("Subject of Karan")
print(students.get("Karan"))
print("Subject of Makla")
print(students.get("Makla"))
students["Makla"]="science"
students["Karan"]="physics"
students.pop("farah")
print("total records:",len(students))
print("Final students records:")
for name,subject in students.items():
    print(name,":",subject)