A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1. Join A and B
A_B_joined = A.union(B)
print("Joined A and B:", A_B_joined)

#2. Find A intersection B
A_B_intersection = A.intersection(B)
print("Intersection of A and B:", A_B_intersection)

#3. Is A subset of B
is_A_subset_of_B = A.issubset(B)
print("Is A a subset of B?", is_A_subset_of_B)

#4. Are A and B disjoint sets
are_A_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_A_B_disjoint)

#5. Join A with B and B with A
A_B_joined_2 = A.union(B)
B_A_joined = B.union(A)
print("Joined A with B and B with A:", A_B_joined_2)
print("Joined B with A:", B_A_joined)

#6. What is the symmetric difference between A and B
symmetric_difference_A_B = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference_A_B)

#7. Delete the sets completely
A.clear()
B.clear()
print("Sets A and B after clearing:", A, B)
