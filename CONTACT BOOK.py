import tkinter as tk
from tkinter import messagebox, simpledialog


# Contact storage
contacts = {}


# Add contact function
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name:
        messagebox.showerror("Error", "Name is required.")
        return
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists.")
        return

    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address,
    }
    update_contact_list()
    messagebox.showinfo("Success", "Contact added successfully!")


# Update contact function
def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter the Name of the Contact:")
    if not name or name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return

    phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:")
    email = simpledialog.askstring("Update Contact", "Enter New Email:")
    address = simpledialog.askstring("Update Contact", "Enter New Address:")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address,
    }
    update_contact_list()
    messagebox.showinfo("Success", "Contact updated successfully!")


# Delete contact function
def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter the Name of the Contact:")
    if not name or name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return

    del contacts[name]
    update_contact_list()
    messagebox.showinfo("Success", "Contact deleted successfully!")


# Search contact function
def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    if not query:
        return

    results = [
        f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}"
        for name, info in contacts.items()
        if query.lower() in name.lower() or query in info["Phone"]
    ]

    if results:
        messagebox.showinfo("Search Results", "\n\n".join(results))
    else:
        messagebox.showerror("Error", "No contact found.")


# View all contacts
def view_contacts():
    if not contacts:
        messagebox.showinfo("Contact List", "No contacts available.")
        return

    contact_list = [
        f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}"
        for name, info in contacts.items()
    ]
    messagebox.showinfo("Contact List", "\n\n".join(contact_list))


# Update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {info['Phone']}")


# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Buttons for contact operations
tk.Button(root, text="Add Contact", command=add_contact, width=20).grid(row=0, column=0, padx=10, pady=5)
tk.Button(root, text="Update Contact", command=update_contact, width=20).grid(row=1, column=0, padx=10, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, width=20).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Search Contact", command=search_contact, width=20).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="View All Contacts", command=view_contacts, width=20).grid(row=4, column=0, padx=10, pady=5)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, width=40, height=15)
contact_listbox.grid(row=0, column=1, rowspan=5, padx=10, pady=5)

# Run the application
root.mainloop()
