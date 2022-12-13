#Choose your desert
#Make match case function 
#Escape from program with leaving message.
def desert():  

    desert_choice = input("Please choose the Yellow , Blue or Green desert block: ").lower()
    
    match desert_choice:
        case "yellow":
            print()
            print("You have choosen a yummy treat human!\n")

        case "blue":
            print()
            print("Blue is the most delicious snack human.\n")

        case "green":
            print()
            print("You have choosen poorly human! Soylent Green is people.....Soylent green is made from people!\n")

        case _:
            print()
            print("You have entered incorrectly human,now you get nothing.\n")

    print("Until we meet again human!\n ")      
#Escape from program with leaving message.


desert() 