#1. Declaration of age as integer variable
age = 25
#2. Declaration of height as a float variable
height = 1.85
#3. Declaration of a variable that store a complex number
complex_number = 3 + 4j

#4. A script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height_triangle
print('The area of the triangle is: ', area)

#5. A script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is: ', perimeter)

#6.  A scrtipt that get rectangle's length and width from the user and calculate its area and perimeter.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))  
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print('The area of the rectangle is: ', area_rectangle)
print('The perimeter of the rectangle is: ', perimeter_rectangle)

#7. A scrtipt that get raduis of the circle from the user and calculate its area and circumference.
radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14 * radius** 2
circumference_circle = 2 * 3.14 * radius
print('The area of the circle is: ', area_circle)
print('The circumference of the circle is: ', circumference_circle)

#8. Calculation of the slope, x-intercept and y-intercept of y = 2x -2
slope8 = 2
y_intercept = -2
x_intercept = -y_intercept / slope8
print('The slope is: ', slope8)
print('The x-intercept is: ', x_intercept)
print('The y-intercept is: ', y_intercept)

#9 Finding the slope and Euclidean distance between point (2, 2) and point (6,10)
slope9 = (10-2) / (6-2)
print('The slope is: ', slope9)

#10 Comparing the slopes in tasks 8 and 9
if slope8 == slope9:
    print('The slopes are equal.')
elif slope8 > slope9:
    print('The slope of task 8 is greater than the slope of task 9.')
else:
    print('the slope of task 8 is less than the slope of task 9.')

#11 Calculating the value of y (y = x^2 + 6x + 9).
x = float(input("Enter a value for x: "))
y = x**2 + 6*x + 9 #try x = -3 to have y = 0
print('The value of y is: ', y)

#12 Finding the length of 'python' and 'dragon' and make a falsy comparison statement
python_length = len('python')
dragon_length = len('dragon')
if python_length == dragon_length:
    print("The lengths of 'python' and 'dragon' are equal.")
elif python_length > dragon_length:
    print("The length of 'python' is greater than the length of 'dragon'.")
else:
    print("The length of 'python' is less than the length of 'dragon'.")

#13 Using and operator to check if 'on' is found in both 'python' and 'dragon'
python_contains_on = 'on' in 'python'
dragon_contains_on = 'on' in 'dragon'   
if python_contains_on and dragon_contains_on:
    print("'on' is found in both 'python' and 'dragon'.")   
else:
    print("'on' is not found in both 'python' and 'dragon'.")

#14 Using in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
if 'jargon' in sentence:
    print("The word 'jargon' is found in the sentence.")
else:
    print("The word 'jargon' is not found in the sentence.")

#15 There is no 'on' in both dragon and python
if 'on' not in 'dragon' and 'on' not in 'python':
    print("'on' is not found in both 'dragon' and 'python'.")
else:
    print("'on' is found in either 'dragon' or 'python' or both.")  

#16 Finding the length of the text python and convert the value to float and convert it to string
text = 'python'
text_length = len(text)
text_length_float = float(text_length)
text_length_str = str(text_length_float)
print("The length of the text 'python' is: ", text_length)
print("The length as float is: ", text_length_float)
print("The length as string is: ", text_length_str)

# 17 Even numbers are divisible by 2 and the remainder is zero, checking if a number is even or not 
number = 4
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is not an even number.")

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division_result = 7 // 3
int_value = int(2.7)
if floor_division_result == int_value:
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7.")
else:
    print("The floor division of 7 by 3 is not equal to the int converted value of 2.7.")

#19 Check if type of '10' is equal to type of 10
type_of_10_str = type('10')
type_of_10_int = type(10)
if type_of_10_str == type_of_10_int:
    print("The type of '10' is equal to the type of 10.")
else:   
    print("The type of '10' is not equal to the type of 10.")

#20 Check if int('9.8') is equal to 10
int_value = int('9.8')
if int_value == 10:
    print("int('9.8') is equal to 10.")
else:
    print("int('9.8') is not equal to 10.")

#21 A script that prompts the user to enter hours and rate per hour. Calculating pay of the person
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is: ", pay)

#22 A script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years you have lived: "))
seconds_per_year = 365 * 24 * 60 * 60  # seconds in a year
total_seconds = years * seconds_per_year
print("You have lived for", total_seconds, "seconds.")

#23 Writing a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for number in range(1, 6):
    square = number ** 2
    cube = number ** 3
    # print the rows using f-strings
    print(f'{number}\t{square}\t{cube}')
