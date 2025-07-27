#1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    #Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("Sorted Ages:", ages)
print("Min Age:", min_age)
print("Max Age:", max_age)

    # Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max:", ages)
    # Find the median age (one middle item or two middle items divided by two)
middle_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
print("Median Age:", median_age)

    # Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print("Average Age:", average_age)

    # Find the range of the ages (max minus min)
age_range = max_age - min_age
print("Age Range:", age_range)

    # Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print("Difference between Min and Average Age:", min_average_diff)
print("Difference between Max and Average Age:", max_average_diff)

#2. Find the middle country(ies) in the countries list
countries = [
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
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = countries[middle_index:middle_index + 1]
print("Middle Country/Countries:", middle_countries)

#3 Divide the countries list into two equal lists if it is even if not one more country for the first half
if len(countries) % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]
print("First Half of Countries:", first_half)
print("Second Half of Countries:", second_half)

#4. Unpack the first three countries and the rest as scandic countries.
theCountries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic_countries = theCountries[3:]
first_country, second_country, third_country = theCountries[:3]
print("First Country:", first_country)
print("Second Country:", second_country)
print("Third Country:", third_country)
print("Scandic Countries:", scandic_countries)