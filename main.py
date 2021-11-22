#Image Credits to Freepik.com downloaded ai file from there and made some change like text etc.
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import sys


verification1 = input("Type your verification Key:   ")
verification2 = input("Enter the 2nd key:   ")
key_1 = "9388376251279"
key_2 = "SUDO LET ME ACCESS THIS PROGRAM 150309"
key_3 = "6453829625"

if verification1 == key_1 :
    print("You can continue.")
    if verification2 == key_2:
        print("You have finished the test you can access this program")
    else:
        tryAgain = input("You have not completed the test! Try Again ")
        if tryAgain == key_3:
            print("You can access the program the program will not run")
        else:
            print("You cannot use this program")
            sys.exit()
else:
    print("You cannot access this program.")
    sys.exit()



def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "@", ]
# We can also use other methods like using .randint but it will be more readable but increase the lines of code 
# but here is used list comprehension to make the code shorter 
    password_letters = [choice(letters) for _ in range(randint(15, 20))]
    password_symbols = [choice(symbols) for _ in range(randint(4, 7))]
    password_numbers = [choice(numbers) for _ in range(randint(5, 7))]

    password_list = password_letters + password_symbols + password_numbers
    #basically shuffles all the characters
    shuffle(password_list)
#Join is a way to add list,tuple to add them and we can seperate them also but i have not seperated them 
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    #This  statement ensures if we have a blank space it will not register it 
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            #Helps us read the file and make changes 
            with open("data.pdf", "a") as data_file:
                data_file.write(f"The password for {website} and for  {email} is  {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

#UI /UX

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "youremail@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()