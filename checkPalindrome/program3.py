def is_palindrome(word):
    # Convert the string to lowercase and remove non-alphanumeric characters
    word = ''.join(e for e in s if e.isalnum()).lower()

    return word == word[::-1]


userWord = input("Enter a word or phrase: ")
if is_palindrome(userWord):
    print(f'"{userWord}" is a palindrome!')
else:
    print(f'"{userWord}" is not a palindrome.')
