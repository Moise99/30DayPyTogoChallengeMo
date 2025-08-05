countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1. Use map to create a new list by changing each country to uppercase in the countries list
def to_uppercase(country):
    return country.upper()
uppercase_countries = list(map(to_uppercase, countries))

print("Uppercase Countries:", uppercase_countries)

#2. Use map to create a new list by changing each number to its square in the numbers list
def square(number):
    return number ** 2
squared_numbers = list(map(square, numbers))

print("Squared Numbers:", squared_numbers)

#3. Use map to change each name to uppercase in the names list
def uppercase_name(name):
    return name.upper()
uppercase_names = list(map(uppercase_name, names))

print("Uppercase Names:", uppercase_names)

#4. Use filter to filter out countries containing 'land'.
def contains_land(country):
    return 'land' in country.lower()
filtered_countries = list(filter(contains_land, countries))

print("Filtered Countries (contains 'land'):", filtered_countries)

#5. Use filter to filter out countries having exactly six characters.
def has_six_characters(country):
    return len(country) == 6
filtered_six_char_countries = list(filter(has_six_characters, countries))

print("Filtered Countries (exactly six characters):", filtered_six_char_countries)

#6. Use filter to filter out countries containing six letters and more in the country list.
def has_six_or_more_letters(country):
    return len(country) >= 6
filtered_six_or_more_countries = list(filter(has_six_or_more_letters, countries))

print("Filtered Countries (six letters or more):", filtered_six_or_more_countries)

#7. Use filter to filter out countries starting with an 'E'
def starts_with_e(country):
    return country.startswith('E')
filtered_countries_starting_with_e = list(filter(starts_with_e, countries))

print("Filtered Countries (starting with 'E'):", filtered_countries_starting_with_e)

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
def concatenate_names(name1, name2):
    return name1 + ' ' + name2
chained_result = reduce(concatenate_names, uppercase_names)

print("Chained Result (concatenated names):", chained_result)

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
string_items = get_string_lists(countries + names + numbers)

print("String Items from Combined List:", string_items)

#10. Use reduce to sum all the numbers in the numbers list.
def sum_numbers(x, y):
    return x + y
sum_of_numbers = reduce(sum_numbers, numbers)

print("Sum of Numbers:", sum_of_numbers)

#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

def concatenate_countries(country1, country2):
    if country1 == '':
        return country2
    elif country2 == countries[-1]:
        return f"{country1}, and {country2}"
    else:
        return f"{country1}, {country2}"
concatenated_countries = reduce(concatenate_countries, countries)

print("Concatenated Countries Sentence:", concatenated_countries, "are north European countries")

#Declare a function called categorize_countries that returns a list of countries with some common pattern eg 'land', 'ia', 'island', 'stan'

countries_list = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

def categorize_countries(countries_list, pattern):
    return list(filter(lambda country: pattern in country.lower(), countries_list))
categorized_countries = categorize_countries(countries_list, 'land')

print("Categorized Countries (contains 'land'):", categorized_countries)

#13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_starting_letter(countries_list):
    from collections import defaultdict
    letter_count = defaultdict(int)
    for country in countries_list:
        first_letter = country[0].upper()
        letter_count[first_letter] += 1
    return dict(letter_count)
country_letter_count = count_countries_by_starting_letter(countries_list)

print("Country Count by Starting Letter:", country_letter_count)

#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries list.
def get_first_ten_countries(countries_list):
    return countries_list[:10]
first_ten_countries = get_first_ten_countries(countries_list)

print("First Ten Countries:", first_ten_countries)

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries_list):
    return countries_list[-10:]
last_ten_countries = get_last_ten_countries(countries_list)
print("Last Ten Countries:", last_ten_countries)