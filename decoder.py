print(' ')
print('Welcome!')
username = raw_input('Enter your username here: ')

if username == 'David' or 'david':
    password = raw_input('Enter your password here, ' + str(username) + ': ')
else:
    print('You are not allowed to enter. Not right clearance, ' + str(username))
                               
if password == 'migoxilla':                  
    print(' ')
    print('Welcome, David, to your decoder!')

    message = raw_input('Please enter your message here: ')
    confirm = raw_input('Confirm that this is the message you want ot decode by typing Yes. If it is not, type No. ')

    if confirm == 'Yes' or 'yes':
        decoded_message = message.replace('13e', 'a').replace('wfug', 'h').replace('sid', 'b').replace('ldj', 'e').replace('vzh8', 't').replace('1q0b', 'o').replace('ap4', 'i')   
        print(decoded_message)
        print('Message has been successfully decoded! ')     
    elif confirm == 'No' or 'no':
        message = raw_input('Please enter your message here again: ')
        confirm = raw_input('Confirm that this is the message you want to decode by typing Yes. If its not, type No. ')

    if confirm == 'Yes' or 'yes':     
        decoded_message = message.replace('13e', 'a').replace('wfug', 'h').replace('sid', 'b').replace('ldj', 'e').replace('vzh8', 't').replace('1q0b', 'o').replace('ap4', 'i')
        print(decoded_message)
        print('Message has been successfully decoded! ')
    else:
        pass