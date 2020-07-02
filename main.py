from PIL import Image, ImageTk
import tkinter as tk
import os
import sys

def create_pdf (lista_nombre_imagenes, nombre_archivo_salida):

    lista_imagenes = []
    for nombre_imagen in lista_nombre_imagenes:
        lista_imagenes.append(Image.open(nombre_imagen))
    lista_normalizada = [imagen.convert('RGB') for imagen in lista_imagenes]
    lista_normalizada[0].save(nombre_archivo_salida,save_all=True, append_images=lista_normalizada[1:])


if __name__== "__main__":
    if len(sys.argv) == 3:
        file_name_list = [nombre_archivo for nombre_archivo in  os.listdir(sys.argv[1]) if nombre_archivo[-3:] in ['jpg', 'png', 'gif']]
        create_pdf(file_name_list, sys.argv[2])
    else:
        print("python main.py 'RUTA IAMGENES' 'NOMBRE ARCHIVO PDF'")
#
# def showPopulation(*args):
#     idxs = list_box.curselection()
#     if len(idxs)==1:
#         idx = int(idxs[0])
#         print(file_name_list[idx])
#         fp = open(file_name_list[idx])
#         pic = Image.open(file_name_list[idx])
#         tkpic = ImageTk.PhotoImage(pic)
#         label = tk.Label(image = tkpic)
#         label.grid()
#         # label['image'] = image
#
# root = tk.Tk()
# c = tk.Frame(root)
# c.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
# file_name_list = [nombre_archivo for nombre_archivo in  os.listdir('.') if nombre_archivo[-3:] in ['jpg', 'png', 'gif']]
# cnames = tk.StringVar(value=file_name_list)
# list_box = tk.Listbox(c, listvariable=cnames, height=20, width=50)
# label = tk.Label(c, text='Full name:', height=20, width=20)
# label.grid(column=1, row=2)
# list_box.bind('<<ListboxSelect>>', showPopulation)
# list_box.grid(column=1, row=1)
# root.mainloop()

