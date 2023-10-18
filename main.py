# Create a function that takes string as parameter and returns number of letters from that string.
def string_to_letters(string):
    letter_dict = {}
    for letter in string:
        if letter.isalpha():
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
    return letter_dict

string_to_letters("kosmo sas")
       
