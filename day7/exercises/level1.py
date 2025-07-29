it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1. Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Updated it_companies:", it_companies)

#3. Insert multiple IT companies at once to the set it_companies
more_companies = {'Snapchat', 'LinkedIn', 'Reddit'}
it_companies.update(more_companies)
print("After adding more companies:", it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print("After removing Oracle:", it_companies)

#5. What is the difference between remove and discard
# If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.