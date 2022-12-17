# T1A3 - Terminal App Assignment
## Stuart NIcoll

[My github link](https://github.com/stuartnicoll/T1A3)

__Overview__

My temainal app is a essentially a shopping list app which has a robot theme. It is run in a linear sequence and structurely is made up of four parts. Thesse are the intro, shopping list, a paper rock scissors game and finally another selection element.

__Minimum requirements__

Mac OS 10.11 or higher
2gb ram (4gb preferred)

Windows 7-10
2gb ram (4gb preferred)

Python 3.10 or above

__How to run the app__

To run this app open the terminal and from the root 
directory type:  

./run_list.sh

Follow the promts and enjoy!

__The main file__

The main file is fairly simple. I have basically written most of the code for each section and put that code onto their own seperate files. These files have their own functions which are called in sequence from the main file as needed. 

I have imported os from system to this file so that I could implement the system clear command from this file. Each code block I made has been imported and called from this page. They are as follows:

Intro
List
Paper, rock & scissor
and desert.

I will go into more details about each of these now.

__Intro__

The intro file intro.py has one function called intro it contains the following inports:

```
import time
from datetime import date
from os import system
```

The first part of this code block simply prints out a message contained within a while loop. Then the screen is cleared and a second message is added.

```
for i in range(1):
    print('''After many years humans and robots 
have managed to forge an uneasy alliance. 
The robots  have agreed to keep us to stay 
alive as long as we remain subservient and
obedient to them.  
''')
    time.sleep(4)

system('clear')

print()

for i in range(1):
    print("Welcome to the Robomart\n")
    print("The ultimate robot overlord shopping list experience!")
    time.sleep(3)
```
After that I added a feature where an Ascii image of a robot face is called from an external text file.

```
for i in range(1):
    with open('intro_read.txt', 'r') as f:
        f_contents = f.read()
        print(f_contents)
        input("Press enter to continue:\n")
```
Here I used the date time module to tell the user what todays date is with a print message as well. There is a delay added to several of the sections in the block to help create some level of control and dynamic tension as well.
```
    for i in range(1):
    todays_date = date.today()
    print("It is important to remind you that todays date is " ,todays_date, "human.")
    time.sleep(2)
```

Then I created a request from the user to enter their name. Once the name was entered this would be written onto an external text file. I then sent this back to the output as feedback to the user confirming their name to them.

```
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
```
    

After this I took the user name from the file and converted it into binary code. This was then printed back to the screen with a message for the user. And the cleared the screen. Ready for the Shopping list section.
```
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
```  
__The shopping list__

