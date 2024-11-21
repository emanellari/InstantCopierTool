import tkinter as tk
from tkinter import ttk

import keyboard

# from EasyOcr import text_from_google_lens
from SelectImageFromScreen import ScreenshotApp

# Krijimi i dritares
window = tk.Tk()
window.title("Instant Copier Tool")
window.geometry("500x600")  # Madhësia e dritares

# Caktimi i ngjyrës së backgroundit
window.configure(bg='#110c6e')

# Vendosja e ikonës PNG për dritaren
# icon_image = Image.open('ico-removebg.png')
# window.iconphoto(True, ImageTk.PhotoImage(icon_image))

# Krijimi i etiketës për titullin
title_label = tk.Label(window, text="Instant Copier Settings", font=("Arial", 24, "bold"), fg="white", bg='#110c6e')
title_label.pack(pady=20)  # pady është një hapësirë midis etiketës dhe pjesës tjetër të dritares

# Etiketa për zgjedhjen e shkurtërave të tastierës
shortcut_label = tk.Label(window, text="Choose Keyboard Shortcut :", font=("Arial", 18), fg="white", bg='#110c6e')
shortcut_label.pack(pady=10)

# Lista e shkurtërave të tastierës
shortcuts = ['F1','F2','F3','F4','F5','F6','F7',"F8",'F9','F10','F11','F12', "Ctrl+C", "Ctrl+X", "Ctrl+V", "Ctrl+Z", "Ctrl+Y"]
shortcut_var = tk.StringVar()
shortcut_dropdown = ttk.Combobox(window, textvariable=shortcut_var, values=shortcuts,  state='readonly',font=("Arial", 18))  # Madhësia e dropdown
shortcut_dropdown.set("F8")  # Defaulti është F8
shortcut_dropdown.pack(pady=10)

# Etiketa për zgjedhjen e opsioneve
option_label = tk.Label(window, text="Choose Option:", font=("Arial", 18), fg="white", bg='#110c6e')
option_label.pack(pady=10)

# Lista e opsioneve
options = ["Better Speed(Ofline)", "Better Accuracy(Requires Internet Conection)"]
option_var = tk.StringVar()
option_dropdown = ttk.Combobox(window, state= 'readonly',textvariable=option_var, values=options, font=("Arial", 16))  # Madhësia e dropdown
option_dropdown.set("Better Speed")  # Defaulti është "Better Speed"
option_dropdown.pack(pady=10)

# Etiketa për zgjedhjen e stilit të tekstit
text_case_label = tk.Label(window, text="Choose Text Case:", font=("Arial", 18), fg="white", bg='#110c6e')
text_case_label.pack(pady=10)

# Lista e stileve të tekstit
text_cases = ["Original(The 1-st example.)","Sentence case(The 1-st example.)", "lower case(the 1-st example.)", "UPPER CASE(THE 1-ST EXAMPLE.)", "Capitalized Case(The 1-st Example.)","Title Case(The 1-St Example.)", "aLtErNaTiNg cAsE(ThE 1-St ExAmPlE.)"]
text_case_var = tk.StringVar()
text_case_dropdown = ttk.Combobox(window,state= 'readonly', textvariable=text_case_var, values=text_cases, font=("Arial", 16))  # Madhësia e dropdown
text_case_dropdown.set("Original")  # Defaulti është "Sentence case"
text_case_dropdown.pack(pady=10)

# Checkbox për të treguar textbox para se të kopjohet
show_textbox_var = tk.BooleanVar()
show_textbox_checkbox = tk.Checkbutton(window, text="Show Textbox Before Copy", variable=show_textbox_var,
                                       font=("Arial", 18), fg="white", bg='#110c6e', selectcolor='black')
show_textbox_checkbox.pack(pady=10)
def check_for_key_press_(root):
    if not root.winfo_exists(): # Check if the window still exists
        return

    if keyboard.is_pressed(key[0]):
        root.lower()
        ScreenshotApp(root, key[0], option[0], txtbox[0], TEXT_CASE[0])

    root.after(100, check_for_key_press_, root)
def Submit():
    key[0]=shortcut_dropdown.get()
    option[0]=option_dropdown.get()
    txtbox[0]=show_textbox_var.get()
    TEXT_CASE[0]=text_case_dropdown.get()
    window.lower()


submit_button = tk.Button(window, text="Submit", command=Submit, font=("Arial", 20))
submit_button.pack(pady=20)
key=['F8']
option=["Better Speed(Ofline)"]
txtbox=[False]
TEXT_CASE=["Original(The 1-st example.)"]
check_for_key_press_(window)
# Ekzekutimi i dritares
window.mainloop()