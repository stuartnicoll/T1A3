#Make a function to create shopping list called main menu
#Make a set of conditional statements
#Create a variable called shopping list
#create a function for each selection to perform


#Make a function to create shopping list called main menu
def main_menu():
    while True:
        print()
        print('''Welcome to your shopping list!

        Welcome back human what task would you like to perform?

        1.View the shopping list
        2.Add an item
        3.Remove an item
        4.Check if an item is still there
        5.How many items do you have to carry
        6.Remove all the contents
        7.Exit
        ''')
        selection = input("Make your choice human: ")
#Make a set of conditional statements
   

        if selection == "1":
            display_list()
        
        elif selection == "2":
            add_item()

        elif selection == "3":
            remove_item()
        
        elif selection == "4":
            check_item()
        
        elif selection == "5":
            list_length()
        
        elif selection == "6":
            clear_list()
        
        elif selection == "7":
            #system('clear')
            print("You are done with me human!")
            break

        else:
            print("You have failed to make the right selection human!")
            
#Create a variable called shopping list
shopping_list = ["Cheese", "Bread", "Wine", "Chocolate"]
#create a function for each selection to perform
def display_list():
    print()
    print("---Shopping List---")
    for i in shopping_list:
        print("* " + i)

def add_item():
    item = input ("Enter item to add to shopping list: ")
    shopping_list.append(item)
    print (item+ " has been added to the shopping list. Now there's more to carry human")

def remove_item():
    item = input ("Enter the item you wish to remove from the shopping list. ")
    shopping_list.remove(item)
    print()
    print(item+ " has been removed from the list. It's easier for you now!")


def check_item():
    item = input ("Which item would you like to check on the shopping list?")

    if item in shopping_list:
        print("Yes, "+item+" is on the list.")

    else:
        print("No, "+item+" is not on the list.")

def list_length():
        print("There are",len(shopping_list)," items on the shopping list for you to carry.")

def clear_list():
    shopping_list.clear()
    print()
    print("The shopping list is now empty.")



