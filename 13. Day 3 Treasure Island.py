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
direction = input("Left or Right?\n").lower()
if direction == "left":
    action_1 = input("You're now in front of a river that dries periodically, 'Swim' or 'Wait'?\n").lower()
    if action_1 == "wait":
        action_2 = input("You've safely crossed the river. Now you're faced with doors of different colors, pick a color of which door you wanna open.\n").lower()
        if (action_2 == "blue") or (action_2 == "red"):
            print("Game over, cos game over")
        elif action_2 == "yellow":
            print("What sorcery?? You win!")
        else:
            action_3 = input("Game over, try again. What color now?\n").lower()
            if action_3 == action_2:
                print("Oh my daeyz, what a fcking idiot. I personally sniped you. Game Over.")
            elif action_3 == "yellow":
                print("You win!")
            else:
                print("Game over, just restart *face palms*")
        
        
    elif action_1 == "swim":
        print("Game over, the water was boiling hot")
    else:
        print("Game over, you're dragged into  the hot boiling river by a mutant killer orca. So much for time wasting")
    
    
    
elif direction == "right":
    print("Game Over, you're devoured by a lion")
    
    
else:
    print("Game Over, you're carried off by a moloch for time wasting, get your head in the game")
