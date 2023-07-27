import tkinter as tk

def ui():
    root = tk.Tk()
    root.title('To do app')

    # label = tk.Label(root, text='To do app', font=('Cascadia Code', 20))
    # label.pack(side='top', pady=200)

    label_top = tk.Label(root, text="Etiqueta arriba", bg="lightblue")
    label_left = tk.Label(root, text="Etiqueta izquierda", bg="lightgreen")
    label_right = tk.Label(root, text="Etiqueta derecha", bg="lightcoral")
    label_bottom = tk.Label(root, text="Etiqueta abajo", bg="lightyellow")

    # Usar el método pack con la opción side para colocar las etiquetas en diferentes lados
    label_top.pack(side="top", padx=10, pady=10)
    label_left.pack(side="left", padx=10, pady=10)
    label_right.pack(side="right", padx=10, pady=10)
    label_bottom.pack(side="bottom", padx=10, pady=10)

    root.mainloop() 


