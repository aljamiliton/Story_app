def start_story():
    print("Welcome to the Adventure Story!")
    print("You find yourself at the entrance of a dark forest. What will you do?")
    print("1. Enter the forest.")
    print("2. Stay outside.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        print("\nYou decide to stay outside. The sun sets, and you return home safely.")
        print("THE END.")
    else:
        print("\nInvalid choice. Please try again.")
        start_story()

def forest_path():
    print("\nYou walk into the forest. It's dark and eerie. Suddenly, you hear a noise.")
    print("1. Investigate the noise.")
    print("2. Ignore the noise and keep walking.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        investigate_noise()
    elif choice == "2":
        print("\nYou ignore the noise and continue walking. Soon, you find a hidden treasure chest!")
        print("You open it and become rich!")
        print("THE END.")
    else:
        print("\nInvalid choice. Please try again.")
        forest_path()

def investigate_noise():
    print("\nYou move toward the noise cautiously. A wild animal appears!")
    print("1. Run away.")
    print("2. Try to calm the animal.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou run as fast as you can and escape safely.")
        print("THE END.")
    elif choice == "2":
        print("\nYou try to calm the animal, and it surprisingly becomes friendly.")
        print("The animal leads you to a hidden treasure!")
        print("THE END.")
    else:
        print("\nInvalid choice. Please try again.")
        investigate_noise()

# Start the story
start_story()
