import customtkinter as ctk
from tkinter import filedialog, Spinbox
import win32print
from smatraPDF_print import print_pdf_with_samatra
from spliter import range_spliter
from pypdf import PdfReader

# -------- COLLECT PRINTERS DATA --------
printers_name=[]
flags = win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
printers = win32print.EnumPrinters(flags, None, 1)
for print in printers:
    printers_name.append(print[2])

# -------- SET TK ENV --------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Print & Sign")

# -------- SET WINDOW ICON --------
try:
    app.iconbitmap("printer.ico")
except Exception as e:
    print(f"Could not load icon: {e}")

# -------- FUNCTIONS --------
def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        file_entry.delete(0, "end")
        file_entry.insert(0, file_path)

def send_command():
    copies=copies_spinbox.get()
    reader = PdfReader(file_entry.get())
    pages=range_spliter(len(reader.pages),pages_entry.get())
    for i in range(int(copies)):
        for page in pages:
            print_pdf_with_samatra(printer_menu.get(),file_entry.get(),page)
    copies_spinbox.delete(0,'end')
    file_entry.delete(0,'end')
    pages_entry.delete(0,'end')


# -------- CENTER WINDOW --------
window_width = 600
window_height = 500
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
app.geometry(f"{window_width}x{window_height}+{x}+{y}")
app.configure(bg="#F4F6F7")

# -------- TITLE --------
title_label = ctk.CTkLabel(app, text="Print, Sign & Resume", font=("Segoe UI", 20, "bold"), text_color="#333333")
title_label.pack(pady=(20, 10))

# -------- SELECT PRINTER --------
printer_label = ctk.CTkLabel(app, text="Select Printer", font=("Segoe UI", 14))
printer_label.pack(anchor="w", padx=40, pady=(5, 0))

printer_menu = ctk.CTkOptionMenu(app, values=printers_name)
printer_menu.pack(padx=40, fill="x", pady=5)

# -------- SELECT FILE --------
file_label = ctk.CTkLabel(app, text="Select File", font=("Segoe UI", 14))
file_label.pack(anchor="w", padx=40, pady=(15, 0))

file_frame = ctk.CTkFrame(app, fg_color="transparent")
file_frame.pack(padx=40, fill="x", pady=5)

file_entry = ctk.CTkEntry(file_frame, placeholder_text="Choose your file")
file_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

browse_btn = ctk.CTkButton(file_frame, text="Browse", command=browse_file)
browse_btn.pack(side="right")

# -------- PAGES + COPIES IN ONE ROW --------
pages_frame = ctk.CTkFrame(app, fg_color="transparent")
pages_frame.pack(padx=40, fill="x", pady=(15, 0))

# Labels
pages_label = ctk.CTkLabel(pages_frame, text="Insert Pages", font=("Segoe UI", 14))
pages_label.grid(row=0, column=0, sticky="w", padx=(0, 10))

copies_label = ctk.CTkLabel(pages_frame, text="Copies", font=("Segoe UI", 14))
copies_label.grid(row=0, column=1, sticky="w", padx=(10, 0))

# Entry + Spinbox
pages_entry = ctk.CTkEntry(pages_frame, placeholder_text="e.g.2,5,..")
pages_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(5, 0))

copies_spinbox = Spinbox(pages_frame, from_=1, to=100, width=5)
copies_spinbox.grid(row=1, column=1, pady=(5, 0))

pages_frame.grid_columnconfigure(0, weight=1)

# -------- PRINT BUTTON --------
print_btn = ctk.CTkButton(app, text="Print", height=40, fg_color="#4A90E2",command=send_command)
print_btn.pack(pady=20)



app.mainloop()