import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to insert numbers
def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Function to clear
def clear():
    entry.delete(0, tk.END)

# Function to calculate
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

for (text,row,col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                  command=equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                  command=lambda t=text: click(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text="C", width=22, height=2, font=("Arial", 14),
          command=clear).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
