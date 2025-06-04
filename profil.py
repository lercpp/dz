
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Валюты")
root.geometry("450x315")
root.resizable(False, False)

content = Frame(root)
content.pack(fill="x")

label = ttk.Label(content, text="Welcome", font=("Arial", 20))
label.pack(pady=3)

label_1 = ttk.Label(content, text="This is currency converter!", font=("Arial", 10))
label_1.pack(pady=5)

content_1 = Frame(root)
content_1.pack()

num_1_enty = ttk.Entry(content_1) 
num_1_enty.grid(row=1, column=1,padx=4,pady=4) 

languages = ["RUB", "EUR", "GBP"] 
combobox1 = ttk.Combobox(content_1, values=languages)  
combobox1.grid(row=1, column=2)  

num_2_enty = ttk.Entry(content_1) 
num_2_enty.grid(row=2, column=1)

combobox2 = ttk.Combobox(content_1, values=languages)  
combobox2.grid(row=2, column=2)  

content_1.pack()

root.mainloop()