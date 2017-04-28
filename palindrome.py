def is_palindrome(string):
	"""Takes in a string and returns True if the string is a palindrome"""
	if len(string) <= 1:
		return True
	if string[0] == string[-1]:
		return is_palindrome(string[1:len(string)-1])
	else:
		return False

### Tests

print("tacocat is a plandrome: {}. ".format(is_palindrome("tacocat")))
print("racecar is a plandrome: {}. ".format(is_palindrome("racecar")))
print(" is a plandrome: {}. ".format(is_palindrome("")))
print("qwer is a plandrome: {}. ".format(is_palindrome("qwer")))
print("e is a plandrome: {}. ".format(is_palindrome("e")))
print("uu is a plandrome: {}. ".format(is_palindrome("uu")))
print("ho is a plandrome: {}. ".format(is_palindrome("ho")))