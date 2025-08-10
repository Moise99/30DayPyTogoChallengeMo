#Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            num_lines = len(content)
            num_words = sum(len(line.split()) for line in content)
            return 'line', num_lines, 'words', num_words
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)
    

#a) Read obama_speech.txt file and count number of lines and words
print(count_lines_and_words('../data/obama_speech.txt'))
#b) Read michelle_obama_speech.txt file and count number of lines and words
print(count_lines_and_words('../data/michelle_obama_speech.txt'))
#c) Read donald_speech.txt file and count number of lines and words
print(count_lines_and_words('../data/donald_speech.txt'))
#d) Read melina_trump_speech.txt file and count number of lines and words
print(count_lines_and_words('../data/melina_trump_speech.txt'))

#2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
def most_spoken_languages(file_path, top_n):
    

    try:
        with open(file_path, 'r', encoding = 'UTF-8') as file:
            data = json.load(file)
            languages_count = {}
            
            for country in data:
                languages = country.get('languages', [])
                for language in languages:
                    if language in languages_count:
                        languages_count[language] += 1
                    else:
                        languages_count[language] = 1
            # Sort languages by count and get the top 10
            sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
            top_languages = sorted_languages[:top_n]
            return top_languages
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Error decoding JSON."
    except Exception as e:
        return str(e)
    
# Read the countries_data.json file and find the ten most spoken languages
print(most_spoken_languages('../data/countries_data.json', 3))

#3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
# Your output should look like this
# print(most_populated_countries(filename='./data/countries_data
# .json', 10))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population':
# 323947000},
# ]
def most_populated_countries(file_path, top_n):
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            countries_population = []
            for country in data:
                name = country.get('name', 'Unknown')
                population = country.get('population', 0)
                countries_population.append({'country': name, 'population': population})
            # Sort countries by population and get the top n
            sorted_countries = sorted(countries_population, key=lambda x: x['population'], reverse=True)
            top_countries = sorted_countries[:top_n]
            return top_countries
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Error decoding JSON."
    except Exception as e:
        return str(e)
# Read the countries_data.json file and find the ten most populated countries
print(most_populated_countries('../data/countries_data.json', 3))


