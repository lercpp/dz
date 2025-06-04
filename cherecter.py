
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def ok():

    def o():
        com=name_entry.get()
        co=class_pers.get()
        cm=rassa.get()
        c=horizontalScale.get()
        ca=sposob_entry.get()
        a=py_check.get()
        f=p_check.get()
        g=y_check.get()
        hh=check.get()
        pp=gender_but.get()
        ii=gender_but_2.get()
        i=gender_but.get()
        u=gender_ut_2.get()

    w=Toplevel()
    w.title("yees")
    w.geometry("400x400")
    win.resizable(False, False)

    lable_name =Label(w, text=f"Имя: {com}")
    lable_name.pack()

    labe_name =Label(w, text=f"{co}")
    labe_name.pack()

    lale_name =Label(w, text=f"{cm}")
    lale_name.pack()

    able_name =Label(w, text=f"{c}")
    able_name.pack()

    labl_name =Label(w, text=f"{ca}")
    labl_name.pack()

    lable_nam =Label(w, text=f"{a}")
    lable_nam.pack()

    lable_nae =Label(w, text=f"{f}")
    lable_nae.pack()

    lable_nme =Label(w, text=f"{g}")
    lable_ame.pack()

    lable_ame =Label(w, text=f"{hh}")
    lable_ame.pack()

    lablename =Label(w, text=f"{pp}")
    lablename.pack()

    lble_name =Label(w, text=f"{ii}")
    lble_name.pack()

    labe_name =Label(w, text=f"{i}")
    labe_name.pack()

    lable1_name =Label(w, text=f"{u}")
    lable1_name.pack()


    win = Toplevel() 
    win.title("Профиль")
    win.geometry("400x400")
    win.resizable(False, False)

    content_1=Frame(Toplevel)

    name_entry=ttk.Entry(content_1)
    name_entry.grid(row=1)

    ok=["Воин","Маг","Лучник","Вор"]
    class_pers= ttk.Combobox(content_1, values=ok) 
    class_pers.grid(row=2)

    am=["Человек","Эльф","Орк","Гном"]
    rassa=ttk.Combobox(content_1, values=am)
    rassa.grid(row=3)

    horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=30)
    horizontalScale.grid(row=4)

    sposob_entry=ttk.Entry(content_1)
    sposob_entry.grid(row=5)

    python = IntVar()
    py_check=ttk.Checkbutton(content_1,text="Огненый шар",variable=python)
    py_check.grid(pady=5,padx=40,row=6,column=1)

    pytho = IntVar()
    p_check=ttk.Checkbutton(content_1,text="Лечение",variable=pytho)
    p_check.grid(pady=5,padx=40,row=6,column=2)

    pyhon = IntVar()
    y_check=ttk.Checkbutton(content_1,text="Невидимость",variable=pyhon)
    y_check.grid(pady=5,padx=40,row=6,column=3)

    ython = IntVar()
    check=ttk.Checkbutton(content_1,text="Взлом",variable=ython)
    check.grid(pady=5,padx=40,row=6,column=4)

    lang = StringVar(value="Меч")
    
    gender_but=ttk.Radiobutton(content_1,text="",value="Меч", variable=lang)
    gender_but.grid(row=6,column= 1)

    gender_but_2=ttk.Radiobutton(content_1,value="Лук", variable=lang,text="Лук")
    gender_but_2.grid(row=6,column=2)

    gender_but=ttk.Radiobutton(content_1,value="Посох", variable=lang,text="Посох")
    gender_but.grid(row=6,column=3)

    gender_ut_2=ttk.Radiobutton(content_1,value="Кинжал", variable=lang,text="Кинжал")
    gender_ut_2.grid(row=6,column=4)

    bth=Button(content_1,text="GO",command=o)
    bth.grid(row=7)

    content_1.pack()
    

root = Tk()
root.title("pers")
root.geometry("450x315")
root.resizable(False, False)

content = Frame(root)
content.pack(fill="x")

label = ttk.Label(content, text="Welcome", font=("Arial", 20))
label.pack(pady=3)

label_1 = ttk.Label(content, text="Start creating a character!", font=("Arial", 10))
label_1.pack(pady=5)

bth=Button(content,bg="red",text="Go", width=20, height=5,command=ok)
bth.pack(pady=10)

content.pack()

root.mainloop()