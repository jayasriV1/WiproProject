import re
def is_Valid_PAN_number(text):
	patterns='^[A-Z]{5}[0-9]{4}[A-z]{1}$'
	if re.search(patterns, text):
		return 'is valid PAN number!'
	else:
		return 'is not valid PAN number!'
print(is_Valid_PAN_number("GVNPP8145P"))
print(is_Valid_PAN_number("9VNPP8905P"))
print(is_Valid_PAN_number("0VNPP8235P"))
print(is_Valid_PAN_number("HANIP8342P"))