#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
def list_of_hexa_colors(num_colors=5):
    colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors
print(list_of_hexa_colors())

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors=5):
    colors = []
    for _ in range(num_colors):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colors.append(color)
    return ['RGB' + str(color) for color in colors]
print(list_of_rgb_colors(2))

#3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(num_colors=5, color_type='hex'):
    if color_type == 'hex':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "color_type must be either 'hex' or 'rgb'"
print(generate_colors(3, 'rgb'))