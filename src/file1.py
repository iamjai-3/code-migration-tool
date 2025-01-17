import random


def deposit(balance, amount):
    if amount > 0:
        balance += amount
        return f"Deposited ${amount}. New balance: ${balance}"
    return "Amount must be positive"


def withdraw(balance, amount):
    if amount > 0:
        if balance >= amount:
            balance -= amount
            return f"Withdrew ${amount}. New balance: ${balance}"
        return "Insufficient funds"
    return "Amount must be positive"


def calculate_area_of_circle(radius):
    if radius > 0:
        return 3.14159 * radius**2
    return "Radius must be positive"


def generate_random_password(length):
    if length > 0:
        characters = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        )
        return "".join(random.choice(characters) for _ in range(length))
    return "Length must be positive"


def reverse_string(s):
    return s[::-1]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n):
    if n <= 0:
        return []
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")


def find_max(numbers):
    if numbers:
        return max(numbers)
    return "List is empty"


def factorial(n):
    if n < 0:
        return "Number must be non-negative"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def check_palindrome(s):
    return s == s[::-1]


def merge_two_lists(list1, list2):
    return list1 + list2


def sort_numbers(numbers):
    return sorted(numbers)


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_even_numbers(limit):
    return [num for num in range(limit + 1) if num % 2 == 0]


def convert_to_uppercase(s):
    return s.upper()


def calculate_bmi(weight, height):
    if height <= 0:
        return "Height must be positive"
    return weight / (height**2)


def count_words(s):
    return len(s.split())


def find_min(numbers):
    if numbers:
        return min(numbers)
    return "List is empty"


def remove_duplicates(numbers):
    return list(set(numbers))


def calculate_power(base, exponent):
    return base**exponent


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def square_numbers(numbers):
    return [num**2 for num in numbers]


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def sum_of_list(numbers):
    return sum(numbers)


def average_of_list(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    return "List is empty"


def generate_multiplication_table(number, limit):
    return [number * i for i in range(1, limit + 1)]


def reverse_list(lst):
    return lst[::-1]


def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())


def find_unique_elements(lst):
    return list(set(lst))


def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def count_occurrences(lst, value):
    return lst.count(value)


def get_unique_vowels(s):
    return set(char for char in s.lower() if char in "aeiou")


def calculate_speed(distance, time):
    if time <= 0:
        return "Time must be positive"
    return distance / time


def multiply_list(numbers, multiplier):
    return [num * multiplier for num in numbers]


def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two elements"
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
