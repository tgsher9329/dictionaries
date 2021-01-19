# print out the menu for the user to follow

print('Electric Phone Book')
print('===================')
print('1. Look up an entry')
print('2. Set an entry')
print('3. Delete an entry')
print('4. List all entries')
print('5. Quit')

book = {}

while(True):

    userInput = input('What is it you need to do? (1-5)')
    
    if userInput == 1:
        
