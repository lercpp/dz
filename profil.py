
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def run():
    num1 = num_1_enty.get()
    combo1=combobox1.get()
    combo2=combobox1.get()

    if combo1==combobox2:
         messagebox.showerror(title="валюта", message="Вы ввели одинаковый тип валюты")

    else:
         
        if combo1=="RUB" and combo2=="EUR":
            combo1=int(combo1)
            a=combo1/89
            num_2_enty.config(text=f"{a}")

        if combo1=="RUB" and combo2=="GBP":
            combo1=int(combo1)
            d=combo1/106
            num_2_enty.config(text=f"{d}")
        
        if combo1=="EUR" and combo2=="RUB":
            combo1=int(combo1)
            h=combo1*89
            num_2_enty.config(text=f"{h}")

        if combo1=="EUR" and combo2=="GBP":
            combo1=int(combo1)
            u=combo1/1,19
            num_2_enty.config(text=f"{u}")

        if combo1=="GBP" and combo2=="RUB":
            combo1=int(combo1)
            p=combo1*106
            num_2_enty.config(text=f"{p}")

        if combo1=="GBP" and combo2=="EUR":
            combo1=int(combo1)
            i=combo1*1,19
            num_2_enty.config(text=f"{i}")


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

but=Button(content_1,text="Go",command=run)

content_1.pack()

root.mainloop()