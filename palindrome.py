def is_palindrome(string):
	"""Takes in a string and returns True if the string is a palindrome"""
	if len(string) <= 1:
		return True
	if string[0] == string[-1]:
		return is_palindrome(string[1:len(string)-1])
	else:
		return False
