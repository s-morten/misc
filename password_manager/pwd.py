# import modules

from tkinter import *
import os

# Designing window for registration


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show="*")
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(
        register_screen,
        text="Register",
        width=10,
        height=1,
        bg="blue",
        command=register_user,
    ).pack()


def passwords():
    global passwords_screen
    passwords_screen = Toplevel(main_screen)
    passwords_screen.title("Passwords")
    passwords_screen.geometry("600x550")
    global userName
    userName = username_n
    # global username
    # global password
    global username_password
    global password_password
    global username_entry
    global password_entry
    # username = StringVar()
    # password = StringVar()
    username_password = StringVar()
    password_password = StringVar()

    Label(passwords_screen, text="Add new Password").pack()
    Label(passwords_screen, text="").pack()
    username_lable = Label(passwords_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(passwords_screen, textvariable=username_password)
    username_entry.pack()
    password_lable = Label(passwords_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(passwords_screen, textvariable=password_password)
    password_entry.pack()
    Label(passwords_screen, text="").pack()
    Button(
        passwords_screen, text="Add", width=10, height=1, command=add_password
    ).pack()

    passwords_in_file = get_passwords()
    for pwd in passwords_in_file:
        password_grid = Label(passwords_screen, text=f"{pwd}")
        password_grid.pack()


# Designing window for login


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show="*")
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button


def add_password():

    username_info = userName
    username_add = username_password.get()
    password_info = password_password.get()

    file = open(username_info, "a")
    file.write(username_add + "-:-" + password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(
        passwords_screen, text="Added Succesfull", fg="green", font=("calibri", 11)
    ).pack()
    passwords_screen.destroy()
    passwords()


def register_user():

    username_info = username.get()
    password_info = password.get()

    aktive_user = username_info
    file = open(username_info, "w")
    # file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(
        register_screen, text="Registration Success", fg="green", font=("calibri", 11)
    ).pack()


# Implementing event on login button


def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    print(f"{username1}+{type(username1)}")
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success


def login_sucess():
    global username
    username = username1
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(
        password_not_recog_screen, text="OK", command=delete_password_not_recognised
    ).pack()


# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(
        user_not_found_screen, text="OK", command=delete_user_not_found_screen
    ).pack()


# Deleting popups


def delete_login_success():
    global username_n
    username_n = username
    login_screen.destroy()
    login_success_screen.destroy()
    passwords()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window


def get_passwords():
    username = userName
    file = open(userName, "r")
    all = file.readlines()[1:]
    return all


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    # Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Quit", height="2", width="30", command=main_screen.destroy).pack()

    main_screen.mainloop()


main_account_screen()
