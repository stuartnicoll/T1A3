#Choose your desert
#Make match case function 
#Escape from program with leaving message.
def desert():  

    desert_choice = input("Please choose the Yellow , Blue or Green desert block: ")
    
    match desert_choice:
        case "Yellow":
            print()
            print("You have choosen a yummy treat human!")

        case "Blue":
            print()
            print("Blue is the most delicious snack human.")

        case "Green":
            print()
            print("You have choosen poorly human! Soylent Green is people.....Soylent green is people!")

        case _:
            print()
            print("You have entered incorrectly human,now you get nothing.")

desert()
#Escape from program with leaving message.
print()
print("We are done here human. Until next time and good luck.")