import tkinter as tk
from tkinter import ttk

def convert_to_html_codes(input_text):
    mapping = {
        'Ç': '&#199;',
        'ç': '&#231;',
        'Ğ': '&#286;',
        'ğ': '&#287;',
        'İ': '&#304;',
        'ı': '&#305;',
        'Ö': '&#214;',
        'ö': '&#246;',
        'Ş': '&#350;',
        'ş': '&#351;',
        'Ü': '&#220;',
        'ü': '&#252;',
    }
    
    for key, value in mapping.items():
        input_text = input_text.replace(key, value)
    
    return input_text

def on_convert():
    input_text = input_box.get(1.0, tk.END)
    converted_text = convert_to_html_codes(input_text)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, converted_text)

#GUI Setup
root = tk.Tk()
root.title("Turkish🇹🇷 Char Converter")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Input Text:").grid(row=0, column=0, sticky=tk.W, pady=5)
input_box = tk.Text(frame, height=10, width=50)
input_box.grid(row=1, column=0, columnspan=2, pady=5)

ttk.Label(frame, text="Converted Text:").grid(row=2, column=0, sticky=tk.W, pady=5)
output_box = tk.Text(frame, height=10, width=50)
output_box.grid(row=3, column=0, columnspan=2, pady=5)

convert_btn = ttk.Button(frame, text="Convert", command=on_convert)
convert_btn.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()