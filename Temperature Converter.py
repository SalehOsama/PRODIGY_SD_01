import tkinter as tk


def convert_temperature():

    temp = float(temp_entry.get())                    # This will store the value entered in a temp_entry(textbox) into 'temp' variable
    Unit = Unit_entry.get()                           # This will store the value entered in a Unit_entry(textbox) into 'Unit' variable

    if Unit == 'C':
        F = (temp * 9/5) + 32                          #  C --> F
        K = temp + 273.15                              # C --> K
        result_label.configure(text=f"Equivalent Fahrenheit: {F} °F\nEquivalent Kelvin: {K} K" )          # print() will print msg in pychram output (Not in GUI window), Hence we use label.configure()

    elif Unit == "F":
        C = (temp - 32) * (5/9)                        # F --> C
        K = (temp + 459.67) * (5/9)                    # F --> K          # K = ((temp - 32)*5)/9 + 273.15
        result_label.configure(text= f"Equivalent Celcius: {C} °C\nEquivalent Kelvin: {K} K" )

    elif Unit == "K" :
        C = temp - 273.15                              # k --> C
        F = ((temp-273.15) * 9/5) + 32                 # K --> F
        result_label.configure(text=f"Equivalent Celcius: {C} °C\nEquivalent Fahrenheit: {F} °F" )

    else:
        result_label.configure(text="!!!Invalid Unit Entered !!!")




root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

temp_label = tk.Label(frame, text= "Enter the temperature value : ")
temp_label.pack()

temp_entry = tk.Entry(frame)
temp_entry.pack(pady = 10)

Unit_label = tk.Label(frame, text="Enter the Unit of Measurement (C, F, or K) : ")
Unit_label.pack()

Unit_entry = tk.Entry(frame)
Unit_entry.pack(pady=10)

convert_button = tk.Button(frame, text="Convert", bg="Green", fg="white", command = convert_temperature)
convert_button.pack(pady = 15)

result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()