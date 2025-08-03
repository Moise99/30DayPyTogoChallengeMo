#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
print(shuffle_list([1, 2, 3, 4, 5]))

#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())