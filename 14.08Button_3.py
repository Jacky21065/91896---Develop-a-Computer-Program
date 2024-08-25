#Date: 14/08/24
#Author: Jacky 
#Purpose: Button 3 - Sunken Buttons with Deep Border

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

# Encapsulate the code into a main function for code execution
# Start the Program Running
def main():
    # Start the GUI buttons and labels up
    setup_buttons()
    # Set the GUI window title
    main_window.title("Julie's Party Hire Store")
    # Set the GUI window background colour
    main_window.configure(bg='MediumSpringGreen')
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
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Row #", bg="DeepSkyBlue2").grid(column=0, row=10, padx=1, pady=5)  # Row Heading
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Receipt Number:", bg="DeepSkyBlue2").grid(column=1, row=10, padx=1, pady=5) # Reciept Number Heading
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Name:", bg="DeepSkyBlue2").grid(column=2, row=10, padx=1, pady=5) # Name Heading
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Item Name:", bg="DeepSkyBlue2").grid(column=3, row=10, padx=1, pady=5) # Item Name Heading
    Label(main_window, font=("Segoe UI", 10, "bold"), text="Quantity Hired:", bg="DeepSkyBlue2").grid(column=4, row=10, padx=1, pady=5) # Quantity Hired Heading

    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=str(name_count + 1), fg="black", bg="MediumSpringGreen").grid(column=0, row=name_count+11) # Row number
        Label(main_window, text=hired_items[name_count][3], fg="black", bg="MediumSpringGreen").grid(column=1, row=name_count+11) # Receipt Number
        Label(main_window, text=hired_items[name_count][0], fg="black", bg="MediumSpringGreen").grid(column=2, row=name_count+11) # Name
        Label(main_window, text=hired_items[name_count][1], fg="black", bg="MediumSpringGreen").grid(column=3, row=name_count+11) # Item Name
        Label(main_window, text=hired_items[name_count][2], fg="black", bg="MediumSpringGreen").grid(column=4, row=name_count+11) # Quantity Hired
        name_count += 1
        counters['name_count'] = name_count

# Check the inputs are all valid
def check_inputs():
    input_check = 0

    # Check that customer full name is not blank, otherwise Display Error Message
    if len(entry_name.get()) == 0:
        messagebox.showerror('Error', 'Customer Full Name: Cannot be blank.')
        input_check = 1
    # Check that customer full name contains only alphabet letters and spaces, otherwise Display Error Message
    elif not all(char.isalpha() or char.isspace() for char in entry_name.get()):
        messagebox.showerror('Error', 'Customer Full Name: Please input only alphabet letters and spaces.')
        input_check = 1

    # Check that an item is selected, otherwise Error Message
    if len(combo_box.get()) == 0:
        messagebox.showerror('Error', 'Item Name: Please select an item.')
        input_check = 1

    # Check the number of Quantity Hired is not blank, otherwise Error Display Message
    quantity_text = entry_quantity.get()
    if len(entry_quantity.get()) == 0:
        messagebox.showerror('Error', 'Quantity Hired: Cannot be blank.')
    # Check the number of Quantity Hired is not below 1, otherwise Error Display Message
    elif quantity_text.isdigit():
        quantity = int(quantity_text)
        if quantity < 1:
            messagebox.showerror('Error', 'Quantity Hired: Value must be higher and in between 1 - 500.')
            input_check = 1
    # Check the number of Quantity Hired is not above 500, otherwise Display Error Message
        elif quantity > 500:
            messagebox.showerror('Error', 'Quantity Hired: Value must be lower and in between 1 - 500.')
            input_check = 1
    else:
    # Check the number of Quantity Hired contains only numerical values, otherwise Display Error Message
        messagebox.showerror('Error', 'Quantity Hired: Please input only numeric values.')
        input_check = 1

    # If no errors, then append the entry data
    if input_check == 0:
        append_item()

# Append entry data into a save file
def append_item():
    # Generate a random receipt number for the user 
    receipt_number = random.randint(1000, 9999)
    # Append each item to its own column in the Program Window
    hired_items.append([entry_name.get(), combo_box.get(), entry_quantity.get(), receipt_number])
    # Clear all entry data in the Program Window
    entry_name.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    counters['total_entries'] += 1
    # Save all details after appending the item
    save_info()  

def save_info():
    # Save the user details into a text file
    with open('user_data.txt', 'a') as file:
        for item in hired_items:
            file.write("Name: {}\n".format(item[0]))
            file.write("Item: {}\n".format(item[1]))
            file.write("Quantity: {}\n".format(item[2]))
            file.write("Receipt Number: {}\n".format(item[3]))
            file.write("\n")
    # Display a Window Message to let the uesr know their data has been successfully saved to a data file
    messagebox.showinfo("Save", "Data Saved")

# Deletes a row from the list, when the user clicks on the Delete button
def delete_row():
    try:
        # Calculate which row is to be deleted and delete it   
        row_number = int(delete_item.get()) - 1
        if row_number < 0 or row_number >= counters['total_entries']:
            messagebox.showerror('Error', 'Invalid row number.')
        else:
            del hired_items[row_number]    
            counters['total_entries'] -= 1
            delete_item.delete(0, 'end')
            # Clear the hired item labels
            for widget in main_window.winfo_children():
                if isinstance(widget, Label) and widget.cget('text') != "" and widget.cget('bg') == 'MediumSpringGreen':
                    widget.destroy()
            # Reprint all the items in the list
            print_hired_item_details()
    # If the inputted row number can not be calculated, then display Error Message
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid row number.')
    setup_buttons()

# Create the buttons and labels and display them on the Program Window
def setup_buttons():
    # Create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location using columns and rows
    Label(main_window, font=("Segoe UI", 10), text="Customer Full Name", bg='MediumSpringGreen').grid(column=0, row=1, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Item Name", bg='MediumSpringGreen').grid(column=0, row=2, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Quantity Hired", bg='MediumSpringGreen').grid(column=0, row=3, sticky=E)
     # Sunken Buttons with Deep Border
    Button(main_window, font=("Arial", 10), text="Submit", bg='orange', bd=7, relief=SUNKEN).grid(column=3, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Quit", bg='orange', bd=7, relief=SUNKEN).grid(column=4, row=1, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Print Details", bg='orange', bd=7, relief=SUNKEN).grid(column=4, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Delete Row", bg='orange', bd=7, relief=SUNKEN).grid(column=4, row=4, sticky=E, padx=5, pady=5)
   
   # Load and place the bin icon next to the "Delete Row" button
    try:
        bin_icon_path = r'C:\Users\21065\OneDrive - Lynfield College\Documents\2PAD 2024\Jacky Zhou - 91897 and 91896 Assessment\Code Prototypes\After Checkpoint 1\Prototype\Bin_icon.png'  # Use raw string for the path
        bin_icon = PhotoImage(file=bin_icon_path)
        bin_icon_label = Label(main_window, image=bin_icon, bg='MediumSpringGreen')
        bin_icon_label.image = bin_icon 
        bin_icon_label.grid(column=5, row=4, padx=5, pady=5)
    # In case the image doesn't display correctly, display an Error Message about this 
    except Exception as e:
        messagebox.showerror("Error", f"Error loading bin icon: {e}")
    
    # Create and place the Combo Box in the correct location for item names
    global combo_box
    combo_box = ttk.Combobox(main_window, width=18, state='readonly')  # Set width of the Combo Box and make it read-only
    combo_box['values'] = ('Forks', 'Spoons', 'Paper Plates', 'Cups', 'Hats', 'Balloons')  # Drop down item options
    combo_box.grid(column=1, row=2)

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
