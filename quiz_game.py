count = 0

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    count += 1;
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print("Correct!")
    count += 1;
else:
    print("Incorrect!")


print("Congrats you got " + str(count) + " out of 4 answers correct!")
print("That is " + str((count/4) * 100)  + "%!")

