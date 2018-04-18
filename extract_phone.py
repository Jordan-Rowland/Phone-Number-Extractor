import re
from pyperclip import paste

def extract_all_phones(input):
    phone_regex = re.compile(r'((\d{3}|\(\d{3}\))( |-|.)?\d{3}(-| |.)\d{4})')
    match = phone_regex.findall(input)
    for number in match:
        print(number[0])    

print(extract_all_phones(paste()))