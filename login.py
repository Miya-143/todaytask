def login(username, password):
    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid Credentials")

# Test the function
user = input("Enter username: ")
pwd = input("Enter password: ")

login(user, pwd)