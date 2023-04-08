import csv
import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title("Call Data Recorder")

# create a frame for the form elements
form_frame = ttk.Frame(window)
form_frame.pack()

# create form labels
ttk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(form_frame, text="Phone Number").grid(row=1, column=0, padx=5, pady=5)
ttk.Label(form_frame, text="Call Duration").grid(row=2, column=0, padx=5, pady=5)

# create form input fields
name_var = tk.StringVar()
ttk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)
phone_var = tk.StringVar()
ttk.Entry(form_frame, textvariable=phone_var).grid(row=1, column=1, padx=5, pady=5)
duration_var = tk.StringVar()
ttk.Entry(form_frame, textvariable=duration_var).grid(row=2, column=1, padx=5, pady=5)

# create a function to handle form submission
def submit_form():
    name = name_var.get()
    phone_number = phone_var.get()
    duration = duration_var.get()

    # write data to CSV file
    with open('data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone_number, duration])

    # clear form fields
    name_var.set('')
    phone_var.set('')
    duration_var.set('')

# create submit button
submit_button = ttk.Button(form_frame, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# start the event loop
window.mainloop()
