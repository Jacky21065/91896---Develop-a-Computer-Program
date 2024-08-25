from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
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
    main_window.mainloop()

# Print details of all hired items
def print_hired_item_details():
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Receipt Number:", bg='red').grid(column=0, row=10)
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Name:", bg='red').grid(column=1, row=10)
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Quantity Hired:", bg='red').grid(column=2, row=10)
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Item Name:", bg='red').grid(column=3, row=10)
    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=hired_items[name_count][0], fg="black", bg="cyan").grid(column=1, row=name_count+8)
        Label(main_window, text=hired_items[name_count][1], fg="black", bg="cyan").grid(column=2, row=name_count+8)
        Label(main_window, text=hired_items[name_count][2], fg="black", bg="cyan").grid(column=3, row=name_count+8)
        Label(main_window, text=hired_items[name_count][3], fg="black", bg="cyan").grid(column=0, row=name_count+8)
        name_count += 1
        counters['name_count'] = name_count

# Check the inputs are all valid
def check_inputs():
    input_check = 0
    # Check that customer full name is not blank and contains only alphabets
    if len(entry_name.get()) == 0 or not entry_name.get().isalpha():
        messagebox.showerror('Error ', 'Please enter your name using ONLY alphabet letters.')
        input_check = 1
    # Check that item is selected, set error text if blank
    if len(combo_box.get()) == 0:
        messagebox.showerror('Error ', 'Please select an item.')
        input_check = 1
    # Check the number of Quantity Hired is not blank and between 1 and 500, set error text if blank
    if entry_quantity.get().isdigit():
        quantity = int(entry_quantity.get())
        if quantity < 1 or quantity > 500:
            messagebox.showerror('Error ', 'Please enter a value from 1-500.')
            input_check = 1
    else:
        messagebox.showerror('Error ', 'Please enter a value from 1-500.')
        input_check = 1
    if input_check == 0: append_item()

    

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
    user_name = entry_name.get()

def save_info():
    Forks = str(Forks.get())
    Spoons = str(Spoons.get())
    Plates = str(Plates.get())
    Cups = str(Cups.get())
    Hats = str(Hats.get())
    Ballons = str(Ballons.get())
    # Save the user details to a text file
    file = open('user_data.txt',w)
    file.write
    with open(file, 'a'):
        file.write("\n")
        file.write("Name: ")
        file.write(entry_name)
        file.write("\n")
        file.write(Forks)
        file.write("  ")
        file.write(Spoons)
        file.write("  ")
        file.write(Plates)
        file.write("  ")
        file.write(Cups)
        file.write("  ")
        file.write(Hats)
        file.write("  ")
        file.write(Ballons)
        file.write("  ")
        file.write("\n")
        file.close()
    messagebox.showinfo("Showinfo", "Data Saved")

    
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
    
    # Create and place the ComboBox for item names
    global combo_box
    combo_box = ttk.Combobox(main_window, width=18, state='readonly')  # Set width and make it read-only
    combo_box['values'] = ('Forks', 'Spoons', 'Paper Plates', 'Cups', 'Hats', 'Balloons')  # Define your item options
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
