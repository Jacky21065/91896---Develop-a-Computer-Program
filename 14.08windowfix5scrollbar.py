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


# Quit subroutine
def quit():
    main_window.destroy()

# Function to open the Receipt window
def open_receipt_window():
    global receipt_window
    global receipt_window_position, receipt_window_size

    # If the receipt window is already open, destroy it and store its position and size
    if receipt_window is not None and receipt_window.winfo_exists():
        receipt_window_position = (receipt_window.winfo_x(), receipt_window.winfo_y())
        receipt_window_size = (receipt_window.winfo_width(), receipt_window.winfo_height())
        receipt_window.destroy()

    # Create a new receipt window
    receipt_window = Toplevel(main_window)
    receipt_window.title("Receipts")
    
    # Set the position and size of the new receipt window
    receipt_window.geometry(f"{receipt_window_size[0]}x{receipt_window_size[1]}+{receipt_window_position[0]}+{receipt_window_position[1]}")
    receipt_window.resizable(False, False)
    receipt_window.configure(bg="#3CB371")

    # Create a canvas widget for scrolling
    canvas = Canvas(receipt_window, bg='#3CB371', borderwidth=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Create a scrollbar widget
    scrollbar = Scrollbar(receipt_window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create a frame to hold the content
    content_frame = Frame(canvas, bg="#3CB371")
    canvas.create_window((0, 0), window=content_frame, anchor='nw')

    # Update the canvas scrolling region
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    content_frame.bind("<Configure>", update_scroll_region)

    # Define the padding for the headings
    heading_padding = {'padx': 10, 'pady': 5}

    # Define the number of columns
    num_columns = 5

    # Configure the columns to expand and fill the space
    for i in range(num_columns):
        content_frame.columnconfigure(i, weight=1)

    # Create column headings in the Receipt window
    Label(content_frame, font=("Segoe UI", 18, "bold"), text="Row #:", bg="DarkSeaGreen", anchor='center').grid(column=0, row=0, **heading_padding, columnspan=1, sticky='ew')
    Label(content_frame, font=("Segoe UI", 18, "bold"), text="Receipt #:", bg="DarkSeaGreen", anchor='center').grid(column=1, row=0, **heading_padding, columnspan=1, sticky='ew')
    Label(content_frame, font=("Segoe UI", 18, "bold"), text="Customer Full Name:", bg="DarkSeaGreen", anchor='center').grid(column=2, row=0, **heading_padding, columnspan=1, sticky='ew')
    Label(content_frame, font=("Segoe UI", 18, "bold"), text="Item Name:", bg="DarkSeaGreen", anchor='center').grid(column=3, row=0, **heading_padding, columnspan=1, sticky='ew')
    Label(content_frame, font=("Segoe UI", 18, "bold"), text="Quantity Hired:", bg="DarkSeaGreen", anchor='center').grid(column=4, row=0, **heading_padding, columnspan=1, sticky='ew')

    # Check if there are items to display
    if hired_items:
        # Display each item in the Receipt window
        for i, item in enumerate(hired_items):
            Label(content_frame, text=str(i + 1), fg="black", bg="#3CB371", anchor='center').grid(column=0, row=i + 1, **heading_padding, sticky='ew')
            Label(content_frame, text=item[3], fg="black", bg="#3CB371", anchor='center').grid(column=1, row=i + 1, **heading_padding, sticky='ew')
            Label(content_frame, text=item[0], fg="black", bg="#3CB371", anchor='center').grid(column=2, row=i + 1, **heading_padding, sticky='ew')
            Label(content_frame, text=item[1], fg="black", bg="#3CB371", anchor='center').grid(column=3, row=i + 1, **heading_padding, sticky='ew')
            Label(content_frame, text=item[2], fg="black", bg="#3CB371", anchor='center').grid(column=4, row=i + 1, **heading_padding, sticky='ew')
    else:
        # If no data to display
        Label(content_frame, text="No data to display.\nNeed Help? Use the Help button on the main window.", font=("Segoe UI", 20, "bold"), bg='red', anchor='center').grid(column=0, row=1, **heading_padding, columnspan=num_columns, sticky='ew')

        
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
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Customer Full Name", bg='MediumSpringGreen').grid(column=0, row=1, sticky=E, padx=1, pady=10)
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Item Name", bg='MediumSpringGreen').grid(column=0, row=2, sticky=E, padx=1, pady=10)
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Quantity Hired", bg='MediumSpringGreen').grid(column=0, row=3, sticky=E, padx=1, pady=10)
    Label(main_window, font=("Segoe UI", 16, "bold"), text="Row #", bg='MediumSpringGreen').grid(column=2, row=6, sticky=E, padx=1, pady=10)
    
    # Setup Buttons
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Submit", bg='orange', bd=5, relief=RAISED, command=check_inputs).grid(column=3, row=2, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Quit", bg='orange', bd=5, relief=RAISED, command=quit).grid(column=4, row=1, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Delete Row", bg='orange', bd=5, relief=RAISED, command=delete_row).grid(column=4, row=6, sticky=E, padx=5, pady=5)
    Button(main_window, font=("Segoe UI", 16, "bold"), text="Receipts", bg='orange', bd=5, relief=RAISED, command=open_receipt_window).grid(column=4, row=2, sticky=E, padx=5, pady=5)

    # Entry Fields
    global entry_name, combo_box, entry_quantity, delete_entry
    entry_name = Entry(main_window, width=24)
    entry_name.grid(column=1, row=1, padx=1, pady=10, sticky=W)

    combo_box = ttk.Combobox(main_window, width=21, state='readonly')
    combo_box['values'] = ('Forks', 'Spoons', 'Paper Plates', 'Cups', 'Hats', 'Balloons')
    combo_box.grid(column=1, row=2, padx=1, pady=10, sticky=W)

    entry_quantity = Spinbox(main_window, width=22, from_=1, to=500)
    entry_quantity.grid(column=1, row=3, padx=1, pady=10, sticky=W)

    delete_entry = Spinbox(main_window, width=22, from_=1, to=100)
    delete_entry.grid(column=3, row=6, padx=1, pady=10, sticky=W)

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
