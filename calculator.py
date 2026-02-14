import tkinter as tk

# Function to calculate
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = choice.get()

    if operation == "Add":
        result.set(num1 + num2)
    elif operation == "Subtract":
        result.set(num1 - num2)
    elif operation == "Multiply":
        result.set(num1 * num2)
    elif operation == "Divide":
        result.set(num1 / num2)

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
choice = tk.StringVar()
choice.set("Add")

tk.OptionMenu(root, choice, "Add", "Subtract", "Multiply", "Divide").pack()

# Result
result = tk.StringVar()
tk.Label(root, text="Result").pack()
tk.Label(root, textvariable=result).pack()

# Button
tk.Button(root, text="Calculate", command=calculate).pack()

root.mainloop()
