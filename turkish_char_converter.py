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

def on_key_release(event=None):
    input_text = input_box.get(1.0, tk.END).strip()
    converted_text = convert_to_html_codes(input_text)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, converted_text)

def copy_to_clipboard():
    text_to_copy = output_box.get(1.0, tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)
    root.update()
    show_fading_popup("Text copied!")

def clear_input():
    input_box.delete(1.0, tk.END)
    output_box.delete(1.0, tk.END)

def show_fading_popup(message):
    popup = tk.Toplevel(root)
    popup.wm_overrideredirect(True)
    x = root.winfo_x() + (root.winfo_width() // 2) - (popup.winfo_reqwidth() // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (popup.winfo_reqheight() // 2)
    popup.geometry("+%d+%d" % (x, y))
    label = ttk.Label(popup, text=message, padding=(10, 5))
    label.pack()
    
    def fade_away():
        alpha = popup.attributes("-alpha")
        if alpha > 0:
            popup.attributes("-alpha", alpha - 0.1)
            root.after(100, fade_away)
        else:
            popup.destroy()

    root.after(1000, fade_away)

# GUI Setup
root = tk.Tk()
root.title("Turkish🇹🇷 Char Converter")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Set column and row weights
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(3, weight=1)

ttk.Label(frame, text="Input Text:").grid(row=0, column=0, sticky=tk.W, pady=5)
input_box = tk.Text(frame, height=10, width=50)
input_box.grid(row=1, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
input_box.bind("<KeyRelease>", on_key_release)

ttk.Label(frame, text="Converted Text:").grid(row=2, column=0, sticky=tk.W, pady=5)
output_box = tk.Text(frame, height=10, width=50)
output_box.grid(row=3, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

copy_btn = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.grid(row=4, column=1, pady=10, sticky=tk.E)

clear_btn = ttk.Button(frame, text="Clear", command=clear_input)
clear_btn.grid(row=4, column=0, pady=10, sticky=tk.W)

root.mainloop()