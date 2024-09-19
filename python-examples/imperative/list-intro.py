# Create List(s)
liste = []


# Functions
def generate():
    # Generate the values
    num1 = input('input a random number:')

    # Convert the values
    num1 = int(num1)

    # Add them to the list
    liste.append(num1)

    return num1

def add(num1, num2):
    # Add the two variables
    num3 = num1 + num2
    num3 = str(num3)
    print("Your added total is", num3)

def subtract(num1, num2):
    num3 = num1 - num2
    num3 = str(num3)
    print("Your subtracted total is", num3)

def multiply(num1, num2):
    num3 = (num1 * num2)
    num3 = str(num3)
    print("Your multiplied total is", num3)

def divide(num1, num2):
    num3 = (num1 / num2)
    num3 = str(num3)
    print("Your divided total is", num3)

# Main loop
while True:  # Same as while 7 == 7:
    act = input("What to do now?")
    if act == "add": #call the function to add the numbers, and then call the function to generate them as inputs.
        add(generate(), generate())
        # This method saves space and looks overall cleaner, though there is a different method you can do this.
    elif act == "subtract":
        num5 = generate()
        num4 = generate()
        subtract(num5, num4)
        # Such as this method, which throws the output of the generate function into a couple of variables instead.
    elif act == "multiply":
        multiply(generate(), generate())
    elif act == "divide":
        divide(generate(), generate())
    elif act == "list":
        print(liste)
    elif act == "clear":
        liste = []
    else:
        print("Please try again.")