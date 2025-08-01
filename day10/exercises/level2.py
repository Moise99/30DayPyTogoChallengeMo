#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    print(i)
    sum += i

print("Sum of all numbers from 0 to 100 is:", sum)

#1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0
for i in range(101):
    print(i)
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("Sum of all even numbers from 0 to 100 is:", sum_even)
print("Sum of all odd numbers from 0 to 100 is:", sum_odd)