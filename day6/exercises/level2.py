family_members = ("Koffi", "Charlie", "Alice", "kossiwa", "Papa", "Maman")

#1 Unpack siblings and parents from family_members
siblings, parents = family_members[:-2], family_members[-2:]
print("Siblings:", siblings)
print("Parents:", parents)

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "eggs")
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff:", food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0: 
    middle_items = food_stuff_tp[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_tp[middle_index:middle_index + 1]
print("Middle item(s):", middle_items)

#5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)

#6. Delete the food_staff_tp tuple completely
del food_stuff_tp
print("Food stuff tuple deleted.")

#7. Check if an item exists in tuple: - Check if 'Estonia' is a nordic country -Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway','Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is Estonia a nordic country?", is_estonia_nordic)
print("Is Iceland a nordic country?", is_iceland_nordic)