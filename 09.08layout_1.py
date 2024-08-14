#Date: 09/08/24
#Author: Jacky 
#Purpose: Layout trial 1

# Import Tkinter
from tkinter import *
# Import Tkinter Windows for Error Messages and Information Messages
from tkinter import messagebox
from tkinter import ttk
# Import Tkinter Image Label
from tkinter import Tk, Label
# Import Tkinter Random Receipt Number Generator
import random
import os

# Quit subroutine
def quit():
    main_window.destroy()

def main():
    setup_buttons()
    main_window.title("Julie's Party Hire Store")
    main_window.configure(bg='Khaki')
    main_window.geometry("800x500")
    main_window.resizable(False, False)
    icon_image = PhotoImage(file=r'C:\Users\21065\OneDrive - Lynfield College\Documents\2PAD 2024\Jacky Zhou - 91897 and 91896 Assessment\Code Prototypes\After Checkpoint 1\Prototype\icon.png')  
    main_window.iconphoto(False, icon_image)
    main_window.mainloop()

def print_hired_item_details():
    name_count = 0
    Label(main_window, font=("Arial", 10, "bold"), text="Row #", bg="Lawn Green").grid(column=0, row=10, padx=5, pady=5)
    Label(main_window, font=("Arial", 10, "bold"), text="Receipt Number:", bg="Lawn Green").grid(column=1, row=10, padx=5, pady=5)
    Label(main_window, font=("Arial", 10, "bold"), text="Name:", bg="Lawn Green").grid(column=2, row=10, padx=5, pady=5)
    Label(main_window, font=("Arial", 10, "bold"), text="Item Name:", bg="Lawn Green").grid(column=3, row=10, padx=5, pady=5)
    Label(main_window, font=("Arial", 10, "bold"), text="Quantity Hired:", bg="Lawn Green").grid(column=4, row=10, padx=5, pady=5)

    while name_count < counters['total_entries']:
        Label(main_window, text=str(name_count + 1), fg="black", bg="Khaki").grid(column=0, row=name_count+11, padx=5, pady=2)
        Label(main_window, text=hired_items[name_count][3], fg="black", bg="Khaki").grid(column=1, row=name_count+11, padx=5, pady=2)
        Label(main_window, text=hired_items[name_count][0], fg="black", bg="Khaki").grid(column=2, row=name_count+11, padx=5, pady=2)
        Label(main_window, text=hired_items[name_count][1], fg="black", bg="Khaki").grid(column=3, row=name_count+11, padx=5, pady=2)
        Label(main_window, text=hired_items[name_count][2], fg="black", bg="Khaki").grid(column=4, row=name_count+11, padx=5, pady=2)
        name_count += 1
        counters['name_count'] = name_count

def check_inputs():
    input_check = 0
    if len(entry_name.get()) == 0:
        messagebox.showerror('Error', 'Customer Full Name: Cannot be blank.')
        input_check = 1
    elif not all(char.isalpha() or char.isspace() for char in entry_name.get()):
        messagebox.showerror('Error', 'Customer Full Name: Please input only alphabet letters and spaces.')
        input_check = 1
    if len(combo_box.get()) == 0:
        messagebox.showerror('Error', 'Item Name: Please select an item.')
        input_check = 1
    quantity_text = entry_quantity.get()
    if len(entry_quantity.get()) == 0:
        messagebox.showerror('Error', 'Quantity Hired: Cannot be blank.')
    elif quantity_text.isdigit():
        quantity = int(quantity_text)
        if quantity < 1:
            messagebox.showerror('Error', 'Quantity Hired: Value must be higher and in between 1 - 500.')
            input_check = 1
        elif quantity > 500:
            messagebox.showerror('Error', 'Quantity Hired: Value must be lower and in between 1 - 500.')
            input_check = 1
    else:
        messagebox.showerror('Error', 'Quantity Hired: Please input only numeric values.')
        input_check = 1
    if input_check == 0:
        append_item()

def append_item():
    receipt_number = random.randint(1000, 9999)
    hired_items.append([entry_name.get(), combo_box.get(), entry_quantity.get(), receipt_number])
    entry_name.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    counters['total_entries'] += 1
    save_info()  

def save_info():
    with open('user_data.txt', 'a') as file:
        for item in hired_items:
            file.write("Name: {}\n".format(item[0]))
            file.write("Item: {}\n".format(item[1]))
            file.write("Quantity: {}\n".format(item[2]))
            file.write("Receipt Number: {}\n".format(item[3]))
            file.write("\n")
    messagebox.showinfo("Save", "Data Saved")

def delete_row():
    try:
        row_number = int(delete_item.get()) - 1
        if row_number < 0 or row_number >= counters['total_entries']:
            messagebox.showerror('Error', 'Invalid row number.')
        else:
            del hired_items[row_number]    
            counters['total_entries'] -= 1
            delete_item.delete(0, 'end')
            for widget in main_window.winfo_children():
                if isinstance(widget, Label) and widget.cget('text') != "" and widget.cget('bg') == 'Khaki':
                    widget.destroy()
            print_hired_item_details()
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid row number.')
    setup_buttons()

def setup_buttons():
    Label(main_window, font=("Arial", 10), text="Customer Full Name", bg='Khaki').grid(column=0, row=1, sticky=E, padx=5, pady=5)
    Label(main_window, font=("Arial", 10), text="Item Name", bg='Khaki').grid(column=0, row=2, sticky=E, padx=5, pady=5)
    Label(main_window, font=("Arial", 10), text="Quantity Hired", bg='Khaki').grid(column=0, row=3, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Quit", bg='Khaki', command=quit, width=10).grid(column=4, row=1, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Submit", bg='Khaki', command=check_inputs).grid(column=3, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Print Details", bg='Khaki', command=print_hired_item_details, width=10).grid(column=4, row=2, sticky=E, padx=5, pady=5)
    Label(main_window, font=("Arial", 10), text="Row #", bg='Khaki').grid(column=3, row=3, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Delete Row", bg='Khaki', command=delete_row, width=10).grid(column=4, row=4, sticky=E, padx=5, pady=5)
    try:
        bin_icon_path = r'C:\Users\21065\OneDrive - Lynfield College\Documents\2PAD 2024\Jacky Zhou - 91897 and 91896 Assessment\Code Prototypes\After Checkpoint 1\Prototype\Bin_icon.png'
        bin_icon = PhotoImage(file=bin_icon_path)
        bin_icon_label = Label(main_window, image=bin_icon, bg='Khaki')
        bin_icon_label.image = bin_icon 
        bin_icon_label.grid(column=5, row=4, padx=5, pady=5)
    except Exception as e:
        messagebox.showerror("Error", f"Error loading bin icon: {e}")

    Button(main_window, font=("comic sans ms", 10), text="Delete Row", bg='Khaki', command=delete_row, width=10).grid(column=4, row=4, sticky=E, padx=5, pady=5)
    global combo_box
    combo_box = ttk.Combobox(main_window, width=18, state='readonly')
    combo_box['values'] = ('Forks', 'Spoons', 'Paper Plates', 'Cups', 'Hats', 'Balloons')
    combo_box.grid(column=1, row=2, padx=5, pady=5)
# Create empty list for hired item details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
hired_items = []
main_window = Tk()
entry_name = Entry(main_window, width=20)  # Set width to match Combo Box
entry_name.grid(column=1, row=1) # Set the Entry Name box to the correct grid location using columns and rows
entry_quantity = Entry(main_window, width=20)  # Set width to match Combo Box
entry_quantity.grid(column=1, row=3) # Set the Quantity Hired box to the correct grid location using columns and rows
delete_item = Entry(main_window, width=20)  # Set width for consistency
delete_item.grid(column=3, row=4) # Set the Delete Item details to the correct grid location using columns and rows
main() # Encapsulate the code into a main function for code execution
