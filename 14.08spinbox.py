# Import Tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import os

# Quit subroutine
def quit():
    main_window.destroy()

# Function to open the history window
def open_history_window():
    history_window = Toplevel(main_window)
    history_window.title("Data History")
    history_window.geometry("800x600")
    history_window.configure(bg='MediumSpringGreen')

    # Create column headings in the history window
    Label(history_window, font=("Segoe UI", 10, "bold"), text="Row #", bg="DeepSkyBlue2").grid(column=0, row=0, padx=1, pady=5)
    Label(history_window, font=("Segoe UI", 10, "bold"), text="Receipt Number:", bg="DeepSkyBlue2").grid(column=1, row=0, padx=1, pady=5)
    Label(history_window, font=("Segoe UI", 10, "bold"), text="Name:", bg="DeepSkyBlue2").grid(column=2, row=0, padx=1, pady=5)
    Label(history_window, font=("Segoe UI", 10, "bold"), text="Item Name:", bg="DeepSkyBlue2").grid(column=3, row=0, padx=1, pady=5)
    Label(history_window, font=("Segoe UI", 10, "bold"), text="Quantity Hired:", bg="DeepSkyBlue2").grid(column=4, row=0, padx=1, pady=5)

    # Display each item in the history window
    for i, item in enumerate(hired_items):
        Label(history_window, text=str(i + 1), fg="black", bg="MediumSpringGreen").grid(column=0, row=i+1)
        Label(history_window, text=item[3], fg="black", bg="MediumSpringGreen").grid(column=1, row=i+1)
        Label(history_window, text=item[0], fg="black", bg="MediumSpringGreen").grid(column=2, row=i+1)
        Label(history_window, text=item[1], fg="black", bg="MediumSpringGreen").grid(column=3, row=i+1)
        Label(history_window, text=item[2], fg="black", bg="MediumSpringGreen").grid(column=4, row=i+1)

    # If no data to display
    if not hired_items:
        Label(history_window, text="No data to display.", font=("Segoe UI", 10), bg='MediumSpringGreen').grid(column=0, row=1, padx=5, pady=5, columnspan=5)

# Encapsulate the code into a main function for code execution
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
    # Open the history window to show updated data
    open_history_window()

def save_info():
    # Save the user details into a text file
    with open('user_data.txt', 'a') as file:
        for item in hired_items:
            file.write("Name: {}\n".format(item[0]))
            file.write("Item: {}\n".format(item[1]))
            file.write("Quantity: {}\n".format(item[2]))
            file.write("Receipt Number: {}\n".format(item[3]))
            file.write("\n")
    # Display a Window Message to let the user know their data has been successfully saved to a data file
    messagebox.showinfo("Save", "Data Saved")

def delete_row():
    try:
        # Calculate which row is to be deleted and delete it   
        row_number = int(delete_entry.get()) - 1
        del hired_items[row_number]
        counters['total_entries'] -= 1

        # Clear entry fields in the main window and open the history window to show updated data
        delete_entry.delete(0, 'end')
        entry_name.delete(0, 'end')
        entry_quantity.delete(0, 'end')
        combo_box.set('')
        open_history_window()

    except (ValueError, IndexError):
        # Show error message if the row number is invalid
        messagebox.showerror('Error', 'Invalid Row Number')

def setup_buttons():
    # Setup Widgets
    Label(main_window, font=("Segoe UI", 10), text="Customer Full Name", bg='MediumSpringGreen').grid(column=0, row=1, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Item Name", bg='MediumSpringGreen').grid(column=0, row=2, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Quantity Hired", bg='MediumSpringGreen').grid(column=0, row=3, sticky=E)
    # Raised Buttons with Shadow Effect
    Button(main_window, font=("Arial", 10), text="Submit", bg='orange', bd=5, relief=RAISED, command=check_inputs).grid(column=3, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Quit", bg='orange', bd=5, relief=RAISED, command=quit).grid(column=4, row=1, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Print Details", bg='orange', bd=5, relief=RAISED, command=print_hired_item_details).grid(column=4, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Delete Row", bg='orange', bd=5, relief=RAISED, command=delete_row).grid(column=4, row=4, sticky=E, padx=5, pady=5)
    
    # Add History button
    Button(main_window, font=("Arial", 10), text="History", bg='orange', bd=5, relief=RAISED, command=open_history_window).grid(column=4, row=5, sticky=E, padx=5, pady=5)

    global entry_name, combo_box, entry_quantity, delete_entry
    entry_name = Entry(main_window)
    entry_name.grid(column=1, row=1, padx=1, pady=5, sticky=W)

    combo_box = ttk.Combobox(main_window, width=18, state='readonly')  # Set width of the Combo Box and make it read-only
    combo_box['values'] = ('Bamboo Forks', 'Bamboo Spoons', 'Bamboo Plates', 'Bamboo Cups', 'Paper Hats', 'Biodegradable Balloons')  # Drop down item options
    combo_box.grid(column=1, row=2, padx=1, pady=10, sticky=W)

    entry_quantity = Spinbox(main_window, from_=1, to=500)
    entry_quantity.grid(column=1, row=3, padx=1, pady=5, sticky=W)

    delete_entry = Spinbox(main_window, from_=1, to=100)
    delete_entry.grid(column=3, row=4, padx=1, pady=5, sticky=W)

    # Buttons setup
    # Create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location using columns and rows
    Label(main_window, font=("Segoe UI", 10), text="Customer Full Name", bg='MediumSpringGreen').grid(column=0, row=1, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Item Name", bg='MediumSpringGreen').grid(column=0, row=2, sticky=E)
    Label(main_window, font=("Segoe UI", 10), text="Quantity Hired", bg='MediumSpringGreen').grid(column=0, row=3, sticky=E)
    # Raised Buttons with Shadow Effect
    Button(main_window, font=("Arial", 10), text="Submit", bg='orange', bd=5, relief=RAISED, command=check_inputs).grid(column=3, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Quit", bg='orange', bd=5, relief=RAISED, command=quit).grid(column=4, row=1, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Print Details", bg='orange', bd=5, relief=RAISED, command=print_hired_item_details).grid(column=4, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Arial", 10), text="Delete Row", bg='orange', bd=5, relief=RAISED, command=delete_row).grid(column=4, row=4, sticky=E, padx=5, pady=5)

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
