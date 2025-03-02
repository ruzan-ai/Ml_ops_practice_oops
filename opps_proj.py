class chatbook:
    def __init__(self):
        self.__name = "Deafult User"
        self.username = ""
        self.password = ""
        self.loggedin = False
        #self.menu()

    def menu(self):
        user_input  = input("""Welcome to chatbook how would you like to proceed
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend1
                            5. Press 5 any key to exit           """)    
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3": 
            self.my_post
        elif user_input == "4":
            self.sendmsg()
        else:
            exit ()
    def signup(self):
        email = input("Enter your email")
        pwd = input("Enter your password")
        self.username = email
        self.password = pwd
        print("Signup successful")
        print("\n")
        self.menu()

    def signin(self):
        if self.loggedin == True and self.password == "":
            print("Please sign up first")
        else:
            uname = input("Enter your username / email")
            pwd = input("Enter your password")
            if self.username == uname and self.password == pwd:
                print("You have successfully logged in sucessfully")
                self.loggedin = True
            else:
                print("Invalid username or password")
            print("\n")
            self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your post here -> ")
            print (f"Your post is -> {txt}")
        else:
            print("Please sign in first")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            frnd = input("Enter the name of the friend you want to message -> ")
            print (f"Your message to {frnd} and your message is -> {txt}")
        else:
            print("Please sign in first")
        print("\n")
        self.menu()


#obj = chatbook()
