'''
Hi, this game was made by Vitor Crosera based on the movie
"Black Mirror: Bandersnatch" by Charlie Brooker and Annabel Jones
'''

print("Hello,\n Welcome to my first game!")
name = input("Please enter your name: ")
age = int(input("How old are you? "))

if age >= 18:
    print("Are you ready to start the game " + name + "? ")
    wants_to_play = input("yes or no? ").lower()
    if wants_to_play == "yes":
        print("Great, let's play!")

        right_or_left = input("You just entered a maze, do you want to go right, left, or center (left/center/right)? ").lower()
        if right_or_left == "left":
            print("Great, you found a lake with a boat")
            boat = input("Do you get in the boat or go around (boat/around)? ").lower()
            if boat == "boat":
                print("Ops...\nthere were alligators in the lake and your boat had a hole...\n YOU DIED... ")
            else:
                print("Great choice, you win!!!")
                print("YOU WINNNNNN")
        elif right_or_left == "center":
            kill = input("You just found a snake, do you try to kill it or go around (kill/around)? ").lower()
            if kill == "kill":
                print("The snake was much faster than you, sorry\n YOU DIED!!!")
            else:
                print("Great choice, you win!!!")
                print("YOU WINNNNNN")
        else:
            trap = input("You found yourself trapped, do you try to climb or go back (climb/go back)? ").lower()
            if trap == "climb":
                print("Sorry the floor of the other side of the wall was full of spikes\nYOU DIED!!!")
            else:
                right_or_left = input(
                    "You just entered a maze, do you want to go right, left, or center (left/center/right)? ").lower()
                if right_or_left == "left":
                    print("Great, you found a lake with a boat")
                    boat = input("Do you get in the boat or go around (boat/around)? ").lower()
                    if boat == "boat":
                        print("Ops...\nthere were alligators in the lake and your boat had a hole...\n YOU DIED... ")
                    else:
                        print("Great choice, you win!!!")
                        print("YOU WINNNNNN")
                elif right_or_left == "center":
                    kill = input("You just found a snake, do you try to kill it, or go around (kill/around)? ").lower()
                    if kill == "kill":
                        print("The snake was much faster than you, sorry\n YOU DIED!!!")
                    else:
                        print("Great choice, you win!!!")
                        print("YOU WINNNNNN")


    else:
        print("No problem, come back when you are ready...")
elif age >= 14:
    print("You are allowed to play only with supervision!!")
    print("Are you ready to start the game " + name + "? ")
    wants_to_play = input("yes or no? ").lower()
    if wants_to_play == "yes":
        print("Great, let's play!")

        right_or_left = input(
            "You just entered a maze, do you want to go right, left, or center (left/center/right)? ").lower()
        if right_or_left == "left":
            print("Great, you found a lake with a boat")
            boat = input("Do you get in the boat or go around (boat/around)? ").lower()
            if boat == "boat":
                print("Ops...\nthere were alligators in the lake and your boat had a hole...\n YOU DIED... ")
            else:
                print("Great choice, you win!!!")
                print("YOU WINNNNNN")
        elif right_or_left == "center":
            kill = input("You just found a snake, do you try to kill it or go around (kill/around)? ").lower()
            if kill == "kill":
                print("The snake was much faster than you, sorry\n YOU DIED!!!")
            else:
                print("Great choice, you win!!!")
                print("YOU WINNNNNN")
        else:
            trap = input("You found yourself trapped, do you try to climb or go back (climb/go back)? ").lower()
            if trap == "climb":
                print("Sorry the floor of the other side of the wall was full of spikes\nYOU DIED!!!")
            else:
                right_or_left = input(
                    "You just entered a maze, do you want to go right, left, or center (left/center/right)? ").lower()
                if right_or_left == "left":
                    print("Great, you found a lake with a boat")
                    boat = input("Do you get in the boat or go around (boat/around)? ").lower()
                    if boat == "boat":
                        print("Ops...\nthere were alligators in the lake and your boat had a hole...\n YOU DIED... ")
                    else:
                        print("Great choice, you win!!!")
                        print("YOU WINNNNNN")
                elif right_or_left == "center":
                    kill = input("You just found a snake, do you try to kill it, or go around (kill/around)? ").lower()
                    if kill == "kill":
                        print("The snake was much faster than you, sorry\n YOU DIED!!!")
                    else:
                        print("Great choice, you win!!!")
                        print("YOU WINNNNNN")
    else:
        print("No problem, come back when you are ready...")
else:
    print("Sorry you are too young to play...")