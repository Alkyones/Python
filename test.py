import re


strn = "11+221+3+1+2+1"


first_res = re.findall("[0-9]+\\s*|[+-/*]\\s*", strn)
print(first_res)

valid_not_valid = re.findall("^([0-9][+-/*])", strn)

if valid_not_valid : print('Invalid')
else: print('Valid')