#1. Declare an empty list
my_list = []

#2. Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3. Find the length of your list
list_length = len(my_list)

#4. Get the first item, the middle item and the last item of the list
first_item = my_list[0]

middle_index = list_length // 2
middle_item = my_list[middle_index]

last_item = my_list[-1]

print(f"First item: {first_item}, Middle item: {middle_item}, Last item: {last_item}")

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Togo Python", 30, 5.9, "Single", "Agoe Assiyéyé"]

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7. Print the list using print()
print("IT Companies:", it_companies)

#8. Print the number of companies in the list
number_of_companies = len(it_companies)

print("Number of IT Companies:", number_of_companies)

#9. Print the first, middle and last company
first_company = it_companies[0]

middle_index = number_of_companies // 2
middle_company = it_companies[middle_index]

last_company = it_companies[-1]

print(f"First company: {first_company}, Middle company: {middle_company}, Last company: {last_company}")

#10. Print the list after modifying one of the companies
it_companies[0] = "Instagram"
print("Modified IT Companies:", it_companies)

#11. Add an IT company to it_companies
it_companies.append("TikTok")
print("After adding TikTok:", it_companies)

#12. Insert an IT company in the middle of the companies list
middle_index = number_of_companies // 2
it_companies.insert(middle_index, "Ubuntu")
print("After inserting Ubuntu:", it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print("After changing Google to uppercase:", it_companies)

#14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print("Joined IT Companies:", joined_companies)

#15. Check if a certain company exists in the it_companies list.
company_to_check = "Apple"
if company_to_check in it_companies:    
    print(f"{company_to_check} exists in the IT Companies list.")       
else:
    print(f"{company_to_check} does not exist in the IT Companies list.")


#16. Sort the list using sort() method
it_companies.sort()
print("Sorted IT Companies:", it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("Reversed IT Companies:", it_companies)

#18. Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print("First three IT Companies:", first_three_companies)

#19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Last three IT Companies:", last_three_companies)

#20. Slice out the middle IT company or companies from the list
number_of_companies = len(it_companies)
if number_of_companies % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = it_companies[middle_index:middle_index + 1]
print("Middle IT Company/Companies:", middle_companies)

#21. Remove the first IT company from the list
it_companies.pop(0)
print("After removing the first company:", it_companies)

#22. Remove the middle IT company or companies from the list
if number_of_companies % 2 == 0:
    it_companies.pop(middle_index - 1)
else:
    it_companies.pop(middle_index)
print("After removing the middle company/companies:", it_companies)

#23. Remove the last IT company from the list
it_companies.pop(-1)
print("After removing the last company:", it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print("After clearing the list, IT Companies:", it_companies)

#25. Destroy the IT companies list
del it_companies
print("IT Companies list has been destroyed.")

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print("Full Stack Technologies:", full_stack)