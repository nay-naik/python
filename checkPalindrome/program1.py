def is_palindrome(word):
    # Removes the spaces and converts the word to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()

    length = len(word)

    # Check for palindrome by comparing characters from start to end and end to start
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True


userWord = input("Enter a word or phrase: ")
if is_palindrome(userWord):
    print(f'"{userWord}" is a palindrome!')
else:
    print(f'"{userWord}" is not a palindrome.')
