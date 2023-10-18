# # Create a function that takes string as parameter and returns number of letters from that string.
# def string_to_letters(string):
#     letter_dict = {}
#     for letter in string:
#         if letter.isalpha():
#             letter_dict[letter] = letter_dict.get(letter, 0) + 1
#     return letter_dict

# # string_to_letters("kosmo sas")
# print(string_to_letters("  nd,anf,m5646sdafsa43345436$££%"))       

# def letters_in_string(string):
#     string_list = [sign for sign in string if sign.isalpha()]
#     return len(string_list)

# print(letters_in_string("   sdf 5456  657$dfsdfad%$%£"))

# def add_two_numbers(a: str, b: str) -> str:
#     print( a + b )

# add_two_numbers("9", "45")



# 1. Create at least 5 different functions by your own and test it

# def make_a_list(text: str) -> list:
#     return [sign for sign in text]

# def reverse_string(text: str) -> str:
#     return text[::-1]

# def count_length_string(text: str) -> int:
#     return len(text)

# def is_divided_by_three(number: int) -> bool:
#     return number % 3 == 0

# def what_type(varable) -> type:
#     return type(varable)

# 2. Create a function that adds a string ending to each member in a list.

# def add_string(string: str, list: list) -> list:
#     return [str(member) + string for member in list]

# 3. Create a mini python program which would take two numbers as an input and
#  would return their sum, subtraction, division, multiplication.

# def number_operations(num1: int, num2: int) -> tuple:
#     return num1 + num2, num1 - num2, num1 / num2, num1 * num2

# 4. Create a function that returns only strings with unique characters.

print(number_operations(1, 8))