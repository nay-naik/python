def is_palindrome(word):
    word = word.replace(" ", "").lower()

    reversed_string = word[::-1]

    # Comparing the original string post reverse
    return word == reversed_string


userWord = input("Enter a word or phrase: ")
if is_palindrome(userWord):
    print(f'"{userWord}" is a palindrome!')
else:
    print(f'"{userWord}" is not a palindrome.')
