import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main application window
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Create a Text widget
text_area = tk.Text(root, wrap='word', undo=True)
text_area.pack(expand=1, fill='both')

# File menu functions
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("New File - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"),
                                                      ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"),
                                                        ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
        root.title(f"{file_path} - Notepad")

# Edit menu functions
def cut_text():
    text_area.event_generate(("<<Cut>>"))

def copy_text():
    text_area.event_generate(("<<Copy>>"))

def paste_text():
    text_area.event_generate(("<<Paste>>"))

# Creating a menu bar
menu_bar = tk.Menu(root)

# Adding File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Adding Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Configuring the menu bar
root.config(menu=menu_bar)

# Run the application
root.mainloop()
