import re
def text_match(text):
	patterns="^a(b+)"
	if re.search(patterns,text):
		return "found match!"
	else:
		return "Not matched"
print(text_match("ab"))
print(text_match("abc"))
print(text_match("abb"))
print(text_match("abcc"))
print(text_match("a"))
print(text_match("ac"))
