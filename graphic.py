import tkinter as tk
from tkinter import messagebox

def getData():
    try:
        with open('data\\data.txt','r',encoding='UTF 8' ) as data:
            content = data.read()
            if content == '':
                return 'No activities'
            else:
                return content
    
    except FileNotFoundError:
        return "No activities"
        

def ui():
    root = tk.Tk()
    root.title('To do App')
    root.geometry('400x300')

    label_title = tk.Label(root, text='To do App', font=('Cascadia Code', 20))
    label_title.pack(pady=10)

    

    text_box = tk.Text(root, font=('Cascadia Code', 12), wrap=tk.WORD)
    text_box.pack(expand=True, fill='both')


    data = getData()
    text_box.insert(tk.END, data)

    text_box.config(state=tk.DISABLED)

    root.mainloop() 


