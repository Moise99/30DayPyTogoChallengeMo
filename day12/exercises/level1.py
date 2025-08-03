#1. Write a function which generates a six digit/character random_user_id.
import random
def generate_random_user_id():
    return ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))
print(generate_random_user_id())

#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for each user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=num_chars))
        user_ids.append(user_id)
    return user_ids
print(user_id_gen_by_user())

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
print(f'RGB: {rgb_color_gen()}')