import tkinter as tk
from tkinter import ttk, messagebox

# Main Window
root = tk.Tk()
root.title("Employee Registration Form")
root.geometry("600x650")
root.resizable(False, False)

# Title
tk.Label(root, text="Employee Registration Form",
         font=("Arial", 20, "bold")).grid(row=0, column=0,
         columnspan=2, pady=20)

# Variables
employee_id = tk.StringVar()
name = tk.StringVar()
email = tk.StringVar()
phone = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()
address = tk.StringVar()
department = tk.StringVar()
designation = tk.StringVar()
salary = tk.StringVar()

# Employee ID
tk.Label(root, text="Employee ID").grid(row=1, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=employee_id, width=35).grid(row=1, column=1)

# Employee Name
tk.Label(root, text="Employee Name").grid(row=2, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=name, width=35).grid(row=2, column=1)

# Email
tk.Label(root, text="Email").grid(row=3, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=email, width=35).grid(row=3, column=1)

# Phone
tk.Label(root, text="Phone").grid(row=4, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=phone, width=35).grid(row=4, column=1)

# Gender
tk.Label(root, text="Gender").grid(row=5, column=0, padx=20, pady=8, sticky="w")

tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").grid(row=5, column=1, sticky="w")

tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").grid(row=5, column=1, padx=80, sticky="w")

# Date of Birth
tk.Label(root, text="Date of Birth").grid(row=6, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=dob, width=35).grid(row=6, column=1)

# Address
tk.Label(root, text="Address").grid(row=7, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=address, width=35).grid(row=7, column=1)

# Department
tk.Label(root, text="Department").grid(row=8, column=0, padx=20, pady=8, sticky="w")

ttk.Combobox(root, textvariable=department,
             values=["IT", "HR", "Sales", "Finance"],
             width=32).grid(row=8, column=1)

# Designation
tk.Label(root, text="Designation").grid(row=9, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=designation, width=35).grid(row=9, column=1)

# Salary
tk.Label(root, text="Salary").grid(row=10, column=0, padx=20, pady=8, sticky="w")
tk.Entry(root, textvariable=salary, width=35).grid(row=10, column=1)


# Submit Function
def submit():
    messagebox.showinfo(
        "Success",
        "Registration Successful!\n\n"
        "Employee ID: " + employee_id.get() +
        "\nName: " + name.get() +
        "\nEmail: " + email.get() +
        "\nPhone: " + phone.get() +
        "\nGender: " + gender.get() +
        "\nDOB: " + dob.get() +
        "\nAddress: " + address.get() +
        "\nDepartment: " + department.get() +
        "\nDesignation: " + designation.get() +
        "\nSalary: " + salary.get()
    )


# Submit Button
tk.Button(root, text="Submit",
          width=15, command=submit).grid(
          row=11, column=0, columnspan=2, pady=20)

# Run Application
root.mainloop()