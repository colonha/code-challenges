def palindrome(word):
    word1 = ""
    word1 = word[::-1]
    if word == word1:
        print ("This is a palindrome")
    else:
        print ("This is not a palindrome")

if __name__ == "__main__":
    word = input("Enter a word: ")
    palindrome(word)