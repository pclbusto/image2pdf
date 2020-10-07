import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image
from PIL import ImageMode
import sys
import os

separador = '/'

def create_pdf (lista_nombre_imagenes, nombre_archivo_salida):
    lista_imagenes = []
    for nombre_imagen in lista_nombre_imagenes:
        imagen = Image.open(nombre_imagen)
        if var_check_bw.get() == 1:
            imagen = imagen.convert('1')
        else:
            imagen = imagen.convert('L')

        imagen = imagen.resize(((int)(0.75*imagen.size[0]),(int)(0.75*imagen.size[1])))
        lista_imagenes.append(imagen)
    print(lista_imagenes)
    lista_normalizada = [imagen.convert('RGB') for imagen in lista_imagenes]
    print(nombre_archivo_salida)
    lista_normalizada[0].save(nombre_archivo_salida, save_all=True, append_images=lista_normalizada[1:])


def open_file():
    """Open a file for editing."""
    filepath = askdirectory()
    if not filepath:

        return
    # txt_edit.delete(1.0, tk.END)
    print(filepath)
    label_path['text'] = filepath
    window.title(f"Simple Text Editor - {filepath}")

def crear_pdf():
    file_name_list = [label_path['text']+separador+nombre_archivo for nombre_archivo in os.listdir(label_path['text']) if
                      nombre_archivo[-3:] in ['jpg', 'png', 'gif']]
    print(file_name_list)
    create_pdf(file_name_list, label_path['text']+separador+text_field.get())
    label_status['text'] = 'Status: Archivo Generado exitosamente'
    print(var_check_bw.get())

window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0,  weight=1)
window.columnconfigure(1,  weight=1)

var_check_bw = tk.IntVar()

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, pady=10)
btn_open = tk.Button(fr_buttons, text="Cargar Directorio", command=open_file)
btp_procesar = tk.Button(fr_buttons, text="Crear archivo Pdf", command=crear_pdf)
label_path = tk.Label(fr_buttons, width=100)
label_path.grid(row=0, column=0,sticky="n")
text_field = tk.Entry(fr_buttons, width=100)
text_field.grid(row=1, column=0,sticky="n")
label_status = tk.Label(fr_buttons, text='Status:', width=100)
label_status.grid(row=2, column=0,sticky="n")
btn_open.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
btp_procesar.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
check_bw = tk.Checkbutton(fr_buttons, text="Blanco y Negro", variable=var_check_bw)

window.mainloop()