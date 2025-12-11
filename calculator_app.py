import tkinter as tk


def multiplication(num3, num4):
    return num3 * num4


def division(num3, num4):
    return num3 / num4


def plus(num3, num4):
    return num3 + num4


def minus(num3, num4):
    return num3 - num4


window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=18, justify="right", font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

first_num = None
operator = None


def on_number_click(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(digit))


def on_operator_click(op):
    global first_num, operator

    try:
        current = float(entry.get())
    except ValueError:
        current = 0.0

    first_num = current
    operator = op
    entry.delete(0, tk.END)


def on_equal_click():
    global first_num, operator

    if operator is None or first_num is None:
        return

    try:
        second_num = float(entry.get())
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        return

    try:
        if operator == '+':
            result = plus(first_num, second_num)
        elif operator == '-':
            result = minus(first_num, second_num)
        elif operator == '*':
            result = multiplication(first_num, second_num)
        elif operator == '/':
            result = division(first_num, second_num)
        else:
            result = second_num
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: /0")
        first_num = None
        operator = None
        return

    entry.delete(0, tk.END)
    entry.insert(0, str(result))

    # איפוס למהלך הבא
    first_num = None
    operator = None


def on_clear():
    global first_num, operator
    entry.delete(0, tk.END)
    first_num = None
    operator = None


buttons_numbers = [
    ('7', 1, 0),
    ('8', 1, 1),
    ('9', 1, 2),
    ('4', 2, 0),
    ('5', 2, 1),
    ('6', 2, 2),
    ('1', 3, 0),
    ('2', 3, 1),
    ('3', 3, 2),
    ('0', 4, 1),
]

for (text, row, col) in buttons_numbers:
    btn = tk.Button(
        window,
        text=text,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda t=text: on_number_click(t)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

buttons_ops = [
    ('+', 1, 3),
    ('-', 2, 3),
    ('*', 3, 3),
    ('/', 4, 3),
]

for (text, row, col) in buttons_ops:
    btn = tk.Button(
        window,
        text=text,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda op=text: on_operator_click(op)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

btn_equal = tk.Button(
    window,
    text="=",
    width=5,
    height=2,
    font=("Arial", 16),
    command=on_equal_click
)
btn_equal.grid(row=5, column=2, padx=5, pady=5)

btn_clear = tk.Button(
    window,
    text="C",
    width=5,
    height=2,
    font=("Arial", 16),
    command=on_clear
)
btn_clear.grid(row=5, column=0, padx=5, pady=5)

window.mainloop()
