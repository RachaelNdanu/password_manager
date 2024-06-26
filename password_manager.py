#master_password = input("What is the master password? ")


def view():
    with open ('passwords.txt' , 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            
            user, passw = data.split ("|")
            print ("user:" ,user , " , password:" , passw)
    

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open ('passwords.txt' , 'a') as f:
        f.write(name + "|" + pwd + "\n" )


while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view) press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
