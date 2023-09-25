import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
# Función para abrir el cuadro de diálogo y seleccionar archivos PDF
def select_pdf_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
    return file_paths
# Función para unir los archivos PDF seleccionados
def merge_pdfs(pdf_list, output_filename):
    if os.path.exists(output_filename):
        base, ext = os.path.splitext(output_filename)
        index = 2
        while os.path.exists(f"{base}{index}{ext}"):
            index += 1
        output_filename = f"{base}{index}{ext}"

    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    pdf_merger.write(output_filename)
    pdf_merger.close()
    result_label.config(text=f"Archivos PDF unidos con éxito. Guardado como {output_filename}")
# Función que se llama al hacer clic en el botón "Unir PDF"
def merge_button_click():
    selected_files = select_pdf_files()
    if selected_files:
        output_pdf = "resultado.pdf"  # Nombre del archivo PDF de salida
        merge_pdfs(selected_files, output_pdf)
# Configuración de la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Unir Archivos PDF")
# Etiqueta de título
title_label = ttk.Label(root, text="Unir Archivos PDF", font=("Helvetica", 16))
title_label.pack(pady=10)
# Botón para seleccionar archivos PDF
select_button = ttk.Button(root, text="Seleccionar PDFs", command=merge_button_click)
select_button.pack(pady=10)
# Etiqueta de resultado
result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()