#1 Create an empty tuple
empty_tuple = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Koffi", "Charlie")
sisters = ("Alice", "kossiwa")

#3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
#4. How many siblings do you have?
number_of_siblings = len(siblings)
print("Number of siblings:", number_of_siblings)

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Papa", "Maman")
print("Family members:", family_members)
