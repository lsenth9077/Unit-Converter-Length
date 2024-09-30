# IMPORTS
from tkinter import *
from tkinter import ttk

# CONSTANTS
conversions_dict = {"miles": 1609, "kilometers": 1000, "meters": 1, "feet": 1 / 3.281, "inches": 1/39.37, "centimeters": 1 / 100, "millimeters": 1 / 1000, "micrometers": 1 / 1000000, "nanometers": 1 / 1000000000}

# FUNCTION
def converter(quantity, unit, conversion, label_func):
    try:
        quantity = int(quantity)
    except:
        label_func.config(text="NOT A NUMBER")
    else:
        for prefix in conversions_dict.keys():
            for prefix_2 in conversions_dict.keys():
                if unit == prefix and conversion == prefix_2:
                    no_prefix_value = quantity * conversions_dict[prefix]
                    final_conversion = round(no_prefix_value / conversions_dict[prefix_2], 2)
                    answer_text = final_conversion
                    print(answer_text)
                    label_func.config(text=answer_text)


# GUI Interface
root = Tk(className="Unit Converter")

# Label
label = Label(root, text="Unit Converter", font='Comic 30')
label.pack()

# Entry
org_quantity = Entry(root, width=10)
org_quantity.pack(pady=5)

# Picker for Input
combo_box_input = ttk.Combobox(root, values=["meters", "centimeters", "millimeters", "micrometers", "nanometers", "inches", "meters", "miles", "feet"], width=10)
combo_box_input.pack(pady=5)
combo_box_input.set("meters")

# Text
to_text = Label(root, text = "to")
to_text.pack()

# Picker for Output
combo_box_output = ttk.Combobox(root, values=["meters", "centimeters", "millimeters", "micrometers", "nanometers", "inches", "meters", "miles", "feet"], width=10)
combo_box_output.set("centimeters")
combo_box_output.pack(pady=5)

# Answer Text
answer_text = Label(root, text="")
answer_text.pack(pady=3)

# Button (to close and to convert)
button_convert = Button(root, text="Convert", width=10, command= lambda: converter(org_quantity.get(), combo_box_input.get(), combo_box_output.get(), answer_text))
button_convert.pack(pady=5)

# Close Text
button_close = Button(root, text="Close", width=12, command=root.destroy)
button_close.pack()


# Run
mainloop()