import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')   # Pattern to search for - r'' means ignore \ escape chars,
                                                        # \d represents a digit
mo = phoneNumRegex.search(message)   # Search string for pattern defined, returns a match object
mo_2 = phoneNumRegex.findall(message)  # List of all occurrences

print(mo.group())  # mo.group tells you the actual text from object
print(mo_2)

print(mo.group(1))   # Parantheses seperates into groups


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo_3 = batRegex.search('Batmobile lost a wheel')
print(mo_3.group())

mo_4 = batRegex.search('Batbike lost a wheel')
print(mo_4)


beeRegex = re.compile(r'Bee(wo)?man')    # ? operator means preceding text can appear 1 or 0 times
mo_5 = beeRegex.search('The adventures of Beewoman')
print(mo_5.group())

beeRegex = re.compile(r'Bee(wo)*man')    # * means the group must appear 0 or more times, + is for 1 or more times
mo_5 = beeRegex.search('The adventures of Beeman')
print(mo_5.group())