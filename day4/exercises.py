# #1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
# string1 = 'Thirty'
# string2 = 'Days'
# string3 = 'Of'
# string4 = 'Python'
# space = ' '
# concatenated_string = string1 + space + string2 + space + string3 + space + string4
# print(concatenated_string)

# #2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# string21 = 'Coding'
# string22 = 'For'
# string23 = 'All'
# space2 = ' '
# concatenated_string2 = string21 + space2 + string22 + space2 + string23
# print(concatenated_string2)

#3 Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding For All"

#4. Print of the variable company using print().
print(company)

#5. Printing of the length of the company string using len() method and print()
print("The length of the company string is:", len(company))

#6. Change all the characters to uppercase letters using upper() method.
company_upper = company.upper()
print("Company in uppercase:", company_upper)

#7. Change all the characters to lowercase letters using lower() method
company_lower = company.lower()
print("Company in lowercase:", company_lower)

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string_capitalize = 'Coding For All'.capitalize()
string_title = 'Coding For All'.title()
string_swapcase = 'Coding For All'.swapcase()
print("Capitalized:", string_capitalize)
print("Title:", string_title)  
print("Swapcase:", string_swapcase)

#9. Cut(slice) out the first word of Coding For All string.
first_word = 'Coding For All'.split()[0]
print("First word:", first_word)

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.

if 'Coding For All'.find('Coding') != -1:
    print("The word 'Coding' is found in 'Coding For All'.")
else:
    print("The word 'Coding' is not found in 'Coding For All'.")

#11. Replace the word coding in the string 'Coding For All' to Python.
replaced_string = 'Coding For All'.replace('Coding', 'Python')
print("New string :", replaced_string)

#12. Change Python for Everyone to Python for All using the replace method or other methods.
replaced_string2 = 'Python for Everyone'.replace('Everyone', 'All')
print("Changed string:", replaced_string2)

#13. Split the string 'Coding For All' using space as the separator (split())
split_string = 'Coding For All'.split(' ')
print("Split string:", split_string)

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')
print("Companies list:", companies)

#15. What is the character at index 0 in the string Coding For All
character_at_index_0 = 'Coding For All'[0]
print("Character at index 0:", character_at_index_0)

#16. What is the last index of the string Coding For All
last_index = len('Coding For All') - 1
print("Last index of 'Coding For All':", last_index)

#17. What character is at index 10 in "Coding For All" string.
character_at_index_10 = 'Coding For All'[10]
print("Character at index 10:", character_at_index_10)

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'
words = 'Python For Everyone'.split()
acronym = ''.join(word[0].upper() for word in words)
print("Acronym for 'Python For Everyone':", acronym)

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
words_coding = 'Coding For All'.split()
acronym_coding = ''.join(word[0].upper() for word in words_coding)
print("Acronym for 'Coding For All':", acronym_coding)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
position_of_C = 'Coding For All'.index('C')
print("Position of first 'C' in 'Coding For All':", position_of_C)

#21. Use index to determine the position of the first occurrence of F in Coding For All.
position_of_F = 'Coding For All'.index('F')
print("Position of first 'F' in 'Coding For All':", position_of_F)

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
position_of_last_l = 'Coding For All People'.rfind('l')
print("Position of last 'l' in 'Coding For All People':", position_of_last_l)

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_of_because = sentence.find('because')
if position_of_because != -1:
    print("The word 'because' is found at index:", position_of_because)
else:
    print("The word 'because' is not found in the sentence.")

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
position_of_last_because = sentence.rindex('because')
print("The last occurrence of 'because' is at index:", position_of_last_because)

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_phrase = sentence[sentence.index('because'):sentence.rindex('because') + len('because')]
print("Sliced phrase:", slice_phrase)

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
position_of_first_because = sentence.find('because')
if position_of_first_because != -1:
    print("The first occurrence of 'because' is at index:", position_of_first_because)
else:
    print("The word 'because' is not found in the sentence.")

#27. (seems like is the question 25, just a remark from me (Moïse)) Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_phrase2 = sentence[sentence.index('because'):sentence.rindex('because') + len('because')]
print("Sliced phrase 2:", slice_phrase2)

#28. Does ''Coding For All' start with a substring Coding?
does_start_with_coding = 'Coding For All'.startswith('Coding')
if does_start_with_coding:
    print("'Coding For All' starts with 'Coding'.")
else:
    print("'Coding For All' does not start with 'Coding'.")

#29. Does 'Coding For All' end with a substring coding?
does_end_with_coding = 'Coding For All'.endswith('coding')
if does_end_with_coding:
    print("'Coding For All' ends with 'coding'.")
else:
    print("'Coding For All' does not end with 'coding'.")

#30. '   Coding For All      ' remove the left and right trailing spaces in the given string.
trailing_spaces_removed = '   Coding For All      '.strip()
print("String with trailing spaces removed:", trailing_spaces_removed)


#31. Which one of the following variables return True when we use the method isidentifier(): 1-30DaysOfPython 2-thirty_days_of_python
is_identifier_1 = '30DaysOfPython'.isidentifier()
is_identifier_2 = 'thirty_days_of_python'.isidentifier()
if is_identifier_1:
    print("'30DaysOfPython' is a valid identifier.")
else:
    print("'30DaysOfPython' is not a valid identifier.")
if is_identifier_2:
    print("'thirty_days_of_python' is a valid identifier.")
else:
    print("'thirty_days_of_python' is not a valid identifier.")

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print("Joined libraries:", joined_libraries)

#33. Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

#34. Use a tab escape sequence to write the following lines
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

#35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")


#36. Make the following using string formatting methods:
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')


