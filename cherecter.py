
from tkinter import *
from tkinter import ttk


#окно для сбора информации о персонаже и вывод на другом окне

def creature():

    def go():
        name=name_entry.get()
        pers=class_pers_combo.get()
        race=race_combo.get()
        level=level_scale.get()
        ability=ability_entry.get()
        fireball=fireball_check.get()
        treatment=treatment_check.get()
        invisibility=invisibility_check.get()
        hacking=hacking_check.get()
        sword=sword_radio.get()
        onion=onion_radio.get()
        stick=stick_radio.get()
        dagger=dagger_radio.get()

    window=Toplevel()
    window.title("yees")
    window.geometry("400x400")
    window.resizable(False, False)

    lable_name =Label(window, text=f"name: {name}")
    lable_name.grid(row=1)

    lable_pers =Label(window, text=f"character: {pers}")
    lable_pers.grid(row=2)

    lable_race =Label(window, text=f"race: {race}")
    lable_race.grid(row=3)

    lable_level =Label(window, text=f"level: {level}")
    lable_level.grid(row=4)

    lable_ability=Label(window, text=f"ability: {ability}")
    lable_ability.grid(row=5)

    lable_fireball =Label(window, text=f"fireball: {fireball}")
    lable_fireball.grid(row=6, column=1)

    lable_treatmen =Label(window, text=f"treatmen: {treatmen}")
    lable_treatmen.grid(row=6, column=2)

    lable_invisibility =Label(window, text=f"invisibility: {invisibility}")
    lable_invisibility.grid(row=6,column=3)

    lable_hacking =Label(window, text=f"hacking: {hacking}")
    lable_hacking.grid(row=6,column=4)

    sword_label =Label(window, text=f"sword: {sword}")
    sword_label.grid(row=7,column=1)

    lable_onion =Label(window, text=f"onion: {onion}")
    lable_onion.grid(row=7,column=2)

    lable_stick =Label(window, text=f"stick: {stick}")
    lable_stick.grid(row=7,column=3)

    lable_dagger =Label(window, text=f"dagger:{dagger}")
    lable_dagger.grid(row=7,column=4)


    win = Toplevel() 
    win.title("Профиль")
    win.geometry("400x400")
    win.resizable(False, False)

    content_1=Frame(Toplevel)

    name_entry=ttk.Entry(content_1)
    name_entry.grid(row=1)

    info=["Воин","Маг","Лучник","Вор"]
    class_pers_combo= ttk.Combobox(content_1, values=info) 
    class_pers_combo.grid(row=2)

    info_2=["Человек","Эльф","Орк","Гном"]
    race_combo=ttk.Combobox(content_1, values=info_2)
    race_combo.grid(row=3)

    level_scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=50.0, value=30)
    level_scale.grid(row=4)

    ability_entry=ttk.Entry(content_1)
    ability_entry.grid(row=5)

    fireball = IntVar()
    fireball_check=ttk.Checkbutton(content_1,text="Огненый шар",variable=fireball)
    fireball_check.grid(pady=5,padx=40,row=6,column=1)

    treatment = IntVar()
    treatment_check=ttk.Checkbutton(content_1,text="Лечение",variable=treatment)
    treatment_check.grid(pady=5,padx=40,row=6,column=2)

    invisibility = IntVar()
    invisibility_check=ttk.Checkbutton(content_1,text="Невидимость",variable=invisibility)
    invisibility_check.grid(pady=5,padx=40,row=6,column=3)

    hacking = IntVar()
    hacking_check=ttk.Checkbutton(content_1,text="Взлом",variable=hacking)
    hacking_check.grid(pady=5,padx=40,row=6,column=4)

    sword = StringVar(value="Меч")
    sword_radio=ttk.Radiobutton(content_1,text="",value="Меч", variable=sword)
    sword_radio.grid(row=6,column= 1)

    onion_radio=ttk.Radiobutton(content_1,value="Лук", variable=sword,text="Лук")
    onion_radio.grid(row=6,column=2)

    stick_radio=ttk.Radiobutton(content_1,value="Посох", variable=sword,text="Посох")
    stick_radio.grid(row=6,column=3)

    dagger_radio=ttk.Radiobutton(content_1,value="Кинжал", variable=sword,text="Кинжал")
    dagger_radio.grid(row=6,column=4)

    bth=Button(content_1,text="GO",command=go)
    bth.grid(row=7)

    content_1.pack()
    

#главное окно

root = Tk()
root.title("pers")
root.geometry("450x315")
root.resizable(False, False)

content = Frame(root)
content.pack(fill="x")

label_name = ttk.Label(content, text="Welcome", font=("Arial", 20))
label_name.pack(pady=3)

label_description = ttk.Label(content, text="Start creating a character!", font=("Arial", 10))
label_description.pack(pady=5)

bth_go=Button(content,bg="red",text="Go", width=20, height=5,command=creature)
bth_go.pack(pady=10)

content.pack()

root.mainloop()