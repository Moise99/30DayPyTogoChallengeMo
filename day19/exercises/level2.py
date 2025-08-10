#4. Extract all incoming email addresses as a list from the email_exchanges_big.txt file.
def extract_email_addresses(file_path):
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            email_addresses = []
            for line in file:
                if '@' in line:
                    parts = line.split()
                    for part in parts:
                        if '@' in part and '.' in part:
                            email_addresses.append(part.strip())
            return list(set(email_addresses))  # Return unique email addresses
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)
print(extract_email_addresses('../data/email_exchanges_big.txt'))

#5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order
# Your output should look like this
# print(find_most_common_words('sample.txt', 5))
# [(10, 'the'),
# (8, 'be'),
# (6, 'to'),
# (6, 'of'),
# (5, 'and')]

def find_most_common_words(source, top_n):
    from collections import Counter
    import re   
    try:
        if source.endswith('.txt'):
            with open(source, 'r', encoding='UTF-8') as file:
                text = file.read().lower()
        else:
            text = source.lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        most_common = word_counts.most_common(top_n)
        return most_common
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)
print(find_most_common_words('../data/obama_speech.txt', 5))
