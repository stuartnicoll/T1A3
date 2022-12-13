import time
from datetime import date
from os import system

def intro():
    for i in range(1):
        print()
        time.sleep(2)

for i in range(1):
    print('''After many years humans and AI have 
managed to forge an uneasy alliance. AI have agreed to 
help us to stay alive as long as we remain subservient and
obediant to them.  
''')
    time.sleep(4)

system('clear')

print()

for i in range(1):
    print("Welcome to the Robomart\n")
    print("The ultimate robot overlord shopping list experience!")
    time.sleep(3)

print()

for i in range(1):
    with open('intro_read.txt', 'r') as f:
        f_contents = f.read()
        print(f_contents)
        input("Press enter to continue:\n")

    
    with open ('intro_write.txt', 'w') as g:
        text = input("Please enter your name: ")
        g.write(text)
        
    with open('intro_write.txt', 'r') as f:
        f_contents = f.read()
        print() 
        print("Welcome "+f_contents+".")
        print()
        time.sleep(3)
for i in range(1):
    todays_date = date.today()
    print("It is important to remind you that todays date is " ,todays_date, "human.")
    time.sleep(2)

string = (text)
result = ' '.join(format(ord(i),'b')for i in string)

for i in range(1):
    print()
    print("Your official robot name is: \n")
    print(result)
    print()
    print("Please take note of this for future reference.\n")
    input("Please press enter to continue. We dare you! ")
    time.sleep(2)

system('clear')
