import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create the input fields for height and weight
height_label = tk.Label(root, text="ส่วนสูง")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="น้ำหนัก:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Define a function to calculate the BMI
def calculate_bmi():
    height = float(height_entry.get()) / 100  # convert height to meters
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text=f"BMI: {bmi:.2f}")

# Create a button to calculate the BMI
calculate_button = tk.Button(root, text="ได้เท่าไร", command=calculate_bmi)
calculate_button.pack()

# Create a label to display the BMI result
bmi_label = tk.Label(root, text="")
bmi_label.pack()

# Start the main loop
root.mainloop()
