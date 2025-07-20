def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    for i in range(len(cleaned) //2):
        if cleaned[i] != cleaned[-1 - i]:
         return False
    return True

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")