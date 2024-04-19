print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print("\nYou are walking in the forest and coming to a crossroad.")
choice1 = input("Take the road to the [left] or to the [right]?").lower()
if choice1 == "left":
    print("\nYou are walking along the road and you see a lake.")
    choice2 = input("Do you want to [swim] or [wait] for a boat?").lower
    if choice2 == "wait":
        print(
            "\nYou are waiting for a boat and a boat arrives. You get on the boat and you are sailing to the other side of the lake.")
        print("You are walking along the road and you see a house with three doors.")
        choice3 = input("Which door do you want to open? The [red], [yellow] or [blue] door?").lower()
        if choice3 == "red":
            print("Game Over!")
        elif choice3 == "yellow":
            print("Game Over!")
        else:
            print("You Win!")
    else:
        print(
            "\nYou are swimming in the lake and you see a crocodile. You try to swim away but the crocodile is faster than you. You are dead.")
        print("Game over.")
else:
    print("\nYou are walking along the road and a big spider catch you.")
    print("Game Over!")
