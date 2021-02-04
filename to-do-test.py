print('Hi, David!')
print('Welcome back to your to-do list')  

thislist = ['Learn the basics of python', 'Learn the basics of vim', 'Play with PS4', 'Take a sh*t']
                                                                    
print('Number of items in your list: ' + str(len(thislist)))

print('Currently in your list are these items: ')
print(thislist)

newItem = input("Enter new item:")
print("Adding to the list: " + str(newItem))

if newItem:
    thislist.append(str(newItem))
    print(thislist)
else:
    print('Sorry, I did not quite get that. Please try again!')

    newItem = input("Enter new item:")
    print("Adding to the list: " + str(newItem))
    if newItem:
        thislist.append(str(newItem))
        print(thislist)
        
removeItem = input('Would you like to remove any items?')

if removeItem == 'yes' or 'Yes':
    remove = input('Ok, which one?' )
    if str(remove) in thislist:
        thislist.remove(remove)
        print(thislist)
    else:
        print('Sorry, I did not quite get that. Please try again!')
        remove = input('Ok, which one?')
        if str(remove) in thislist:
            thislist.remove(remove)
            print(thislist)

if removeItem == 'no' or 'No': 
    print('Ok.') 