user = input("Input your username: ")
password = input("Enter your password: ")

admins = ['nate', 'gibz', 'june']

def login():
    while True:
        for i in range(len(admins)):
            if user == admins[i] and password == "admin":
                print(f"Login successful, Welcome {user}")
                return 
        print("Login failed")
        break

login()



