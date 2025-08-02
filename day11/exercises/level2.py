#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    if n < 0:
        return "Please enter a non-negative number."    
    evens = 0
    odds = 0    
    for i in range(n + 1) :
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return {"evens": evens, "odds": odds}

print(evens_and_odds(100))

#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n < 0:
        return "Please enter a non-negative number."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if isinstance(param, (list, dict, str, set)):
        return len(param) == 0
    return False

print(is_empty([]))

#4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(numbers):
    if not numbers:
        return "List is empty."
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    if not numbers:
        return "List is empty."
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def calculate_mode(numbers):
    if not numbers:
        return "List is empty."
    mode = max(set(numbers), key=numbers.count)
    return mode if numbers.count(mode) > 1 else "No mode found."

def calculate_range(numbers):
    if not numbers:
        return "List is empty."
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    if not numbers:
        return "List is empty."
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std(numbers):
    if not numbers:
        return "List is empty."
    variance = calculate_variance(numbers)
    return variance ** 0.5


   