print(' ')
print('Welcome to your own password generator.')
print('I cant stress this enough: it is NOT a password manager!')
print(' ')

import string
import random

confirm = raw_input('Would you like to generate a password? ')

if confirm == 'yes' or 'Yes':
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print('Random string of length', length, 'is:', result_str)

    get_random_string(8) 
    get_random_string(16)
    get_random_string(32)

    print('Pick and choose from the passwords above, with 8, 16 nd 32 characters.')

elif confirm == 'no' or 'No':
    print('Ok.')