#Date: 02/07/24
#Author: Jacky 
#Purpose: Checkpoint 2 AS91896 - Functional Program

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Label
import random
import os

# Quit subroutine
def quit():
    main_window.destroy()

# Start the program running
def main():
    # Start the GUI buttons and labels up
    setup_buttons()
    # Set the GUI window title
    main_window.title("Julie's Party Hire Store")
    # Set the GUI window background colour
    main_window.configure(bg='cyan')
    # Windows Geometry to set Window size 
    main_window.geometry("800x500")
    # Make the window non-resizable
    main_window.resizable(False, False)
    # Set the window icon
    icon_image = PhotoImage(file=r'C:\Users\21065\OneDrive - Lynfield College\Documents\2PAD 2024\Jacky Zhou - 91897 and 91896 Assessment\Code Prototypes\After Checkpoint 1\Prototype\icon.png')  
    main_window.iconphoto(False, icon_image)
    main_window.mainloop()
    
# Print details of all hired items
def print_hired_item_details():
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Receipt Number:", bg='red').grid(column=0, row=10, padx=1, pady=5)
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Name:", bg='red').grid(column=1, row=10, padx=1, pady=5)
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Quantity Hired:", bg='red').grid(column=2, row=10, padx=1, pady=5)
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Item Name:", bg='red').grid(column=3, row=10, padx=1, pady=5)
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Row #", bg='red').grid(column=4, row=10, padx=1, pady=5)  # Row header

    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=hired_items[name_count][3], fg="black", bg="cyan").grid(column=0, row=name_count+11)
        Label(main_window, text=hired_items[name_count][0], fg="black", bg="cyan").grid(column=1, row=name_count+11)
        Label(main_window, text=hired_items[name_count][1], fg="black", bg="cyan").grid(column=2, row=name_count+11)
        Label(main_window, text=hired_items[name_count][2], fg="black", bg="cyan").grid(column=3, row=name_count+11)
        Label(main_window, text=str(name_count + 1), fg="black", bg="cyan").grid(column=4, row=name_count+11)  # Row number
        name_count += 1
        counters['name_count'] = name_count

# Check the inputs are all valid
def check_inputs():
    input_check = 0

    # Check that customer full name is not blank and contains only alphabets
    if len(entry_name.get()) == 0:
        messagebox.showerror('Error', 'Customer Full Name: Cannot be blank.')
        input_check = 1
    elif not entry_name.get().isalpha():
        messagebox.showerror('Error', 'Customer Full Name: Please input only alphabet letters.')
        input_check = 1

    # Check that item is selected, set error text if blank
    if len(combo_box.get()) == 0:
        messagebox.showerror('Error', 'Item Name: Please select an item.')
        input_check = 1

    # Check the number of Quantity Hired is not blank and between 1 and 500
    quantity_text = entry_quantity.get()
    if len(entry_name.get()) == 0:
        messagebox.showerror('Error', 'Quantity Hired: Cannot be blank.')
    if quantity_text.isdigit():
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


# Add the next hired item to the list
def append_item():
    # Generate a random receipt number
    receipt_number = random.randint(1000, 9999)
    # Append each item to its own area of the list
    hired_items.append([entry_name.get(), combo_box.get(), entry_quantity.get(), receipt_number])
    # Clear the boxes
    entry_name.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    counters['total_entries'] += 1
    save_info()  # Save the details after appending the item

def save_info():
    # Save the user details to a text file
    with open('user_data.txt', 'a') as file:
        for item in hired_items:
            file.write("Name: {}\n".format(item[0]))
            file.write("Item: {}\n".format(item[1]))
            file.write("Quantity: {}\n".format(item[2]))
            file.write("Receipt Number: {}\n".format(item[3]))
            file.write("\n")
    messagebox.showinfo("Save", "Data Saved")

# Delete a row from the list
def delete_row():
    try:
        # Find which row is to be deleted and delete it   
        row_number = int(delete_item.get()) - 1
        if row_number < 0 or row_number >= counters['total_entries']:
            messagebox.showerror('Error', 'Invalid row number.')
        else:
            del hired_items[row_number]    
            counters['total_entries'] -= 1
            delete_item.delete(0, 'end')
            # Clear the hired item labels
            for widget in main_window.winfo_children():
                if isinstance(widget, Label) and widget.cget('text') != "" and widget.cget('bg') == 'cyan':
                    widget.destroy()
            # Reprint all the items in the list
            print_hired_item_details()
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid row number.')
    setup_buttons()

# Create the buttons and labels
def setup_buttons():
    # Create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, font=("Segoe UI", 10), text="Customer Full Name", bg='cyan').grid(column=0, row=1, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Item Name", bg='cyan').grid(column=0, row=2, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Quantity Hired", bg='cyan').grid(column=0, row=3, sticky=E)
    Button(main_window, font=("Segoe UI", 10), text="Quit", bg='cyan', command=quit, width=10).grid(column=4, row=1, sticky=E)
    Button(main_window, font=("Segoe UI", 10), text="Submit", bg='cyan', command=check_inputs).grid(column=3, row=2, sticky=E)
    Button(main_window, font=("Segoe UI", 10), text="Print Details", bg='cyan', command=print_hired_item_details, width=10).grid(column=4, row=2, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Row #", bg='cyan').grid(column=3, row=3, sticky=E)
    Button(main_window, font=("Segoe UI", 10), text="Delete Row", bg='cyan', command=delete_row, width=10).grid(column=4, row=4, sticky=E)

   # Load and place the bin icon next to the "Delete Row" button
    try:
        bin_icon_path = r'C:\Users\21065\OneDrive - Lynfield College\Documents\2PAD 2024\Jacky Zhou - 91897 and 91896 Assessment\Code Prototypes\After Checkpoint 1\Prototype\Bin_icon.png'  # Use raw string for the path
        bin_icon = PhotoImage(file=bin_icon_path)
        bin_icon_label = Label(main_window, image=bin_icon, bg='cyan')
        bin_icon_label.image = bin_icon 
        bin_icon_label.grid(column=5, row=4, padx=5, pady=5)
    except Exception as e:
        messagebox.showerror("Error", f"Error loading bin icon: {e}")

    Button(main_window, font=("Segoe UI", 10), text="Delete Row", bg='cyan', command=delete_row, width=10).grid(column=4, row=4, sticky=E)
    
    # Create and place the ComboBox for item names
    global combo_box
    combo_box = ttk.Combobox(main_window, width=18, state='readonly')  # Set width and make it read-only
    combo_box['values'] = ('Forks', 'Spoons', 'Paper Plates', 'Cups', 'Hats', 'Balloons')  # Define item options
    combo_box.grid(column=1, row=2)

# Create empty list for hired item details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
hired_items = []
main_window = Tk()
entry_name = Entry(main_window, width=20)  # Set width to match ComboBox
entry_name.grid(column=1, row=1)
entry_quantity = Entry(main_window, width=20)  # Set width to match ComboBox
entry_quantity.grid(column=1, row=3)
delete_item = Entry(main_window, width=20)  # Optional: Set width for consistency
delete_item.grid(column=3, row=4)
main()
