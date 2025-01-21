import tkinter as tk

def on_button_click(value):
    current = entry_var.get()
    if value == '=':
        try:
            result = eval(current)
            if isinstance(result, float):
                result = round(result, 10)
                if result.is_integer():
                    result = int(result)
            entry_var.set(str(result))
        except Exception:
            entry_var.set("Error")
    elif value == 'C':
        entry_var.set("")
    elif value == '⌫':
        entry_var.set(current[:-1])
    else:
        entry_var.set(current + value)

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x500")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Courier", 22), justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+'),
    ('⌫')
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn_text = buttons[i][j]
        tk.Button(root, text=btn_text, font=("Courier", 20), width=5, height=2,
                  command=lambda b=btn_text: on_button_click(b)).grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()

