#Palindrome Checker (Using Stack Concept)
def is_palindrome(word):
    stack = []

    for char in word:
        stack.append(char)

    reversed_word = ""

    while stack:
        reversed_word += stack.pop()

    if word == reversed_word:
        print("Palindrome")
    else:
        print("Not a Palindrome")

word = input("Enter a word: ")
is_palindrome(word)