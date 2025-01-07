import random as rn
import tkinter as tk
import string

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x320")
root.resizable(0,0)

def copy_to_clipboard():
    text = entry.get()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    print("Copied to clipboard:", text)

def generate_random_code():
    if checkbox_var.get():
        letter_part = ''.join(rn.choices(string.ascii_letters, k=4))
    else:
        letter_part = ''.join(rn.choices(string.ascii_lowercase, k=4))
    if specialvar.get():
        special_pool = string.digits + "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
    else:
        special_pool = string.digits
    special_part = ''.join(rn.choices(special_pool, k=4))
    random_code = letter_part + special_part
    return random_code

def generate(entry):
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, generate_random_code())
    entry.config(state="readonly")

title = tk.Label(root, text="Random Password Generator", font=("Helvetica", 16))
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 24))
entry.config(justify="center", state="readonly")
entry.pack(pady=20)

btn = tk.Button(root, text="Generate Password", font=("Helvetica", 16), command=lambda: generate(entry))
btn.pack(pady=10)

copyBtn = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 16), command=lambda: copy_to_clipboard())
copyBtn.pack()

checkbox_var = tk.BooleanVar()
capsCheck = tk.Checkbutton(root, text="Capitals", font=("Helvetica", 12), variable=checkbox_var)
capsCheck.pack(pady=5)

specialvar = tk.BooleanVar()
specialCheck = tk.Checkbutton(root, text="Special Characters", font=("Helvetica", 12), variable=specialvar)
specialCheck.pack(pady=1)

if __name__ == "__main__":
    root.mainloop()
