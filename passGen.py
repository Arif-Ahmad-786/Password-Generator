from tkinter import *
import random
import string

root = Tk()
root.geometry("400x300")
root.title("Password Generator")


button_color = "#4CAF50"
button_text_color = "#FFFFFF"
entry_bg = "#E0E0E0"
font_large = ("Arial", 14, "bold")
font_medium = ("Arial", 12)
font_small = ("Arial", 10)

myframe = LabelFrame(root, text="Password Generator", font=font_large, padx=10, pady=10)
myframe.pack(fill="both", expand=True)

mylabel = Label(myframe, text="Enter Length:", font=font_medium)
mylabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
ent = Entry(myframe, width=10, font=font_medium, bg=entry_bg, borderwidth=5)
ent.grid(row=0, column=1, padx=10, pady=10)


lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
number = list(string.digits)
special = list(string.punctuation)

password = []


def eas():
    x = int(ent.get())
    password.clear()  
    if x < 6:
        mylabel5.config(text="Min: 6 characters", fg="red")
    elif x > 12:
        mylabel5.config(text="Max: 12 characters", fg="red")
    else:
        password.append(random.choice(upper))
        password.append(random.choice(number))
        password.append(random.choice(special))
        for i in range(3, x):
            password.append(random.choice(lower))
        random.shuffle(password)
        generated_password = ''.join(password)
        mylabel5.config(text=generated_password, fg="green")

def med():
    x = int(ent.get())
    password.clear()
    if x < 6:
        mylabel5.config(text="Min: 6 characters", fg="red")
    elif x > 12:
        mylabel5.config(text="Max: 12 characters", fg="red")
    else:
        password.append(random.choice(special))
        for i in range(2):
            password.append(random.choice(upper))
            password.append(random.choice(number))
        for i in range(x-5):
            password.append(random.choice(lower))
        random.shuffle(password)
        generated_password = ''.join(password)
        mylabel5.config(text=generated_password, fg="green")

def hard():
    x = int(ent.get())
    password.clear()
    if x < 6:
        mylabel5.config(text="Min: 6 characters", fg="red")
    elif x > 12:
        mylabel5.config(text="Max: 12 characters", fg="red")
    else:
        for i in range(x // 4):
            password.append(random.choice(upper))
            password.append(random.choice(number))
            password.append(random.choice(lower))
            password.append(random.choice(special))
        for i in range(x % 4):
            password.append(random.choice(lower))
        random.shuffle(password)
        generated_password = ''.join(password)
        mylabel5.config(text=generated_password, fg="green")


mybutton = Button(myframe, text="Easy", command=eas, font=font_medium, bg=button_color, fg=button_text_color)
mybutton.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
mybutton2 = Button(myframe, text="Medium", command=med, font=font_medium, bg=button_color, fg=button_text_color)
mybutton2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
mybutton3 = Button(myframe, text="Hard", command=hard, font=font_medium, bg=button_color, fg=button_text_color)
mybutton3.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")


mylabel4 = Label(myframe, text="Password:", font=font_medium)
mylabel4.grid(row=2, column=0, padx=10, pady=10, sticky="e")
mylabel5 = Label(myframe, text="Generated Password", bg="white", font=font_medium, relief="sunken", width=20)
mylabel5.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")


for i in range(3):  
    myframe.grid_rowconfigure(i, weight=1)
for j in range(3):  
    myframe.grid_columnconfigure(j, weight=1)

root.mainloop()
