# Import Tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import os

# Global variable to track the receipt window
receipt_window = None
# Global variables for storing the position and size of the receipt window
receipt_window_position = (0, 0)
receipt_window_size = (1200, 600)

# Input validation functions
def validate_name(input_value):
    if len(input_value) > 25:
        messagebox.showerror('Invalid Input', 'Customer Full Name: Cannot exceed 25 characters, including spaces.')
        return False
    elif not all(char.isalpha() or char.isspace() for char in input_value):
        messagebox.showerror('Invalid Input', 'Customer Full Name: Please input only alphabet letters and spaces.')
        return False
    return True    

import string

def validate_quantity(input_value):
    if input_value.isdigit():
        quantity = int(input_value)
        if quantity == 0:
            messagebox.showerror('Invalid Input', 'Quantity Hired: Numeric value cannot be zero.')
            return False
        elif 1 <= quantity <= 500:
            return True
        else:
            messagebox.showerror('Invalid Input', 'Quantity Hired: Numeric value must be between 1 and 500.')
            return False
    elif input_value.isalpha():
        messagebox.showerror('Invalid Input', 'Quantity Hired: Please input only numeric values, not alphabet letters.')
        return False
    elif not all(char.isalpha() or char.isspace() for char in input_value):
        messagebox.showerror('Invalid Input', 'Quantity Hired: Please input only numeric values, not symbols.')
        return False 
    elif input_value == "":
        return True  # Allow empty input for the Entry (user might be typing)
    else:
        messagebox.showerror('Invalid Input', 'Quantity Hired: Please input valid numeric values from 1 - 500.')
        return False

def validate_delete_entry(input_value):
    if input_value.isdigit():
        quantity = int(input_value)
        if quantity == 0:
            messagebox.showerror('Invalid Input', 'Delete Row: Numeric value cannot be zero.')
            return False
        elif quantity > 1000:
            messagebox.showerror('Invalid Input', 'Delete Row: Cannot exceed 1000.')
            return False
        else:
            return True  # Input is valid
    elif input_value.isalpha():
        messagebox.showerror('Invalid Input', 'Delete Row: Please input only numeric values, not alphabet letters.')
        return False
    elif not all(char.isalpha() or char.isspace() for char in input_value):
        messagebox.showerror('Invalid Input', 'Delete Row: Please input only alphabet letters and spaces, not symbols.')
        return False  
    elif input_value == "":
        return True  # Allow empty input for the Entry (user might be typing)
    else:
        messagebox.showerror('Invalid Input', 'Delete Row: Please input valid numeric values.')
        return False


# Function to open the Receipt window
def open_receipt_window():
    global receipt_window
    global receipt_window_position, receipt_window_size

    # If the receipt window is already open, destroy it
    if receipt_window is not None and receipt_window.winfo_exists():
        receipt_window_position = (receipt_window.winfo_x(), receipt_window.winfo_y())
        receipt_window_size = (receipt_window.winfo_width(), receipt_window.winfo_height())
        receipt_window.destroy()

    # Create a new receipt window
    receipt_window = Toplevel(main_window)
    receipt_window.title("Reciepts")
    receipt_window.geometry("1200x600")
    receipt_window.resizable(False,False)
    receipt_window.configure(bg='MediumSpringGreen')

    # Set the position and size of the new receipt window
    receipt_window.geometry(f"{receipt_window_size[0]}x{receipt_window_size[1]}+{receipt_window_position[0]}+{receipt_window_position[1]}")
    receipt_window.resizable(False, False)
    receipt_window.configure(bg='MediumSpringGreen')

    # Define the padding for the headings
    heading_padding = {'padx': 10, 'pady': 5}

    # Define the column weights to make sure columns expand evenly
    for col in range(10):
        receipt_window.grid_columnconfigure(col, weight=1)

    # Create column headings in the Receipt window
    Label(receipt_window, font=("Segoe UI", 18, "bold"), text="Row #:", bg='MediumSpringGreen', anchor='center').grid(column=0, row=0, **heading_padding, sticky='ew')
    Label(receipt_window, font=("Segoe UI", 18, "bold"), text="Receipt #:", bg='MediumSpringGreen', anchor='center').grid(column=1, row=0, **heading_padding, sticky='ew')
    Label(receipt_window, font=("Segoe UI", 18, "bold"), text="Customer Full Name:", bg='MediumSpringGreen', anchor='center').grid(column=2, row=0, **heading_padding, sticky='ew')
    Label(receipt_window, font=("Segoe UI", 18, "bold"), text="Item Name:", bg='MediumSpringGreen', anchor='center').grid(column=4, row=0, **heading_padding, sticky='ew')
    Label(receipt_window, font=("Segoe UI", 18, "bold"), text="Quantity Hired:", bg='MediumSpringGreen', anchor='center').grid(column=6, row=0, **heading_padding, sticky='ew')

    # Check if there are items to display
    if hired_items:
        #Display each item in the Receipt Window
        for i, item in enumerate(hired_items):
            Label(receipt_window, font=("Segoe UI", 14, "bold"), text=str(i + 1), fg="black", bg="#3CB371", anchor='center').grid(column=0, row=i + 1, **heading_padding, sticky='ew')
            Label(receipt_window, font=("Segoe UI", 14, "bold"), text=item[3], fg="black", bg="#3CB371", anchor='center').grid(column=1, row=i + 1, **heading_padding, sticky='ew')
            Label(receipt_window, font=("Segoe UI", 14, "bold"), text=item[0], fg="black", bg="#3CB371", anchor='center').grid(column=2, row=i + 1, **heading_padding, sticky='ew')
            Label(receipt_window, font=("Segoe UI", 14, "bold"), text=item[1], fg="black", bg="#3CB371", anchor='center').grid(column=4, row=i + 1, **heading_padding, sticky='ew')
            Label(receipt_window, font=("Segoe UI", 14, "bold"), text=item[2], fg="black", bg="#3CB371", anchor='center').grid(column=6, row=i + 1, **heading_padding, sticky='ew')
    
    # If no data to display
    else:
        Label(receipt_window, text="No data to display.\nNeed Help? Use the Help button on the main window.", font=("Segoe UI", 20, "bold"), bg='red', anchor='center').grid(column=0, row=1, **heading_padding, columnspan=10, sticky='ew')
        
# Encapsulate the code into a main function for code execution
def main():
    # Start the GUI buttons and labels up
    setup_buttons()
    # Set the GUI window title
    main_window.title("Julie's Party Hire Store")
    # Set the GUI window background colour
    main_window.configure(bg='MediumSpringGreen')
    # Windows Geometry to set Window size 
    main_window.geometry("1000x500")
    # Make the window non-resizable
    main_window.resizable(False, False)
    # Set the window icon
    icon_image = PhotoImage(file=r'C:\Users\21065\OneDrive - Lynfield College\Documents\2PAD 2024\Jacky Zhou - 91897 and 91896 Assessment\Code Prototypes\After Checkpoint 1\Prototype\icon.png')  
    main_window.iconphoto(False, icon_image)
    main_window.mainloop()

def print_hired_item_details():
    name_count = 0
        # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=str(name_count + 1), fg="black", bg="MediumSpringGreen").grid(column=0, row=name_count+11) # Row number
        Label(main_window, text=hired_items[name_count][3], fg="black", bg="MediumSpringGreen").grid(column=1, row=name_count+11) # Receipt Number
        Label(main_window, text=hired_items[name_count][0], fg="black", bg="MediumSpringGreen").grid(column=2, row=name_count+11) # Name
        Label(main_window, text=hired_items[name_count][1], fg="black", bg="MediumSpringGreen").grid(column=3, row=name_count+11) # Item Name
        Label(main_window, text=hired_items[name_count][2], fg="black", bg="MediumSpringGreen").grid(column=4, row=name_count+11) # Quantity Hired
        name_count += 1
        counters['name_count'] = name_count

def check_inputs():
    input_check = 0

    # Capitalise the customer full name before validation
    full_name = entry_name.get().title()

    # Check that customer full name is not blank
    if len(entry_name.get()) == 0:
        messagebox.showerror('Invalid Input', 'Customer Full Name: Cannot be blank.')
        input_check = 1
    elif not all(char.isalpha() or char.isspace() for char in entry_name.get()):
        messagebox.showerror('Invalid Input', 'Customer Full Name: Please input only alphabet letters and spaces.')
        input_check = 1

    # Check that an item is selected
    if len(combo_box.get()) == 0:
        messagebox.showerror('Invalid Input', 'Item Name: Please select an item.')
        input_check = 1

    # Check if Quantity Hired is not empty and is valid
    quantity_text = entry_quantity.get()
    if len(quantity_text) == 0:
       messagebox.showerror('Invalid Input', 'Quantity Hired: Cannot be blank.')
       input_check = 1
    elif quantity_text.isdigit():
        quantity = int(quantity_text)
        if quantity < 1 or quantity > 500:
            messagebox.showerror('Invalid Input', 'Quantity Hired: Value must be between 1 and 500.')
            input_check = 1
    else:
        messagebox.showerror('Invalid Input', 'Quantity Hired: Please input only numeric values.')
        input_check = 1

    # If no errors, append the entry data
    if input_check == 0:
        append_item(full_name)

def append_item(full_name):
    # Generate a random receipt number for the user 
    receipt_number = random.randint(1000, 9999)
    # Append each item to its own column in the Program Window
    hired_items.append([full_name, combo_box.get(), entry_quantity.get(), receipt_number])
    # Clear all entry data in the Program Window
    entry_name.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    combo_box.set('')
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
            file.write("Receipt #: {}\n".format(item[3]))
            file.write("\n")
    # Display a Window Message to let the user know their data has been successfully saved to a data file
    messagebox.showinfo("Save", """Details Saved.
Click the "Reciepts" button to view your details.""")

def delete_row():
    try:
        # Calculate which row is to be deleted and delete it   
        row_number = int(delete_entry.get()) - 1
        del hired_items[row_number]
        counters['total_entries'] -= 1

        # Clear entry fields in the main window and open the Receipt window to show updated data
        delete_entry.delete(0, 'end')
        entry_name.delete(0, 'end')
        entry_quantity.delete(0, 'end')
        combo_box.set('')
        open_receipt_window()

    except (ValueError, IndexError):
        # Show error message if the row number is invalid
        messagebox.showerror('Error', 'Invalid Row Number')

def setup_buttons():
    # Setup Buttons
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Customer Full Name", bg='MediumSpringGreen').grid(column=0, row=1, sticky=E, padx=1, pady=10)
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Item Name", bg='MediumSpringGreen').grid(column=0, row=2, sticky=E, padx=1, pady=10)
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Quantity Hired", bg='MediumSpringGreen').grid(column=0, row=3, sticky=E, padx=1, pady=10)
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Row #", bg='MediumSpringGreen').grid(column=2, row=6, sticky=E, padx=1, pady=10)
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Submit", bg='orange', bd=5, relief=RAISED, command=check_inputs).grid(column=3, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Quit", bg='orange', bd=5, relief=RAISED, command=quit).grid(column=4, row=1, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Delete Row", bg='orange', bd=5, relief=RAISED, command=delete_row).grid(column=4, row=6, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Receipts", bg='orange', bd=5, relief=RAISED, command=open_receipt_window).grid(column=4, row=2, sticky=E, padx=5, pady=5)

    # Setup Entry Fields
    global entry_name, combo_box, entry_quantity, delete_entry
    entry_name = Entry(main_window, width=24, validate='key', validatecommand=(main_window.register(validate_name), '%P'))
    entry_name.grid(column=1, row=1, padx=1, pady=10, sticky=W)

    combo_box = ttk.Combobox(main_window, width=21, state='readonly', validate='key', validatecommand=(main_window.register(validate_name), '%P'))
    combo_box['values'] = ('Forks', 'Spoons', 'Paper Plates', 'Cups', 'Hats', 'Balloons')
    combo_box.grid(column=1, row=2, padx=1, pady=10, sticky=W)

    entry_quantity = Entry(main_window, width=24, validate='key', validatecommand=(main_window.register(validate_quantity), '%P'))
    entry_quantity.grid(column=1, row=3, padx=1, pady=10, sticky=W)

    delete_entry = Entry(main_window, width=24, validate='key', validatecommand=(main_window.register(validate_delete_entry), '%P'))
    delete_entry.grid(column=3, row=6, padx=1, pady=10, sticky=W)

    # Create a frame for the help and terms buttons at the bottom center
    bottom_frame = Frame(main_window, bg='MediumSpringGreen')
    bottom_frame.grid(column=0, row=10, columnspan=5, pady=20, sticky='ew')

    # Add Help and Terms buttons to the bottom frame
    Button(bottom_frame, font=("Segoe UI", 16, "bold"), text="Help", bg='orange', bd=5, relief=RAISED, command=open_help_window).pack(side=LEFT, padx=10)
    Button(bottom_frame, font=("Segoe UI", 16, "bold"), text="Terms", bg='orange', bd=5, relief=RAISED, command=open_terms_window).pack(side=LEFT, padx=10)

   # Set the weight of the row containing the bottom_frame to push it down
    main_window.grid_rowconfigure(10, weight=1)

# Add functions for Help and Terms buttons
def open_help_window():
    messagebox.showinfo("Help", """How to use:
1) Next to "Customer Full Name",  enter your full name.
2) Next to "Item Name", select the item you want to hire.
3) Next to "Quantity Hired", type in the quantity of the item you want to hire (1-500).
4) Click the "Submit" button to add the item to your reciepts.


View your Receipts:
Click the "Receipts" button to open a window displaying all your hired items, alongside your details.


Delete an Item:
Enter the row number of the item you want to remove and click the "Delete Row" button to delete it from the list.


Quit:
Click "Quit" to close Julie's Party Hire application.


Terms and Conditions:
Click "Terms" to read the terms and conditions of renting items through Julie's Party Hire.


Get Help:
Click "Help" for how to manage your party hire items and how to the Julie's Party Hire application.


If you require any additional help, email or ring us.
Have a great day :)""")

def open_terms_window():
    messagebox.showinfo("Terms", """Julie's Party Hire Store agrees to provide its equipments on hire in accordance with the terms and conditions stated:


1. The period of hire shall commence from the time and date when the Equipment is delivered and shall terminate when the Equipment is returned to the Owner's storage premises.


2. The Owner would undertake to provide the Equipment to the Hirer by the agreed date but failing to do so due to any justified cause would not subject the Owner to any liability.


3. The Hirer must collect the hired equipments from a venue specified by the Owner.


4. A bond will be required when hiring items. This will be added to the hire charge and will be refunded to the Hirer if the equipment is returned in good condition and clean state.


5. Deposits are required on all future bookings. The amount will be 50% of the total hire fee due unless otherwise discussed with the company.


6. The Hirer must check the hired equipment(s) upon acceptance at the time of hiring.


7. The Hirer must take reasonable care of the Equipment and must not deliberately damage it, tamper with it, attempt to repair it or mistreat it in any way.


8. The Hirer must ensure that any instructions supplied by the Owner for use of the Equipment shall be fully observed.

""")

# Main Window settings
main_window = Tk()

# Track user data 
hired_items = []
counters = {
    'total_entries': 0,
    'name_count': 0,
}

# Execute main window functions
if __name__ == "__main__":
    main()
