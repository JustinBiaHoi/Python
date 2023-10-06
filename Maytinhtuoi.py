import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        input_value = entry_input.get()
        current_year = datetime.now().year

        if var.get() == "Tuổi":
            if input_value.isdigit():
                age = int(input_value)
                birth_year = current_year - age
                result_label.config(text=f"Năm sinh của bạn là: {birth_year}")
            else:
                result_label.config(text="Nhập tuổi hợp lệ!")
        elif var.get() == "Năm sinh":
            if len(input_value) == 4 and input_value.isdigit():
                birth_year = int(input_value)
                age = current_year - birth_year
                result_label.config(text=f"Tuổi của bạn là: {age} tuổi")
            else:
                result_label.config(text="Nhập năm sinh hợp lệ!")

    except ValueError:
        result_label.config(text="Nhập năm sinh hoặc tuổi hợp lệ!")

def on_enter_pressed(event):
    calculate_age()

window = tk.Tk()
window.title("Máy tính tuổi thông minh")
window.geometry("400x200")

title_label = tk.Label(
    window, text="MÁY TÍNH TUỔI THÔNG MINH", font=("Helvetica", 16, "bold"), fg="red"
)
title_label.pack()

label_option = tk.Label(window, text="Chọn phương án nhập:")
label_option.pack()

var = tk.StringVar()
var.set("Tuổi")

radio_age = tk.Radiobutton(window, text="Tuổi", variable=var, value="Tuổi")
radio_birth_year = tk.Radiobutton(
    window, text="Năm sinh", variable=var, value="Năm sinh"
)

radio_age.pack()
radio_birth_year.pack()

label_instruction = tk.Label(window, text="Nhập năm sinh hoặc tuổi:")
entry_input = tk.Entry(window)
entry_input.bind('<Return>', on_enter_pressed)  

calculate_button = tk.Button(window, text="Tính", command=calculate_age)

result_label = tk.Label(window, text="")

label_instruction.pack()
entry_input.pack()
calculate_button.pack()
result_label.pack()

window.mainloop()
