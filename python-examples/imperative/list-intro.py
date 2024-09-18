# Create List(s)
liste = []


# Functions
def add(num1, num2):
    # Add the two variables
    num3 = num1 + num2
    num3 = str(num3)
    print("Your added total is", num3)

def subtract(num1, num2):
    num3 = num2 - num1
    num3 = str(num3)
    print("Your subtracted total is", num3)


# Main loop
while True:  # Same as while 7 == 7:
    act = input("What to do now?")
    if act == "add":
            # Generate the Values
        num1 = input('input a random number:')
        num2 = input('input a second random number:')

        # Convert the Values
        num1 = int(num1)
        num2 = int(num2)

        # Add them to the list
        liste.append(num1)
        liste.append(num2)
        add(num1, num2)
    elif act == "subtract":
            # Generate the Values
        num1 = input('input a random number:')
        num2 = input('input a second random number:')

        # Convert the Values
        num1 = int(num1)
        num2 = int(num2)

        # Add them to the list
        liste.append(num1)
        liste.append(num2)
        subtract(num1, num2)
    elif act == "list":
        print(liste)
    elif act == "clear":
        liste = []
    else:
        print("Please try again.")