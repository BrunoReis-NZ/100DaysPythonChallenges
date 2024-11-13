import random

# Random Module Exercises

print("\n1. Generate a Random Integer")

# Use randint() to generate a random integer between 1 and 100. Print the result.

rand_int_1 = random.randint(1, 100)
print(rand_int_1)

print("\n2. Generate a Random Float")

# Use random() to generate a random float between 0 and 1. Print the result.

rand_float_1 = random.random()
print(rand_float_1)

print("\n3. Generate a Random Float within a Range")

# Use uniform() to generate a random float between 5.5 and 10.5. Print the result.

rand_float_2 = random.uniform(5.5, 10.5)
print(rand_float_2)

print("\n4. Random Choice from a List")

# Create a list of colors and use random.choice() to pick a random color from the list.

color_list = ["blue", "red", "yellow", "green", "pink", "gray"]
print(random.choice(color_list))

print("\n5. Random Choice from a Tuple")

# Create a tuple of numbers and use random.choice() to pick a random number from the tuple.

number_tuple = (1, 2, 3, 4, 5)
print(random.choice(number_tuple))

print("\n6. Shuffling a List")

# Create a list of numbers, then use random.shuffle() to randomly reorder the list.

number_list = [1, 2, 3, 4, 5]
print(number_list)
random.shuffle(number_list)
print(number_list)

# List Exercises

print("\n7. Create a List and Print an Element")

# Create a list with five different fruits. Print the third fruit.

fruits = ["apple", "Mandarin", "Grape", "Kiwi", "Mango"]
print(fruits[2])

print("\n8. Append an Element to a List")

# Create a list of animals, then add "elephant" to the list using append().

animals = ["lion", "hyppo", "giraffe", "gorilla"]
animals.append("Elephant")
print(animals)

print("\n9. Insert an Element at a Specific Position")

# Insert "giraffe" as the second element in a list of animals.

animals_2 = ["lion", "hyppo", "elephant", "gorilla"]
animals_2.insert(1, "giraffe")
print(animals_2)

print("\n10. Remove an Element from a List")

# Remove "lion" from a list of animals using remove().

animals_3 = ["lion", "hyppo", "elephant", "gorilla"]
animals_3.remove("lion")
print(animals_3)

print("\n11. Pop an Element from a List")

# Use pop() to remove the last element from a list of numbers and print it.

cars = ["Toyota", "Honda", "Ford", "Chevrolet"]
cars.pop()
print(cars)

print("\n12. Count Occurrences of an Element in a List")

# Create a list with duplicate elements and use count() to find how many times a specific element appears.

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(numbers.count(1))

print("\n13. Find the Index of an Element")

# Use index() to find the position of "banana" in a list of fruits.

fruits_2 = ["apple", "banana", "grape", "kiwi", "mango"]
print(fruits_2.index("banana"))

print("\n14. Sort a List")

# Create a list of 20 random numbers and use sort() to arrange them in ascending order.

numbers_2 = [3, 5, 1, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 19, 17, 15, 13, 11]
numbers_2.sort()
print(numbers_2)

print("\n15. Reverse a List")

# Create a list and use reverse() to reverse its order.

numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers_3.reverse()
print(numbers_3)

# Nested Lists Exercises

print("\n16. Create and Access a Nested List")

#Create a nested list with two inner lists, and access an element from the first inner list.

nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][0])

print("\n17. Append a List to a List")

# Create a list and append another list to it. Print the result.

program_languages_1 = ["Java", "C++", "C#"]
program_languages_2 = ["Python", "Javascript"]
program_languages_1.append(program_languages_2)
print(program_languages_1)

print("\n18.Extend a List with Another List")

# Use extend() to add all elements of one list to another list.

list_one = ["Volvo", "BMW", "Tesla"]
list_two = ["Holden", "Peugeot"]
list_one.extend(list_two)
print(list_one)

#Tuple Exercises

print("\n19. Create and Access a Tuple")

# Create a tuple with three items and print the second item.

colors = ("blue", "red", "Yellow")
print(colors[1])

print("\n20. Tuple Unpacking")

# Create a tuple with three numbers and unpack them into three variables. Print each variable.

tnumbers = (1, 2, 3)
a, b, c = tnumbers
print(a, b, c)

print("\n21. Convert a Tuple to a List")

# Convert a tuple to a list and add a new element to the list.

letters1 = ("a", "b", "c")
letters_lists = list(letters1)
letters_lists.append("d")
print(letters_lists)

print("\n22. Convert a List to a Tuple")

# Convert a list to a tuple and print the tuple.

letters2 = ["a", "b", "c", "d", "e"]
letters_tuple = tuple(letters2)
print(letters_tuple)

print("\n23. Check If an Item Exists in a Tuple")

# Use the in keyword to check if an element is in a tuple and print the result.

fruits2 = ["apple", "Mandarin", "Grape", "Kiwi", "Mango"]
print("banana" in fruits2)
print("Mandarin" in fruits2)




