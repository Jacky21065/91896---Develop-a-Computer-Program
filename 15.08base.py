"""
    *   Author: Jacky Zhou
    *   Date: 15th August


    *   AS91896/AS91897 Program
    *   2PAD


    *   Program and GUI created using Tkinter, Python and Idle on Windows 11
    *   Icons designed by me using Adobe Illustrator

"""



# Import necessary modules
from tkinter import *  # Import the entire Tkinter library for GUI components
from tkinter import messagebox  # Import messagebox for error and information pop-ups
from tkinter import ttk  # Import ttk for advanced widgets in Tkinter
import random  # Import random module for generating random numbers
import os  # Import os module for operating system dependent functionality

# Set a global variable to track the receipt window
receipt_window = None
# Global variables for storing the position of the receipt window
receipt_window_position = (0, 0)
# Global variables for storing the size of the receipt window
receipt_window_size = (1200, 600)

# Input validation functions for Customer Full Name, Quantity Hired, and Delete Row entry boxes

# Input validation function for Customer Full Name
def validate_name(input_value):
    """
    Validates the Customer Full Name field.
    Ensures that the input does not exceed 25 characters and contains only alphabetic characters or spaces.
    """
    if len(input_value) > 25:
        messagebox.showerror(
            'Invalid Input', 'Customer Full Name: Cannot exceed 25 characters, including spaces.'
        )
        return False
    elif not all(char.isalpha() or char.isspace() for char in input_value):
        messagebox.showerror(
            'Invalid Input', 'Customer Full Name: Please input only alphabet letters and spaces.'
        )
        return False
    return True

# Input validation function for Quantity Hired entry box
def validate_quantity(input_value):
    """
    Validates the Quantity Hired field.
    Ensures that the input is a number between 1 and 500, and does not contain alphabetic characters or symbols.
    """
    if input_value.isdigit():
        quantity = int(input_value)
        if quantity == 0:
            messagebox.showerror(
                'Invalid Input', 'Quantity Hired: Numeric value cannot be zero.'
            )
            return False
        elif 1 <= quantity <= 500:
            return True
        else:
            messagebox.showerror(
                'Invalid Input', 'Quantity Hired: Numeric value must be between 1 and 500.'
            )
            return False
    elif input_value.isalpha():
        messagebox.showerror(
            'Invalid Input', 'Quantity Hired: Please input only numeric values, not alphabet letters.'
        )
        return False
    elif not all(char.isalpha() or char.isspace() for char in input_value):
        messagebox.showerror(
            'Invalid Input', 'Quantity Hired: Please input only numeric values, not symbols.'
        )
        return False
    elif input_value == "":
        return True  # Allow empty input to clear the entry box
    else:
        messagebox.showerror(
            'Invalid Input', 'Quantity Hired: Please input valid numeric values from 1 - 500.'
        )
        return False

# Input validation function for Delete Row entry box
def validate_delete_entry(input_value):
    """
    Validates the Delete Row field.
    Ensures that the input is a number between 1 and 1000, and does not contain alphabetic characters or symbols.
    """
    if input_value.isdigit():
        quantity = int(input_value)
        if quantity == 0:
            messagebox.showerror(
                'Invalid Input', 'Delete Row: Numeric value cannot be zero.'
            )
            return False
        elif quantity > 1000:
            messagebox.showerror(
                'Invalid Input', 'Delete Row: Cannot exceed 1000.'
            )
            return False
        else:
            return True  # Input is valid
    elif input_value.isalpha():
        messagebox.showerror(
            'Invalid Input', 'Delete Row: Please input only numeric values, not alphabet letters.'
        )
        return False
    elif not all(char.isalpha() or char.isspace() for char in input_value):
        messagebox.showerror(
            'Invalid Input', 'Delete Row: Please input only numeric values, not symbols.'
        )
        return False
    elif input_value == "":
        return True  # Allow empty input to clear the entry box
    else:
        messagebox.showerror(
            'Invalid Input', 'Delete Row: Please input valid numeric values.'
        )
        return False

# Function to open the second window, which is the "Receipt" window
def open_receipt_window():
    """
    Opens or reopens the "Receipt" window.
    If already open, it retains the previous size and position before reopening.
    """
    global receipt_window, receipt_window_position, receipt_window_size

    if receipt_window is not None and receipt_window.winfo_exists():
        receipt_window_position = (
            receipt_window.winfo_x(), receipt_window.winfo_y()
        )
        receipt_window_size = (
            receipt_window.winfo_width(), receipt_window.winfo_height()
        )
        receipt_window.destroy()

    # Create a new "Receipt" window
    receipt_window = Toplevel(main_window)
    receipt_window.title("Receipts")
    receipt_window.geometry("1200x600")
    receipt_window.resizable(False, False)
    receipt_window.configure(bg='MediumSpringGreen')

    # Retain the position and size of the "Receipt" window
    receipt_window.geometry(
        f"{receipt_window_size[0]}x{receipt_window_size[1]}+"
        f"{receipt_window_position[0]}+{receipt_window_position[1]}"
    )
    receipt_window.resizable(False, False)
    receipt_window.configure(bg='MediumSpringGreen')

    # Define the padding for the headings for the x-axis (horizontal) and y-axis (vertical)
    heading_padding = {'padx': 10, 'pady': 5}

    # Define the column weights to make sure columns expand evenly
    for col in range(10):
        receipt_window.grid_columnconfigure(col, weight=1)

    # Create column headings in the Receipt window
    Label(
        receipt_window, font=("Segoe UI", 18, "bold"), text="Row #:", 
        bg='MediumSpringGreen', anchor='center'
    ).grid(column=0, row=0, **heading_padding, sticky='ew')
    Label(
        receipt_window, font=("Segoe UI", 18, "bold"), text="Receipt #:", 
        bg='MediumSpringGreen', anchor='center'
    ).grid(column=1, row=0, **heading_padding, sticky='ew')
    Label(
        receipt_window, font=("Segoe UI", 18, "bold"), text="Customer Full Name:", 
        bg='MediumSpringGreen', anchor='center'
    ).grid(column=2, row=0, **heading_padding, sticky='ew')
    Label(
        receipt_window, font=("Segoe UI", 18, "bold"), text="Item Name:", 
        bg='MediumSpringGreen', anchor='center'
    ).grid(column=4, row=0, **heading_padding, sticky='ew')
    Label(
        receipt_window, font=("Segoe UI", 18, "bold"), text="Quantity Hired:", 
        bg='MediumSpringGreen', anchor='center'
    ).grid(column=6, row=0, **heading_padding, sticky='ew')

    # Check if there are items to display
    if hired_items:
        # Display each item in the Receipt Window, underneath headings
        for i, item in enumerate(hired_items):
            Label(
                receipt_window, font=("Segoe UI", 14, "bold"), text=str(i + 1),
                fg="black", bg="#3CB371", anchor='center'
            ).grid(column=0, row=i + 1, **heading_padding, sticky='ew')
            Label(
                receipt_window, font=("Segoe UI", 14, "bold"), text=item[3], 
                fg="black", bg="#3CB371", anchor='center'
            ).grid(column=1, row=i + 1, **heading_padding, sticky='ew')
            Label(
                receipt_window, font=("Segoe UI", 14, "bold"), text=item[0], 
                fg="black", bg="#3CB371", anchor='center'
            ).grid(column=2, row=i + 1, **heading_padding, sticky='ew')
            Label(
                receipt_window, font=("Segoe UI", 14, "bold"), text=item[1], 
                fg="black", bg="#3CB371", anchor='center'
            ).grid(column=4, row=i + 1, **heading_padding, sticky='ew')
            Label(
                receipt_window, font=("Segoe UI", 14, "bold"), text=item[2], 
                fg="black", bg="#3CB371", anchor='center'
            ).grid(column=6, row=i + 1, **heading_padding, sticky='ew')
    else:
        # If no data to display, display this error message on the "Receipts" window
        Label(
            receipt_window, text="No data to display.\nNeed Help? Use the Help button on the main window.",
            font=("Segoe UI", 20, "bold"), bg='red', anchor='center'
        ).grid(column=0, row=1, **heading_padding, columnspan=10, sticky='ew')
        
# Encapsulate the code into a main function for code execution, which is modular and reusable.
def main():
    # Start the GUI buttons and labels up.
    setup_buttons()
    # Set the title of the main window to "Julie's Party Hire Store".
    main_window.title("Julie's Party Hire Store")
    # Set the colour of the main window to be MediumSpringGreen.
    main_window.configure(bg='MediumSpringGreen')
    # Set the size of the main window to "1000" in length and "500" in width.
    main_window.geometry("1000x500")
    # Disable the resizable function for both length and width of the "Reciept" window
    # so that the user is not able to resize the window length and width.
    main_window.resizable(False, False)
    # Set the window icon to a party image.
    icon_image = PhotoImage(file=r'C:\Users\21065\OneDrive - Lynfield College\Documents\2PAD 2024\Jacky Zhou - 91897 and 91896 Assessment\Code Prototypes\After Checkpoint 1\Prototype\icon.png')  
    main_window.iconphoto(False, icon_image)
    # Keeps the main window running.
    main_window.mainloop()

# Define the function that prints the hired item details on the "Receipts" window.
def print_hired_item_details():
    # Sets an index to iterate through the list of items.
    name_count = 0
        # Add each item in the list into its own row.
    while name_count < counters['total_entries']:
        # Background colour is MediumSpringGreen.
        Label(main_window, text=str(name_count + 1), fg="black", bg="MediumSpringGreen").grid(column=0, row=name_count+11) 
        Label(main_window, text=hired_items[name_count][3], fg="black", bg="MediumSpringGreen").grid(column=1, row=name_count+11) 
        Label(main_window, text=hired_items[name_count][0], fg="black", bg="MediumSpringGreen").grid(column=2, row=name_count+11) 
        Label(main_window, text=hired_items[name_count][1], fg="black", bg="MediumSpringGreen").grid(column=3, row=name_count+11) 
        Label(main_window, text=hired_items[name_count][2], fg="black", bg="MediumSpringGreen").grid(column=4, row=name_count+11) 
        name_count += 1
        counters['name_count'] = name_count

# Define the function that checks inputted data by the user, immediately after they click the Submit button.
def check_inputs():
    # Set input_check value equal to 0, which means that no errors are present in the user's entry before validation happens.
    # This is needed to make sure validation happens correctly.
    input_check = 0

    # Capitalise the Customer Full name before validation.
    full_name = entry_name.get().title()

    # Validation for Customer Full Name, check that the inputted entry for Customer Full Name is not blank.
    if len(entry_name.get()) == 0:
        # If the Customer Full Name is blank, display this error message immediately after they click the submit button.
        messagebox.showerror('Invalid Input', 'Customer Full Name: Cannot be blank.')
        # Set input_check value equal to 1, which means that there has been an error in the user's entry after validation happened.
        input_check = 1
        
    # Validation for Item Name, check that the user has selected an item from the combo box.
    if len(combo_box.get()) == 0:
        # If the Item Name combobox is blank and an item has not been selected, display this error message immediately after they click the submit button.
        messagebox.showerror('Invalid Input', 'Item Name: Please select an item.')
        # Set input_check value equal to 1, which means that there has been an error in the user's entry after validation happened.
        input_check = 1

    # Retreieve the value inputted for Quantity Hired to check it is not empty and is valid
    quantity_text = entry_quantity.get()
    # Validation for Quantity Hired, check that the inputted entry for Quantity Hired is not blank.
    if len(quantity_text) == 0:
        # If Quantity Hired is blank, display this error message imemdiately after they click the submit button.
       messagebox.showerror('Invalid Input', 'Quantity Hired: Cannot be blank.')
        # Set input_check value equal to 1, which means that there has been an error in the user's entry after validation happened.
       input_check = 1

    # After validation, input_check = 0 as there are no more errors that have not been addressed.
    # If no errors, append all the inputted entry to be displayed in the "Receipts" window.
    if input_check == 0:
        # Call the function that appends the inputted entry to be in the "Receipts" window.
        append_item(full_name)

#  Define the function that appends the inputted entry to be in the "Receipts" window.
def append_item(full_name):
    # Generate a random receipt number to be printed on the "Reciepts" window, alongside the user's inputted entries
    # The random receipt number generated will be from a range of 1000 - 9999, including 1000 and 9999.
    receipt_number = random.randint(1000, 9999)
    # Append each entry input to its own column on the "Reciepts" window.
    hired_items.append([full_name, combo_box.get(), entry_quantity.get(), receipt_number])
    # Clear all entry data in the input boxes in the main window, immediately after the user clicks the "Submit" button.
    # Clear the "Customer Full Name" field.
    entry_name.delete(0, 'end')
    # Clear the "Quantity Deleted" field.
    entry_quantity.delete(0, 'end')
    # Clear the "Quantity Hired" field via inputting a blank space into the combobox.
    combo_box.set('')
    counters['total_entries'] += 1
    # Call the function that saves all details after appending an entry.
    save_info()  

# Define the function that saves all details after appending an entry.
def save_info():
    # Save the user details into a text file.
    # This text file is named "user_data.txt" and can be found in the same folder as this current .py file
    with open('user_data.txt', 'a') as file:
        # For loop goes through each entry input one by one so that they can be saved into a text file
        for item in hired_items:
            # Save "Customer Full Name" entry input
            file.write("Name: {}\n".format(item[0]))
            # Save "Item Name" entry input
            file.write("Item: {}\n".format(item[1]))
            # Save "Quantity Hired" entry input
            file.write("Quantity Hired: {}\n".format(item[2]))
            # Save "Receipt #" entry input
            file.write("Receipt #: {}\n".format(item[3]))
            # Leave a blank line at the end of the code so that there is a blank line for the next entry
            # This leaves breathing space for the user when reading and viewing their past data, achieving an aesthetically pleasing text file
            file.write("\n")
    # Display a Window Message to let the user know their data has been successfully saved to a data file
    messagebox.showinfo("Save", """Details Saved.
Click the "Reciepts" button to view your details.""")

# Define the function that deletes a row of inputted data off the "Reciepts" window.
def delete_row():
    try:
        # Calculate which row is to be deleted and delete it.
        # int(delete_entry.get()) converts the inputted entry from string type to integer type.
        # -1 subtracts 1 from the integer value.
        # This is done because list indices in Python are zero-based, meaning the first item is at index 0, the second at index 1, and so on.
        # If the user inputs 1 (assuming they think of the first row as 1), subtracting 1 will give them the correct zero-based index 0.
        row_number = int(delete_entry.get()) - 1
        # Deletes the row at the specified row number from the "Receipts" window.
        del hired_items[row_number]
        # Decreases the value of 'total_entries' by 1.
        # This is done to keep the count in sync with the removal of an entry from the "Receipts" window.
        counters['total_entries'] -= 1

        # Clear entry fields in the main window.
        delete_entry.delete(0, 'end')
        # Clear the "Customer Full Name" field.
        entry_name.delete(0, 'end')
        # Clear the "Item Name" field via inputting a blank space into the combobox.  
        combo_box.set('')
        # Clear the "Quantity Hired" field.
        entry_quantity.delete(0, 'end')
        # Open the "Reciepts" window so that the user can see their inputted row has been deleted.
        open_receipt_window()

  # Handle the case where the row number provided for deletion is invalid.
  # If the row number is not valid (e.g., it is out of range or not a number), a ValueError or IndexError may be raised.
  # Instead of trying to delete an invalid row, show an error message to the user indicating that the row number is invalid.
    except (ValueError, IndexError):
        # Show error message if the row number is invalid
        messagebox.showerror('Error', 'Invalid Row Number')

# Define the function that lays out and sets up the buttons for the main window
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

    # Setup the entry fields: entry_name, combo_box, entry_quantity and delete_entry.
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

    # Create a frame for the help and terms buttons at the bottom center.
    bottom_frame = Frame(main_window, bg='MediumSpringGreen')
    bottom_frame.grid(column=0, row=10, columnspan=5, pady=20, sticky='ew')

    # Add Help and Terms buttons to the bottom frame.
    Button(bottom_frame, font=("Segoe UI", 16, "bold"), text="Help", bg='orange', bd=5, relief=RAISED, command=open_help_window).pack(side=LEFT, padx=10)
    Button(bottom_frame, font=("Segoe UI", 16, "bold"), text="Terms", bg='orange', bd=5, relief=RAISED, command=open_terms_window).pack(side=LEFT, padx=10)

   # Set the weight of the row containing the bottom_frame to push it down.
    main_window.grid_rowconfigure(10, weight=1)

# Define function on the "Help" window that will open when the user clicks on the "Help" button.
def open_help_window():
    # Display this message in the "Help" window when the user clicks on the "Help" button.
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

# Define function the "Terms and Conditions" window that will open when the user clicks on the "Terms" button.
def open_terms_window():
    # Display this message in the "Terms and Conditions" window when the user clicks on the "Terms and Conditions" button.
    messagebox.showinfo("Terms and Conditions", """Julie's Party Hire Store agrees to provide its equipments on hire in accordance with the terms and conditions stated:


1. The period of hire shall commence from the time and date when the Equipment is delivered and shall terminate when the Equipment is returned to the Owner's storage premises.


2. The Owner would undertake to provide the Equipment to the Hirer by the agreed date but failing to do so due to any justified cause would not subject the Owner to any liability.


3. The Hirer must collect the hired equipments from a venue specified by the Owner.


4. A bond will be required when hiring items. This will be added to the hire charge and will be refunded to the Hirer if the equipment is returned in good condition and clean state.


5. Deposits are required on all future bookings. The amount will be 50% of the total hire fee due unless otherwise discussed with the company.


6. The Hirer must check the hired equipment(s) upon acceptance at the time of hiring.


7. The Hirer must take reasonable care of the Equipment and must not deliberately damage it, tamper with it, attempt to repair it or mistreat it in any way.


8. The Hirer must ensure that any instructions supplied by the Owner for use of the Equipment shall be fully observed.

""")

# Create the main application window in Tkinter
# Tk () is a class from the  "Tkinter" module that represents the main window of a Tkinter application.
main_window = Tk()

# This line initializes an empty list called hired_items. This list will be used to store information about items that have been hired.
# As users input data into the application, the relevant information will be appended to this list.
hired_items = []
counters = {
    'total_entries': 0,
    'name_count': 0,
}

# Execute main window functions
if __name__ == "__main__":
    # Encapsulate the code into a main function for code execution, which is modular and reusable.
    main()
