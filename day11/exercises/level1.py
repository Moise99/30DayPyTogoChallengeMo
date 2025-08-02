#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5))  

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

print(area_of_circle(5))

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*numbers):
    for number in numbers:
        if type(number) is not int and type(number) is not float:
            return "All arguments must be numbers."
    
    return sum(numbers)
print(add_all_nums(1, 2, 3, 4)) 

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(10))  

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    elif month in ['september', 'october', 'november']:
        return "Autumn"
    else:
        return "Invalid month"

print(check_season("January"))

#6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(y2, y1, x2, x1):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope(4, 2, 2, 1))

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root)
    else:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return (root1, root2)
print(solve_quadratic_eqn(1, -3, 2))  

#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(elements):
    for element in elements:
        print(element)

print_list([1, 2, 3, 4, 5])

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(normal_array):
    reversed_array = []
    for i in range(len(normal_array) - 1, -1, -1):
        reversed_array.append(normal_array[i])
    return reversed_array

print(reverse_list([1, 2, "3", 4, 5]))

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items):
    capitalized_items = []
    for item in items:
        if type(item) is str:
            capitalized_items.append(item.capitalize())
        else:
            capitalized_items.append(item)
    return capitalized_items

print(capitalize_list_items(["apple", "banana", "cherry", 42, "date"]))

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(items, item):
    items.append(item)
    return items
print(add_item([1, 2, 3], 4))

#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(items, item):
    if item in items:
        items.remove(item)
    return items

print(remove_item([1, 2, 3, 4], 3))

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    if n < 0:
        return "Please enter a non-negative number."
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers(5))

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    if n < 0:
        return "Please enter a non-negative number."
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    if n < 0:
        return "Please enter a non-negative number."
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(10))