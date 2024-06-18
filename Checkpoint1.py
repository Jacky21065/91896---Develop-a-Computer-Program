from tkinter import *

# Quit subroutine
def quit():
    main_window.destroy()

# Print details of all hired items
def print_hired_item_details():
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica", 10, "bold"), text="RECEIPT NUMBER").grid(column=0, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Item Name").grid(column=2, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Items Hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica", 10, "bold"), text="Delete Row").grid(column=4, row=7)
    # Add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(hired_items[name_count][0])).grid(column=1, row=name_count+8)
        Label(main_window, text=(hired_items[name_count][1])).grid(column=2, row=name_count+8)
        Label(main_window, text=(hired_items[name_count][2])).grid(column=3, row=name_count+8)
        Label(main_window, text=(hired_items[name_count][3])).grid(column=4, row=name_count+8)
        name_count += 1
        counters['name_count'] = name_count

# Check the inputs are all valid
def check_inputs():
    input_check = 0
    Label(main_window, text="               ").grid(column=2, row=0)
    Label(main_window, text="               ").grid(column=2, row=1)
    Label(main_window, text="               ").grid(column=2, row=2)
    Label(main_window, text="               ").grid(column=2, row=3)
    # Check that customer full name is not blank, set error text if blank
    if len(entry_name.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=0)
        input_check = 1
    # Check that item is not blank, set error text if blank
    if len(entry_item.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=1)
        input_check = 1
    # Check the number of items hired is not blank and between 1 and 500, set error text if blank
    if entry_quantity.get().isdigit():
        if int(entry_quantity.get()) < 1 or int(entry_quantity.get()) > 500:
            Label(main_window, fg="red", text="1-500 only").grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="1-500 only").grid(column=2, row=2)
        input_check = 1
    if input_check == 0:
        append_item()

# Add the next hired item to the list
def append_item():
    # Append each item to its own area of the list
    hired_items.append([entry_name.get(), entry_receipt.get(), entry_item.get(), entry_quantity.get()])
    # Clear the boxes
    entry_name.delete(0, 'end')
    entry_receipt.delete(0, 'end')
    entry_item.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    counters['total_entries'] += 1

# Delete a row from the list
def delete_row():
    # Find which row is to be deleted and delete it
    del hired_items[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0, 'end')
    # Clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count+7)
    Label(main_window, text="       ").grid(column=1, row=name_count+7)
    Label(main_window, text="       ").grid(column=2, row=name_count+7)
    Label(main_window, text="       ").grid(column=3, row=name_count+7)
    Label(main_window, text="       ").grid(column=4, row=name_count+7)
    # Print all the items in the list
    print_hired_item_details()

# Create the buttons and labels
def setup_buttons():
    # Create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="Customer Full Name").grid(column=0, row=0, sticky=E)
    Label(main_window, text="Receipt Number").grid(column=0, row=1, sticky=E)
    Label(main_window, text="Item Name").grid(column=0, row=2, sticky=E)
    Label(main_window, text="Items Hired").grid(column=0, row=3, sticky=E)
    Button(main_window, text="Quit", command=quit, width=10).grid(column=4, row=0, sticky=E)
    Button(main_window, text="Submit", command=check_inputs).grid(column=3, row=1)
    Button(main_window, text="Print Details", command=print_hired_item_details, width=10).grid(column=4, row=1, sticky=E)
    Label(main_window, text="Row #").grid(column=3, row=2, sticky=E)
    Button(main_window, text="Delete Row", command=delete_row, width=10).grid(column=4, row=3, sticky=E)
    Label(main_window, text="               ").grid(column=2, row=0)

# Start the program running
def main():
    # Start the GUI up
    setup_buttons()
    main_window.mainloop()

# Create empty list for hired item details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
hired_items = []
main_window = Tk()
entry_name = Entry(main_window)
entry_name.grid(column=1, row=0)
entry_receipt = Entry(main_window)
entry_receipt.grid(column=1, row=1)
entry_item = Entry(main_window)
entry_item.grid(column=1, row=2)
entry_quantity = Entry(main_window)
entry_quantity.grid(column=1, row=3)
delete_item = Entry(main_window)
delete_item.grid(column=3, row=3)
main()
