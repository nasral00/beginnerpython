name = input("Type your name: ")

print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around it swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died")
    else:
        print("Not a valid response.")
elif answer == "right":
    answer = input("You come across a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back to the main road and our found, game over.")
    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ")

        if answer == "yes":
            print("You talk to the stranger and are awarded with gold. You win!")
        elif answer == "no":
            print("You ignored the stranger and they are offended. You lose.")
        else:
            print("Not a valid response.")
    else:
        print("Not a valid response.")
else:
    print("Not a valid option. You lose.")


print("Thank you for trying!")