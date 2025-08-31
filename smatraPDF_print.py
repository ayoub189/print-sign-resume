import subprocess
import time


def print_pdf_with_samatra(printer_name,pdf_path,pages):
    exe_path = r"C:\Users\brency\AppData\Local\SumatraPDF\SumatraPDF.exe" 
    if printer_name:
        command = [exe_path, "-print-to", printer_name, "-silent","-print-settings",pages,pdf_path]
    else:
        command = [exe_path, "-print-to-default", "-silent","-print-settings",pages, pdf_path]
    subprocess.run(command)
    time.sleep(1.5)  


