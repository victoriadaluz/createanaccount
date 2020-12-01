granted = False
def grant():
    global granted
    granted = True

def login (name, password):
    success = False
    file = open("createlogin.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            success=True
            break
    file.close()
    if(success):
        print("Login Succesful!")
        grant()
    else:
        print("Wrong username or password")
        
def register(name,password):
    file = open("createlogin.txt", "a")
    file.write("\n"+name+","+password)
    file.close()
    grant()

def access(option):
    global name
    if(option=="login"):
        name = input("Enter your username to login: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)

def begin():
    global option
    print("Hi, welcomo to Chili's!")
    option = input("Login or register (login,reg): ")
    if(option!="login" and option!="reg"):
        begin()
begin()
access(option)
if(granted):
    print("Hi! Welcome to Chili's!")
    print("### User Details ###")
    print("Username: ", name)
