
#1
Dog = {}
print(Dog)

#2
Dog = {'name': 'Julio', 'color': 'Black', 'breed': 'Doberman', 'legs': 4, 'age': 5}
print(Dog)

#3
student_dictionary = {
    "first_name": "Oliver",
    "last_name": "Camacho",
    "gender": "M",
    "age": 18,
    "marital_status": "unmarried",
    "skills": ["procrastinating"],
    "country": "Mexico",
    "city": "Aguascalientes",
    "address": "Calle 13",
}

#4
print(len(student_dictionary))

#5
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))

#6
student_dictionary["skills"].append("Sleeping")

#7
list_keys = list(student_dictionary.keys())

#8
list_values = list(student_dictionary.values())

#9
list_of_tuples = [(k, v) for k, v in student_dictionary.items()]

#10
student_dictionary.pop("marital_status")

#11
del Dog