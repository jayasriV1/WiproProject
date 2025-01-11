import re
def isValidAadhaarNumber(text):
     patterns = '^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$'


        if re.search(patterns,  text):
                return 'valid adhar card no'
        else:
                return('Not valid adhar card no  ')



str1 = "3382 7607 8244"
print(isValidAadhaarNumber(str1))