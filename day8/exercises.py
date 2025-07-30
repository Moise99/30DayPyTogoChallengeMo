#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Buddy",
    "color": "Brown",
    "breed": "Labrador",
    "legs": 4,
    "age": 5
}

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Koffi",
    "last_name": "Kouma",
    "gender" : "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript", "HTML"],
    "country": "Togo",
    "city": "Lome",
    "address": "Adidogome"
}

#4. Get the length of the student dictionary
student_length = len(student)
print("Length of student dictionary:", student_length)

#5. Get the value of skills and check the data type, it should be a list
skills = student["skills"]
skills_type = type(skills)
print("Skills:", skills)
print("Type of skills:", skills_type)

#6. Modify the skills values by adding one or two skills
student["skills"].extend(["CSS", "React"])
print("Updated skills:", student["skills"])

#7. Get the dictionary keys as a list
student_keys = list(student.keys())
print("Student keys:", student_keys)

#8. Get the dictionary values as a list
student_values = list(student.values())
print("Student values:", student_values)

#9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student items as list of tuples:", student_items)

#10. Delete one of the items in the dictionary
del student["marital_status"]
print("Updated student dictionary after deletion:", student)

#11. Delete one of the dictionaries (dog)
del dog
print("Dog dictionary deleted.")