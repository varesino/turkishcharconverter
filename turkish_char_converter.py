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

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_box.get(1.0, tk.END))
    root.update()  # This line ensures the clipboard contents are updated
    show_fading_popup("Text copied successfully!")

def show_fading_popup(message):
    popup = tk.Toplevel(root)
    popup.wm_overrideredirect(True)  # Removes window decorations
    popup.geometry("+%d+%d" % (root.winfo_x() + 50, root.winfo_y() + 50))
    label = ttk.Label(popup, text=message, padding=(10, 5))
    label.pack()
    
    def fade_away():
        alpha = popup.attributes("-alpha")
        if alpha > 0:
            popup.attributes("-alpha", alpha - 0.1)
            root.after(100, fade_away)
        else:
            popup.destroy()

    root.after(1000, fade_away)  # Start fading after 1 second

# GUI Setup
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
convert_btn.grid(row=4, column=0, pady=10)

copy_btn = ttk.Button(frame, text="Copy Text", command=copy_to_clipboard)
copy_btn.grid(row=4, column=1, pady=10)

root.mainloop()