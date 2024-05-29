# User credentials
credentials = {
    "username": "admin",
    "password": "password123"
}

def login():
    print("Welcome to the login system")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == credentials["username"] and password == credentials["password"]:
        print("Login successful!")
        print("Welcome to the data entry system")
    else:
        print("Invalid username or password. Please try again.")
        login()

# Main program
if __name__ == "__main__":
    login()
