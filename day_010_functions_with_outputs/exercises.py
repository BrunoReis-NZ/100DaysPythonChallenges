# Basic Functions with Outputs

print("\n1. Simple Greeting. \n"
      "Write a function greet(name) that returns a string \"Hello, [name]!\".")

def greet(name):
    return f"Hello, {name}"

print(greet("Bruno"))

print("\n2. Addition. \n"
      "Write a function add(a, b) that returns the sum of two numbers.")

def add(a, b):
    return a + b

print(add(3, 7))

print("\n3. Square of a Number. \n"
      "Write a function square(num) that returns the square of a number.")

def square(num):
    return num * num

print(square(7))

print("\n4. Convert Celsius to Fahrenheit. \n"
      "Write a function to_fahrenheit(celsius) that returns the Fahrenheit equivalent of a Celsius temperature. \n"
      "(Formula: F = C * 9/5 + 32)")

def to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5) + 32)
    return fahrenheit

print(to_fahrenheit(17))

print("\n5. Calculate Area and Perimeter. \n"
      "Write a function rectangle_properties(length, width) that returns both the area and perimeter of a rectangle.")

def rectangle_properties(length, width):
    area = length * width
    perimeter = (2 * (length * width))
    return area, perimeter

area, perimeter = rectangle_properties(4, 9)
print(f"The area is {area} and the perimeter is {perimeter}")

# Intermediate Functions with Outputs

print("\n6. Determine if a Number is Even or Odd. \n"
      "Write a function is_even(num) that returns True if a number is even and False otherwise.")

def is_even(num):
    return num % 2 == 0

print(is_even(1))  # False
print(is_even(10))  # True

print("\n7. Check for a Prime Number. \n"
      "Write a function is_prime(num) that returns True if the number is prime and False otherwise.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(10))  # False

print("\n8. Find the Largest of Three Numbers. \n"
      "Write a function find_largest(a, b, c) that returns the largest of three numbers.")

def find_largest(a, b, c):
    return max(a, b, c)

print(find_largest(17, 66, 18))

print("\n9. Split a String into Words. \n"
      "Write a function split_sentence(sentence) that takes a sentence and returns a list of words.")

def split_sentence(sentence):
    return sentence.split()

print(split_sentence("This is a test sentence, with a comma."))

print("\n10. Calculate Discounted Price. \n"
      "Write a function apply_discount(price, discount) that returns the discounted price.")

def apply_discount(price, discount):
    return price - (price * (discount / 100))

print(apply_discount(100, 20))

print("\n11. Find All Factors of a Number. \n"
      "Write a function find_factors(num) that returns a list of all factors of a number.")

def find_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

print(find_factors(16))

# Advanced Functions with Outputs

print("\n12. Validate a Password. \n"
      "Write a function validate_password(password) that returns True \n"
      "if the password meets the criteria (at least 8 characters, n\
      contains both letters and numbers) and False otherwise.")

def validate_password(password):
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    return len(password) >=8 and has_letter and has_number

print(validate_password("Bruno8554#"))
print(validate_password("Bruno34"))

print("\n13. Count Vowels and Consonants. \n"
      "Write a function count_vowels_consonants(string) that returns the count of vowels and consonants in a string.")

def count_vowels_consonants(string):
    vowels = "aeiouy"
    v_count = sum(1 for char in string.lower() if char in vowels)
    c_count = sum(1 for char in string.lower() if char.isalpha() and char not in vowels)
    return v_count, c_count

print(count_vowels_consonants("Hello, world!"))

print("\n14. Find the Longest Word in a Sentence. \n"
      "Write a function longest_word(sentence) that returns the longest word in a sentence.")

def longest_word(sentence):
    words_in_sentence = sentence.split()
    return max(words_in_sentence, key=len)

print(longest_word("Find the longest word in this sentence"))

print("\n15. Generate a Dictionary of Squares. \n"
      "Write a function generate_squares(n) that returns a dictionary with numbers from 1 to n as keys and their squares as values.")

def generate_squares(n):
    return {i: i ** 2 for i in range(1, n + 1)}

print(generate_squares(10))
