print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!\n")
print("Your mission is to find the legendary Golden Treasure hidden deep within the island.\n"
      "But beware, danger lurks at every corner...\n\n")

# First choice: Left or Right
direction = input("You find yourself at a crossroads in a dense jungle.\n"
                  "Will you go 'Left' into the shadows of towering trees,\n"
                  "or 'Right' toward the sound of crashing waves? Choose wisely: ").lower()
if direction == "left" or direction == "l":
    print("\nYou venture down the left path, stepping over twisted roots and ducking under low-hanging vines. "
          "The air grows thicker, but you feel closer to your goal...")

    # Second choice: Swim or Wait
    action = input("\nAhead, you see a vast lake shimmering under the moonlight.\n"
                   "There's a small island in the center, but no boat in sight.\n"
                   "Will you 'Swim' across or 'Wait' on the shore for something to happen? ").lower()
    if action == "wait":
        print("\nYou decide to wait patiently. After a few tense moments, the water begins to ripple,\n"
              "and a mysterious old boat emerges from the mist, seemingly there just for you.\n"
              "You row across safely, feeling a thrill of adventure!\n")

        # Third choice: Door Color
        door = input("\nOnce across, you approach an ancient stone temple with three towering doors,\n"
                     "each glowing a different color: 'Red', 'Blue', and 'Yellow'. Which door do you choose? ").lower()
        if door == "yellow":
            print("\nYou push open the yellow door, and golden light floods the room!\n"
                  "The legendary Golden Treasure sits before you, glittering beyond your wildest dreams.\n"
                  "You've found it! Congratulations, you win! :)")
        elif door == "red":
            print("\nThe red door creaks open, and a burst of flame shoots out, engulfing you in a fiery blaze.\n"
                  "You’ve been burned by fire.\nGame Over. :(")
        else:
            print("\nYou open the blue door, stepping into darkness. Suddenly, you hear growls all around...\n"
                  "Wild beasts leap at you from the shadows!\nGame Over. :(")
    else:
        print("\nYou dive into the lake and begin swimming toward the island.\n"
              "Suddenly, a sharp pain surges through your leg as something bites you from below.\n"
              "A trout as large as a shark drags you under.\nGame Over. :(")
else:
    print("\nYou turn to the right and start walking,\n"
          "but the ground gives way beneath you!\n"
          "You tumble down into a hidden pit.\nGame Over :(.")










