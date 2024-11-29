# Functions with Inputs

print("\n1. Simple Greeting. \n"
      "Write a function greet(name) that takes a name as input and prints a greeting: 'Hello, [name]!'")

def greet(name):
    print(f"Hello, {name}!")

greet("Bruno")

# ***

print("\n2. Personalized Age Message. \n"
      "Write a function age_message(name, age) that prints: '[Name], you are [age] years old!'")

def age_message(name, age):
    print(f"{name}, you are {age} years old!")

age_message("Bruno", 47)

# ***

print("\n3. Sum of Two Numbers. \n"
      "Write a function add_numbers(a, b) that takes two numbers as inputs and prints their sum.")

def add_numbers(a, b) :
    print(f"The sum of {a} and {b} is = {a + b}")

add_numbers(4,5)

# ***

print("\n4. Temperature Conversion. \n"
      "Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit \n"
      "as input and prints its Celsius equivalent. (Formula: (F - 32) * 5/9).")

def convert_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} degrees in Fahrenheit equals to {celsius} degrees Celsius.")

convert_to_celsius(32)

# ***

print("\n5. User-Defined Multiplication Table. \n"
      "Write a function multiplication_table(number, limit) that prints \n"
      "the multiplication table of a given number up to the specified limit.")

def multiplication_table(number, limit):

    for i in range(1, limit+1):
        print(f"{number} * {i} = {number * i}")

multiplication_table(2, 100)

# Positional vs Keyword Arguments

print("\n6. Movie Ticket Price. \n"
      "Write a function ticket_price(movie, price) that prints: \"The price of a ticket for [movie] is $[price]\". \n"
      "Call the function using positional and keyword arguments.")

def ticket_price(movie, price):
    print(f"The price of a ticket for \"{movie}\" is ${price}")

ticket_price("Shark", 12)
ticket_price(price=12, movie="Shark")

# ***

print("\n7. Personal Introduction. \n"
      "Write a function introduce(name, age, city) that prints: \n\"Hi, my name is [name], I am [age] years old, and I live in [city].\". \n"
      "Call the function using positional and keyword arguments.")

def introduce(name, age, city):
    print(f"Hi, my name is {name}, I am {age} years old, and I live in {city}.")

introduce("Bruno", 47, "Wellington")
introduce(city="Wellington", name="Bruno", age=47)

# ***

print("\n8. Book Details. \n"
      "Write a function book_info(title, author, year) that prints: \"[Title] by [Author], published in [Year].\". \n"
      "Call the function using positional and keyword arguments.")

def book_info(title, author, year):
    print(f"{title} by {author}, published in {year}.")

book_info("O Bem Amado", "Dias Gomes", 1973)
book_info(year=1973, author="Dias Gomes", title="O Bem Amado")

# ***

print("\n9. Book Details. \n"
      "Write a function order_coffee(size, type, sugar_level=\"Medium\") that prints: \n"
      "You ordered a [size] [type] coffee with [sugar_level] sugar."
      "Call the function using positional and keyword arguments.")

def order_coffee(size, type, sugar_level="Medium"):
    print(f"You ordered a {size} {type} coffee with {sugar_level} sugar.")

order_coffee("Large", "Latte")
order_coffee(type="Espresso", size="Small", sugar_level="Low")

# ***

print("\n10. Calculate Discount. \n"
      "Write a function apply_discount(price, discount=10) that prints the discounted price after applying the discount percentage.")

def apply_discount(price, discount=10):
    discounted_price = price - (price * discount / 100)
    print(f"The discounted price is: ${discounted_price:.2f}")

apply_discount(1000)
apply_discount(1000, 20)
apply_discount(discount=25, price=700)

# ***

print("\n11. Trip Cost Calculator. \n"
      "Write a function trip_cost(distance, fuel_cost, mileage=15) \n"
      "that calculates and prints the total cost of a trip. \n"
      "(Formula: (distance / mileage) * fuel_cost)")

def trip_cost(distance, fuel_cost, mileage=15):
    trip_cost = (distance / mileage) * fuel_cost
    print(f"The trip cost was: {trip_cost:.2f}.")

trip_cost(600, 2.36)
trip_cost(600, 2.36, mileage=9)

# ***

print("\n12. Gym Membership Fee. \n"
      "Write a function membership_fee(months, fee_per_month=50) that calculates and prints the total membership cost.")

def membership_fee(months, fee_per_month=50):
    total_fee = months * fee_per_month
    print(f"The total membership fee for {months} months is ${total_fee}.")

membership_fee(6)
membership_fee(12, fee_per_month=45)

# ***

print("\n13. Favorite Things. \n"
      "Write a function favorite_things(person, *args) \n"
      "that prints the person's name followed by their list of favorite things.")

def favorite_things(person, *args):
    print(f"{person}'s favorite things are:")
    for thing in args:
        print(f"- {thing}")

favorite_things("Bruno", "Read comix", "Watch series", "Coding")

# ***

print("\n14. Multi-Currency Conversion. \n"
      "Write a function convert_currency(amount, rate, currency=\"USD\") that prints the converted amount.")

def convert_currency(amount, rate, currency1="NZD", currency2="USD"):
    converted = amount * rate
    print(f"{amount} {currency1} is equal to {converted:.2f} {currency2}")

convert_currency(750, 0.59)
