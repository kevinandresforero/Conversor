import tkinter as tk
from tkinter import Canvas
from tkinter.filedialog import askopenfilename

NombreArch = askopenfilename()

with open(NombreArch , "r+") as f:
    contenido = f.read()
    print("\nAntes:\n\n"+contenido+"\n\n")
    n = len(contenido) -1
    i=0
    while (i <= n):
        if contenido[i] == ";":
            contenido = contenido.replace(contenido[i],",")
            print(contenido)
        i = i + 1
    f.seek(0)
    f.write(contenido)
    print("\nAntes:\n\n"+contenido+"\n\n")

