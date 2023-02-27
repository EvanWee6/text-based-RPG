import random

print( '''
                             -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
''')
print("You are in a castle\n")
print("You're goal is to gather weapons, interprets clues, then fight the final boss at the end!\n")
print("To get you started, there is a kitchen at (3,2)\n")
 
x = 1
y = 1
health = 50
inventory = []
bossHealth = 200

while True:
    
    while len(inventory) <= 1:
        print(f'You are located at ({x},{y})\n')
        move_x = int(input("How much would you like to move on the x axis: "))
        move_y = int(input("How much would you like to move on the y axis: "))
        x += move_x
        y += move_y

        #kitchen
        if x == 3 and y == 2:
        
            while True: 
                print("\nYou've reached the kitchen!")
                kitchenDecision = int(input("\nWould you like to eat something from the kitchen? [1]Yes [2]No "))
                print(f'You currently have {health} health\n')

                if kitchenDecision == 1:
                    if health < 100:
                        health += 10
                        print(f"You've healed 10 and are now at {health} health")
                    elif health >= 100:

                        print(
                        """
                        ------------------------------
                        |You've reach maximum health!|
                        ------------------------------
                        """
                        )

                        break

                else:
                    print(f"Ok, your health will remain at {health}") 
                    break
            
            print("\nThere is a chef hiding in a corner at (3,8)")
            print("\nHe might have a clue!")
        
        #chef
        if x == 3 and y == 8:
            while True:
                print('\nYou found a chef!\n')
                
                print("But in order to retrieve the information from me, you must solve this question!")

                print("\nWhat is the name of the chef who helps runs the kitchen when the main chef is preoccupied with other tasks (second in command)")
                print(
                """
                1.Assistant chef
                2.Bouillabaisse en chefie 
                3.Sous chef
                """
                )
                sousChefAnswer = int(input("Answer(#): "))

                if sousChefAnswer == 3:
                    print("\nHe says: there might be weapon at (5,5)\n")
                    break
       
        #chest
        if x == 5 and y == 5:
            while True:  
                print("\nYou found a chest!\n")  
                chestDecision = int(input("Would you like to open the chest? [1]Yes [2]No "))
                if chestDecision == 1:
                    if "dagger" in inventory:

                        print(
                        """\n
                        -----------------------------
                        |You already have that item!|
                        -----------------------------
                        """
                        )
                        

                        break
                    else:
                        inventory.append('dagger')

                    print("\nNEW ITEM!")
                    print("""
                    --------
                    |Dagger| 
                    --------
                    \n""")

                    print("There's a note inside the chest!\n")
                    mapDecision = input("Would you like to read the note! [1]Yes [2]No ")
                    if int(mapDecision) == 1:
                        print("\nThe note is a map!")
                        print("The map says you have to head to the roof to find something!")
                        print("The roof is located at (10,15)!\n")
                    else: 
                        print("Ok, have fun with the rest of your journey!")

                    break
                elif chestDecision == 2:
                    print('\nOk, continue on your journey!\n')
                    break
                
        #roof
        if x == 10 and y == 15:
            while True: 
                print("\nYou've reached the top of the castle!\n")
                roofDecision = int(input("There is a bow and arrow - would you like to pick it up? [1]Yes [2]No "))

                if roofDecision == 1:
                    if 'bow' in inventory:
                        print(
                        """\n
                        -----------------------------
                        |You already have that item!|
                        -----------------------------
                        """
                        )
                        break
                    else:
                        inventory.append('bow')

                        print("\nNEW ITEM!")
                        print("""
                        ---------------
                        |Bow and Arrow| 
                        ---------------
                        \n""")
                        break
                elif roofDecision == 2:
                    print("\nOk, continue on your journey!")
                    break
        
            

                print(
                """\n
                -------------------------
                |Your inventory is full!|
                -------------------------
                \n"""
                )

                print("You are now ready to fight the zombie king!")
                print("He is located at\n")
                print(
                """
                (7,16) 
                """
                )
                break
    print("\n" * 5)
    print("Inventory full!\n")
    print(f'Stats:\n')
    print(f'Health: {health}\n')
    print('Inventory:\n')
    for i in range(len(inventory)):
        print(f'- {inventory[i]}')

    while bossHealth > 0:

        print("The final boss is final boss is located at (20, 5)\n")

        print(f'You are located at ({x},{y})\n')
        move_x = int(input("How much would you like to move on the x axis: "))
        move_y = int(input("How much would you like to move on the y axis: "))
        x += move_x
        y += move_y 

        if x == 20 and y == 5:
            print("\nYou've arrived to the lair of the vampire that has waited for you!")
            print("He attacks you first and takes away 10 health when he punches you")
            health -= 10

            while bossHealth > 0:
                if health > 0:
                    bossAttackRandom = random.randint(0,1)
                    if bossAttackRandom == 0:
                        print('\nThe vampire bites you and deals 10 damage!')
                        health -= 10
                        print(f'You are now at {health} health\n')
                        
                        weaponDecision = int(input("Which weapon do you choose to use on him? [1]Dagger [2]Bow and arrow [3]Fist "))
                        if weaponDecision == 1: 

                            print("You choose dagger!\n")
                            print("\nYou deal 20 damage!\n")
                            bossHealth -= 20
                            print(f'The vampire is at {bossHealth} health!')

                        elif weaponDecision == 2:

                            print("You choose Bow and Arrow!\n")
                            print("\nYou did 10 damage\n")
                            bossHealth -= 10
                            print(f'The vampire is at {bossHealth} health!')

                        elif weaponDecision == 3: 
                    
                            print("You choose your fist!\n")
                            print("\nYou deal 5 damage\n")
                            bossHealth -= 5
                            print(f'The vampire is at {bossHealth} health!')

                        else: 
                            print("Invalid choice")
                    
                    elif bossAttackRandom == 1:
                        weaponDecision = int(input("Which weapon do you choose to use on him? [1]Dagger [2]Bow and arrow [3]Fist "))
                        if weaponDecision == 1: 

                            print("You choose dagger!\n")
                            print("\nYou deal 20 damage!\n")
                            bossHealth -= 20
                            print(f'The vampire is at {bossHealth} health!')

                        elif weaponDecision == 2:

                            print("You choose Bow and Arrow!\n")
                            print("\nYou did 10 damage\n")
                            bossHealth -= 10
                            print(f'The vampire is at {bossHealth} health!')

                        elif weaponDecision == 3: 
                    
                            print("You choose your fist!\n")
                            print("\nYou deal 5 damage\n")
                            bossHealth -= 5
                            print(f'The vampire is at {bossHealth} health!')

                        else: 
                            print("Invalid choice")
                else:
                    print("\nYou died!")
                    print("GAME OVER")

                    print(
                    """
                    --------------
                    |  You died  |
                    | GAME OVER! |
                    --------------
                    """
                    )
                    break
                
    print("\nCongrats you win!\n")  

    break
    