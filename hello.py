def get_name():
    """
    Function to get the user's name as input
    """
    name = input("Please enter your name: ")
    return name

def greet_user(name):
    """
    Function to greet the user
    """
    print(f"\nHello, {name}! Welcome to the world of Python and GitHub.\n")

def hello_world():
    """
    Main function to run the hello world program
    """
    name = get_name()
    greet_user(name)

if __name__ == "__main__":
    hello_world()