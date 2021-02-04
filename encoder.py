print(' ')
print('Welcome!')
username = raw_input('Enter your username here: ')

if username == 'David' or 'david':
    password = raw_input('Enter your password here, ' + str(username) + ': ')
else:
    print('You are not allowed to enter. Not right clearance, ' + str(username))
                               
if password == 'migoxilla':                  
    print(' ')
    print('Welcome, David, to your encoder!')    

    message = raw_input('Please enter your message here: ')    
    confirm = raw_input('Confirm that this is your message by typing Yes. If its not, type No. ')    

    if confirm == 'Yes' or 'yes':    
        encoded_message = message.replace('a', '13e').replace('h', 'wfug').replace('b', 'sid').replace('e', 'ldj').replace('t', 'vzh8').replace('o', '1q0b').replace('i', 'ap4')    
        print(encoded_message)    
        print('Message has been successfully been encoded! ')    
    elif confirm == 'No' or 'no':                                                             
        message = raw_input('Please enter your message here again: ')
        confirm = raw_input('Confirm that this is your message by typing Yes. If its not, type No. ')    
                                         
        if confirm == 'Yes' or 'yes':    
                encoded_message = message.replace('a', '13e').replace('h', 'wfug').replace('b', 'sid').replace('e', 'ldj').replace('t', 'vzh8').replace('o', '1q0b').replace('i', 'ap4')
                print(encoded_message)
                print('Message has been successfully encoded! ')
        else:    
            pass    

else:    
    password = raw_input('Re-enter your password, it was incorrect: ')    

    if password == 'migoxilla':    
        print('Welcome, David, to your encoder!')    

        message = raw_input('Please enter your message here: ')    
        confirm = raw_input('Confirm that this is your message by typing Yes. If its not, type No. ')    

        if confirm == 'Yes' or 'yes':    
            encoded_message = message.replace('a', '13e').replace('h', 'wfug').replace('b', 'sid').replace('e', 'ldj').replace('t', 'vzh8').replace('o', '1q0b').replace('i', 'ap4')    
            print(encoded_message)    
            print('Message has been successfully been encoded! ')    
        elif confirm == 'No' or 'no':    
            message = raw_input('Please enter your message here again: ')    
            confirm = raw_input('Confirm that this is your message by typing Yes. If its not, type No. ')    

            if confirm == 'Yes' or 'yes':    
                encoded_message = message.replace('a', '13e').replace('h', 'wfug').replace('b', 'sid').replace('e', 'ldj').replace('t', 'vzh8').replace('o', '1q0b').replace('i', 'ap4')    
                print(encoded_message)    
                print('Message has been successfully encoded! ')    
            else:    
                pass
 