
# Import modules
import time

# All accounts
users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
        "mail": []
    }
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Register
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["mail"] = []
    time.sleep(1)
    print("Account has been created")

# Send mail
def sendmail(username):
    while True:
        recipient = input("Recipient > ")
        if not len(recipient) > 0:
            print("Recipient can't be blank")
            continue
        elif recipient not in users:
            print("There is no account with that username")
            continue
        else:
            break
    while True:
        subject = input("Subject > ")
        if not len(subject) > 0:
            print("Subject can't be blank")
            continue
        else:
            break
    while True:
        context = input("Context > ")
        if not len(context) > 0:
            print("Context can't be blank")
        else:
            break
    print("Sending mail...")
    users[recipient]["mail"].append(["Sender: " + username, "Subject: " + subject, "Context: " + context])
    time.sleep(1)
    print("Mail has been sent to " + recipient)

# User session
def session(username):
    print("Welcome to your account " + username)
    print("Options: view mail | send mail | logout")
    if users[username]["group"] == "admin":
        print("")
    while True:
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break
        elif option == "view mail":
            print("Current mail:")
            for mail in users[username]["mail"]:
                print(mail)
        elif option == "send mail":
            sendmail(username)
        elif users[username]["group"] == "admin":
            if option == "user mail":
                print("Whos mail would you like to see?")
                userinfo = input("> ")
                if userinfo in users:
                    for mail in users[userinfo]["mail"]:
                        print(mail)
                else:
                    print("There is no account with that username")
            elif option == "delete mail":
                print("Whos mail would you like to delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Deleting " + userinfo + "'s mail...")
                    users[userinfo]["mail"] = []
                    time.sleep(1)
                    print(userinfo + "'s mail has been deleted")
                else:
                    print("There is no account with that username")
            elif option == "delete account":
                print("Whos account would you like to delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Are you sure you want to delete " + userinfo + "'s account?")
                    print("Options: yes | no")
                    while True:
                        confirm = input("> ")
                        if confirm == "yes":
                            print("Deleting " + userinfo + "'s account...")
                            del users[userinfo]
                            time.sleep(1)
                            print(userinfo + "'s account has been deleted")
                            break
                        elif confirm == "no":
                            print("Canceling account deletion...")
                            time.sleep(1)
                            print("Account deletion canceled")
                            break
                        else:
                            print(confirm + " is not an option")
                else:
                    print("There is no account with that username")
        else:
            print(option + " is not an option")

# On start
print("Welcome to the system. Please register or login.")
print("Options: register | login | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")

# from tkinter import *
# import os
 
# # Designing window for registration
 
# def register():
#     global register_screen
#     register_screen = Toplevel(main_screen)
#     register_screen.title("Register")
#     register_screen.geometry("300x250")
 
#     global username
#     global password
#     global username_entry
#     global password_entry
#     username = StringVar()
#     password = StringVar()
 
#     Label(register_screen, text="Please enter details below", bg="blue").pack()
#     Label(register_screen, text="").pack()
#     username_lable = Label(register_screen, text="Username * ")
#     username_lable.pack()
#     username_entry = Entry(register_screen, textvariable=username)
#     username_entry.pack()
#     password_lable = Label(register_screen, text="Password * ")
#     password_lable.pack()
#     password_entry = Entry(register_screen, textvariable=password, show='*')
#     password_entry.pack()
#     Label(register_screen, text="").pack()
#     Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# # Designing window for login 
 
# def login():
#     global login_screen
#     login_screen = Toplevel(main_screen)
#     login_screen.title("Login")
#     login_screen.geometry("300x250")
#     Label(login_screen, text="Please enter details below to login").pack()
#     Label(login_screen, text="").pack()
 
#     global username_verify
#     global password_verify
 
#     username_verify = StringVar()
#     password_verify = StringVar()
 
#     global username_login_entry
#     global password_login_entry
 
#     Label(login_screen, text="Username * ").pack()
#     username_login_entry = Entry(login_screen, textvariable=username_verify)
#     username_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Label(login_screen, text="Password * ").pack()
#     password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
#     password_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# # Implementing event on register button
 
# def register_user():
 
#     username_info = username.get()
#     password_info = password.get()
 
#     file = open(username_info, "w")
#     file.write(username_info + "\n")
#     file.write(password_info)
#     file.close()
 
#     username_entry.delete(0, END)
#     password_entry.delete(0, END)
 
#     Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# # Implementing event on login button 
 
# def login_verify():
#     username1 = username_verify.get()
#     password1 = password_verify.get()
#     username_login_entry.delete(0, END)
#     password_login_entry.delete(0, END)
 
#     list_of_files = os.listdir()
#     if username1 in list_of_files:
#         file1 = open(username1, "r")
#         verify = file1.read().splitlines()
#         if password1 in verify:
#             login_sucess()
 
#         else:
#             password_not_recognised()
 
#     else:
#         user_not_found()
 
# # Designing popup for login success
 
# def login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(login_screen)
#     login_success_screen.title("Success")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Success").pack()
#     Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# # Designing popup for login invalid password
 
# def password_not_recognised():
#     global password_not_recog_screen
#     password_not_recog_screen = Toplevel(login_screen)
#     password_not_recog_screen.title("Success")
#     password_not_recog_screen.geometry("150x100")
#     Label(password_not_recog_screen, text="Invalid Password ").pack()
#     Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# # Designing popup for user not found
 
# def user_not_found():
#     global user_not_found_screen
#     user_not_found_screen = Toplevel(login_screen)
#     user_not_found_screen.title("Success")
#     user_not_found_screen.geometry("150x100")
#     Label(user_not_found_screen, text="User Not Found").pack()
#     Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# # Deleting popups
 
# def delete_login_success():
#     login_success_screen.destroy()
 
 
# def delete_password_not_recognised():
#     password_not_recog_screen.destroy()
 
 
# def delete_user_not_found_screen():
#     user_not_found_screen.destroy()
 
 
# # Designing Main(first) window
 
# def main_account_screen():
#     global main_screen
#     main_screen = Tk()
#     main_screen.geometry("300x250")
#     main_screen.title("Account Login")
#     Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(text="").pack()
#     Button(text="Login", height="2", width="30", command = login).pack()
#     Label(text="").pack()
#     Button(text="Register", height="2", width="30", command=register).pack()
 
#     main_screen.mainloop()
 
 
# main_account_screen()