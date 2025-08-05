names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1. Explain the difference between map, filter, and reduce
# Map applies a function to each item in an iterable and returns a new iterable with the results.
# Filter applies a function to each item in an iterable and returns a new iterable with items that return True.
# Reduce applies a function cumulatively to the items of an iterable, reducing it to a single value.

#2. Explain the difference between higher order function, closure and decorator
# A higher order function is a function that takes another function as an argument or returns a function.
# A closure is a function that captures the lexical scope in which it was defined, allowing it to access variables from that scope even when called outside of it.
# A decorator is a higher order function that takes a function and extends its behavior without modifying its code.

#3. Define a call function before map, filter or reduce
def call(func, iterable):
    return func(lambda x: x.upper(), iterable)

map_call = list(call(map, names))


#4. Use for loop to print each country in the countries list.
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for country in countries:
    print(country)

#5. Use for to print each name in the names list.
for name in names:
    print(name)

#6. Use for to print each number in the numbers list
for number in numbers:
    print(number)