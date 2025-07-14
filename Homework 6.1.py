import string

def letters_range(input_str):
    all_letters = string.ascii_letters
    start , end = input_str.split('-')
    start_index = all_letters.index(start)
    end_index = all_letters.index(end)
    result = all_letters[start_index:end_index+1]
    return result

user_input = input("Enter a letters ( example: h-r): ")
print(letters_range(user_input))
