### Function
def is_palindrome(string):
	"""Takes in a string and returns True if the string is a palindrome"""
	if len(string) <= 1:
		return True
	if string[0] == string[-1]:
		return is_palindrome(string[1:len(string)-1])
	else:
		return False

### Tests

"""print("tacocat is a palindrome: {}. ".format(is_palindrome("tacocat")))
print("racecar is a palindrome: {}. ".format(is_palindrome("racecar")))
print(" is a palindrome: {}. ".format(is_palindrome("")))
print("qwer is a palindrome: {}. ".format(is_palindrome("qwer")))
print("e is a palindrome: {}. ".format(is_palindrome("e")))
print("uu is a palindrome: {}. ".format(is_palindrome("uu")))
print("ho is a palindrome: {}. ".format(is_palindrome("ho")))
"""

### Main Program
word = input("Give me a word, and I will tell you if it is a palindrome. ")
print('"{}" is a palindrom: {}'. format(word,is_palindrome(word)))