print('Hi, David!')     
print('Welcome back to your to-do list')  

thislist = ['Learn the basics of python', 'Learn the basics of nvim', 'Play with PS4', 'Take a sh*t']
                                                                    
print('Number of items in your list: ')
print(len(thislist))

print('Currently in your list are these items: ') 
               
print(thislist)

print('Your number of tasks is ' + str(len(thislist)))

x = 'Your number of tasks is '
y = str(len(thislist))
z = x + y

print(z)

newItem = raw_input("Enter new item:")
print("Username is: " + str(newItem))