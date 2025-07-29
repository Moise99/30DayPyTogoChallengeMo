age = [22, 19, 24, 25, 26, 24, 25, 24]
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
length_age_list = len(age)
length_age_set = len(ages_set)
print("Length of age list:", length_age_list)
print("Length of age set:", length_age_set)

if length_age_list > length_age_set:
    print("List is bigger than set.")
elif length_age_list < length_age_set:
    print("Set is bigger than list.")
else:
    print("List and set are of equal length.")

#2 Explain the difference between the following data types: string, list, tuple and set
# String: A sequence of characters enclosed in quotes, used to represent text.
# List: An ordered collection of items that can contain duplicates and is mutable (can be changed).
# Tuple: An ordered collection of items that can contain duplicates but is immutable (cannot be changed).
# Set: An unordered collection of unique items, which does not allow duplicates and is mutable. 

#3I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("Unique words in the sentence:", unique_words)