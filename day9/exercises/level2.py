#1. Write a code which gives grade to students according to theirs scores:
#80-100, A | 70-89 (error here it must be 70 - 79), B | 60-69, C | 50-59, D | 0-49, F
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("Your grade is A.")
elif 70 <= score < 79:
    print("Your grade is B.")
elif 60 <= score < 69:
    print("Your grade is C.")
elif 50 <= score < 59:
    print("Your grade is D.")
elif 0 <= score < 49:
    print("Your grade is F.")

#2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter a month: ").strip().capitalize()
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month entered. Please try again.")

#3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input("Enter a fruit: ").strip().lower()
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Fruit added to the list. New list:", fruits)

