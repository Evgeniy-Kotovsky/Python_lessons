import string

def make_hashtag(text):
    clean_text = ''.join(char for char in text if char not in string.punctuation)

    words = clean_text.split()
    capitalized = [word.capitalize() for word in words]

    hashtag = '#' + ''.join(capitalized)

    return hashtag[:140]


user_input = input("Enter a string: ")
result = make_hashtag(user_input)
print(result)
