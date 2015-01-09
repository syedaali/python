__author__ = 'syedaali'

'''
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
 check them according to the above criteria. Passwords that match the criteria
  are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''

import string

s = raw_input()

p = []

p = s.split(',')

is_password = []

for word in p:
    if any(c.isupper() for c in word):
        if any(c.islower() for c in word):
            if any(c.isdigit() for c in word):
                if any(c in '$#@' for c in word):
                    if len(word) >= 6:
                        if len(word) <= 12:
                            is_password.append(word)


print is_password
