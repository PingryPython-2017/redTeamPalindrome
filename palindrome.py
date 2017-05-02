### Function
def is_palindrome(string):
	"""Takes in a string and returns True if the string is a palindrome"""
	if len(string) <= 1: # This is the terminating case
		return True
	if string[0] == string[-1]: # This checkes if the first and last character of a list are the same
		return is_palindrome(string[1:len(string)-1])
	else:
		return False





