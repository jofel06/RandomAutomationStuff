#! python 3
# To do a phone and email scraper

import re
import pyperclip

# TODO:Create a regex for phone number
phoneRE = re.compile(r'''
# Example 412-222-3333, 555-2222, (415) 222-333, 222,0000 ext 12345, ext.12345. x12345
(
((\d\d\d)|(\(\d\d\d))?    #area code optional
(\s|-)          #first separator
\d\d\d          #first 3 digits
(\s|-)          #seperator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x ) #extension word-part
(\d{2.5}))?      )   #extension number-part
''', re.VERBOSE)    #c:Verbose mode, can be used so you can add comments and new lines as part of the RE expression


# TODO:Create a regex for email
emailRE = re.compile(r'''
#Example some.+_thing@something.com

[a-zA-Z0-9._+]+    #name part
@                  #the @ symbol
[a-zA-Z0-9._+]+    #domain
''', re.VERBOSE)


# TODO:Get the text of the clipboard
text = pyperclip.paste()
# TODO:Extract the email and phone number from the text
extractedPhone = phoneRE.findall(text)
extractedEmail = emailRE.findall(text)

allphonenumber = []
for phonenumber in extractedPhone:
    allphonenumber.append(phonenumber[0])

# TODO:copy the extracted email and phone number to the clipboard
results = ','.join(allphonenumber) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print(results)