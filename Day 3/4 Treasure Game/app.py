print("Welcome to Treasure Island.\nYour mission is to find The treasure.")
left_right = input(
    "You're at the cross road, where do you want to go ? 'left' or 'right' : ").lower()
if left_right == "left":
    swim_wait = input(
        "You've come to the lake. There is an island in the middle of the lake. Type 'Wait' for boat or 'swim' to swim across : ").lower()
    if swim_wait == "wait":
        which_door = input(
            "Congrats ! You've found the key or Island. Which door you want to select ? 'Red', 'Blue', 'Yellow' : ").lower()
        if which_door == "yellow":
            print("Congrats !! You found the treaseure. You win !!")
        elif which_door == "red":
            print("You got attacked by wolves !!. Game Over !!")
        elif which_door == "blue":
            print("It's a room full of fire. Game Over !!")
        else:
            print("You've turned the Volcano on. Game Over !!")
    else:
        print("You fell into a hole. Game Over !!")
else:
    print("You fell into a hole. Game Over !!")
