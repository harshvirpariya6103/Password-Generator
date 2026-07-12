import secrets 
import string
import tkinter as tk
import customtkinter
from tkinter import messagebox
import pyperclip
from PIL import Image

# Core Logics
def generate_password(event=None):
    password_entry.configure(state="normal")
    password_entry.delete(0, tk.END)

    try: 
        length = int(length_entry.get())
        if length < 6 or length > 24:
            messagebox.showerror("Error", "Length should be between 6 to 24 characters.")
            password_entry.configure(state="readonly")
            return

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")
        password_entry.configure(state="readonly")
        return
    
    chars=""

    if upper_var.get():
        chars+=string.ascii_uppercase
    if lower_var.get():
        chars+=string.ascii_lowercase
    if num_var.get():
        chars+=string.digits
    if sym_var.get():
        chars+=string.punctuation
    
    if not chars:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    
    password=""
    char_count={}

    for _ in range(length):
        while True:
            char=secrets.choice(chars)

            if password and password[-1] == char:
                continue

            if char_count.get(char,0) >= 2:
                continue

            password+=char
            char_count[char]=char_count.get(char,0)+1
            break

    password_entry.insert(0,password)
    password_entry.configure(state="readonly")

    password_history.insert(0, password)
    if len(password_history) > 10:
        password_history.pop()

    for widget in history_scroll.winfo_children():
        widget.destroy()

    for p in password_history:
        row = customtkinter.CTkFrame(history_scroll, fg_color="transparent")
        row.pack(fill="x", pady=2)
        
        lbl = customtkinter.CTkLabel(row, text=p, font=("Arial", 14), text_color="#333333")
        lbl.pack(side="left", padx=5)
        
        btn = customtkinter.CTkButton(row, text="Copy", width=40, height=24, font=("Arial", 12), fg_color="#F0F0F0", text_color="#333333", hover_color="#E0E0E0")
        btn.configure(command=lambda pwd=p, b=btn: copy_specific_password(pwd, b))
        btn.pack(side="right", padx=5)
        
        div = customtkinter.CTkFrame(history_scroll, height=1, fg_color="#E0E0E0")
        div.pack(fill="x", padx=5, pady=(0, 2))

def copy_password():
    if password_entry.get():
        pyperclip.copy(password_entry.get())
        copy_button.configure(text="Copied!")
        root.after(1500, lambda: copy_button.configure(text="Copy to Clipboard"))

password_history = []

def copy_specific_password(pwd, btn):
    pyperclip.copy(pwd)
    btn.configure(text="Copied")
    root.after(1500, lambda: btn.configure(text="Copy"))

# GUI Design
root = customtkinter.CTk()
root.title("Password Generator")
root.geometry("1900x1080")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


main_container = customtkinter.CTkFrame(root, fg_color="transparent")
main_container.pack(fill="both", expand=True, padx=40, pady=40)

left_frame = customtkinter.CTkFrame(main_container, fg_color="transparent")
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 20))

hero_label_main = customtkinter.CTkLabel(left_frame, text="PASSWORD GENERATOR", font=("Impact", 84, "bold"), justify="left", text_color="white")
hero_label_main.pack()

middle_frame = customtkinter.CTkFrame(left_frame, fg_color="transparent")
middle_frame.pack(anchor="w", fill="x")

my_image = customtkinter.CTkImage(light_image=Image.open("image.png"), size=(300, 400))
image_label = customtkinter.CTkLabel(middle_frame, text="", image=my_image)
image_label.pack(side="left")

hero_label = customtkinter.CTkLabel(middle_frame, text="Generate Secure,\nand strong \npassword \nTry our random\npassword generator.", font=("Kacsttitle", 48, "bold", "italic"), justify="left", text_color="#FFCD37")
hero_label.pack(side="left", padx=(20, 0))

sub_label = customtkinter.CTkLabel(left_frame, text="Stop relying on weak, predictable passwords that leave your personal \ndata vulnerable. Build maximum-security, randomized keys tailored \nexactly to your needs.", font=("Kacsttitle", 30, "italic"), justify="left", text_color="#94A3B8")
sub_label.pack(anchor="w", pady=(20, 0))

right_card = customtkinter.CTkFrame(main_container, fg_color="#FFFFFF", corner_radius=30, width=450)
right_card.pack(side="right", fill="y", ipadx=20)
right_card.pack_propagate(False)

customize_label = customtkinter.CTkLabel(right_card, text="Customize your new password", font=("Kacsttitle", 20, "bold"), text_color="#000000")
customize_label.pack(anchor="w", padx=20, pady=50)

divider1 = customtkinter.CTkFrame(right_card, height=1, fg_color="#575757")
divider1.pack(fill="x", padx=20)

length_row = customtkinter.CTkFrame(right_card, fg_color="transparent")
length_row.pack(fill="x", padx=20, pady=0)

length_label = customtkinter.CTkLabel(length_row, text="Password Length (6-24):  ", font=("Kacsttitle", 18), text_color="#555555")
length_label.pack(side="left")

length_entry = customtkinter.CTkEntry(length_row, font=("Kacsttitle", 14), justify="center", width=60, fg_color="#FFFFFF", border_color="#CCCCCC", text_color="#333333")
length_entry.pack(side="left")
length_entry.insert(0, "12")

switch_frame = customtkinter.CTkFrame(right_card, fg_color="transparent")
switch_frame.pack(fill="x", padx=20, pady=15)

upper_var = customtkinter.BooleanVar(value=True)
lower_var = customtkinter.BooleanVar(value=True)
num_var = customtkinter.BooleanVar(value=True)
sym_var = customtkinter.BooleanVar(value=True)

upper_switch = customtkinter.CTkSwitch(switch_frame, text="Uppercase (A-Z)", variable=upper_var, font=("Kacsttitle", 14), text_color="#555555")
upper_switch.grid(row=0, column=0, pady=10, sticky="w")

lower_switch = customtkinter.CTkSwitch(switch_frame, text="Lowercase (a-z)", variable=lower_var, font=("Kacsttitle", 14), text_color="#555555")
lower_switch.grid(row=0, column=1, padx=(20, 0), pady=10, sticky="w")

num_switch = customtkinter.CTkSwitch(switch_frame, text="Numbers (0-9)", variable=num_var, font=("Kacsttitle", 14), text_color="#555555")
num_switch.grid(row=1, column=0, pady=10, sticky="w")

sym_switch = customtkinter.CTkSwitch(switch_frame, text="Symbols (!@#$)", variable=sym_var, font=("Kacsttitle", 14), text_color="#555555")
sym_switch.grid(row=1, column=1, padx=(20, 0), pady=10, sticky="w")

divider2 = customtkinter.CTkFrame(right_card, height=1, fg_color="#E0E0E0")
divider2.pack(fill="x", padx=20, pady=(5, 15))

output_label = customtkinter.CTkLabel(right_card, text="Generated password", font=("Kacsttitle", 20, "bold"), text_color="#333333")
output_label.pack(anchor="w", padx=20, pady=(5, 10))

password_entry = customtkinter.CTkEntry(right_card, font=("Kacsttitle", 24), justify="center", state="readonly", height=60, fg_color="#FFFFFF", border_color="#E0E0E0", border_width=1, text_color="#111111")
password_entry.pack(fill="x", padx=20, pady=(0, 20))

button_frame = customtkinter.CTkFrame(right_card, fg_color="transparent")
button_frame.pack(fill="x", padx=20, pady=(0, 20))

copy_button = customtkinter.CTkButton(button_frame, text="Copy password", font=("Kacsttitle", 18, "bold"), text_color="#FFFFFF", fg_color="#0066FF", corner_radius=25, hover_color="#0052CC", height=40, command=copy_password)
copy_button.pack(side="left", fill="x")

btn_generate = customtkinter.CTkButton(button_frame, text="Generat password", font=("kacsttitle", 18, "bold"), text_color="#0066FF", fg_color="#FFFFFF", border_color="#0066FF", corner_radius=25, border_width=1,  hover_color="#F0F8FF",height=40, command=generate_password)
btn_generate.pack(side="right", fill="x")

history_label = customtkinter.CTkLabel(right_card, text="More passwords", font=("Kacsttitle", 16, "bold"), text_color="#30336b")
history_label.pack(anchor="w", padx=20, pady=(0, 5))

history_scroll = customtkinter.CTkScrollableFrame(right_card, fg_color="transparent", height=120)
history_scroll.pack(fill="both", expand=True, padx=10, pady=(0, 15))

root.bind('<Return>', generate_password)
root.mainloop()