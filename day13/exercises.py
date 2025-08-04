#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)

#2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flattened_list)

#3. Using list comprehension create the following list of tuples:
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

#4. Flatten the following list to a new list to have output output:[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway','Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), city.upper()] for country, city in (item[0] for item in countries)]

print(flattened_countries)

#5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
countries_dicts = [{'country': country.upper(), 'city': city.upper()} for country, city in (item[0] for item in countries)]
print(countries_dicts)

#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name[0]) for name in names]

print(concatenated_names)