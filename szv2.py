import io
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from datetime import datetime
from datetime import date
from  time import  strftime
from tkinter.messagebox import showerror, showinfo
from tkinter.scrolledtext import ScrolledText
from turtle import bgcolor
from PIL import Image, ImageTk
from datetime import timedelta
import gc


root = Tk()
root.title("Контроль")
root.geometry("1920x1080")
root.state('normal')
root.attributes('-fullscreen', True)
root.configure(bg='#f0f0f0')

style = ttk.Style(root)
navi_btn_s = ttk.Style()
navi_btn_s.configure('my.TButton', font=('Helvetica', 30))
frame_style = ttk.Style(root)
style.configure('TFrame', background='#f0f0f0', bordercolor="#f0f0f0")

lbl_style = ttk.Style(root)
style.configure('TLabel', background='#f0f0f0', bordercolor="#f0f0f0", borderwidth=0, highlightthickness=0)

frame_0 = ttk.Frame(width=1920, height=1080) #Фрейм главного окна
frame_1 = ttk.Frame(width=1920, height=1080) #Фрейм с выбором изделия наконечники
frame_11 = ttk.Frame(width=1920, height=1080) #Фрейм с выбором изделия соединители
frame_2 = ttk.Frame(width=1920, height=1080) #Фрейм с выбором станка наконечники
frame_22 = ttk.Frame(width=1920, height=1080) #Фрейм с выбором станка соединители
frame_3 = ttk.Frame(width=1920, height=1080) #Фрейм с фио и паролем наконечники
frame_33 = ttk.Frame(width=1920, height=1080) #Фрейм с фио и паролем соединители
frame_4 = ttk.Frame(width=1920, height=1080) #Фрейм с окном контроля наконечников
frame_44 = ttk.Frame(width=1920, height=1080) #Фрейм с окном контроля соединителей
frame_6 = ttk.Frame(width=1920, height=1080) #Фрейм с чертежами и эскизами
frame_7 = ttk.Frame(width=1920, height=1080) #Фрейм с внесенными данными наконечников
frame_77 = ttk.Frame(width=1920, height=1080) #Фрейм с внесенными данными соединителей

zeta_img = Image.open('zeta_logo.PNG')
zeta_render = ImageTk.PhotoImage(zeta_img)
blueprint_pic = Image.open("blueprint.PNG")
blueprint_render = ImageTk.PhotoImage(blueprint_pic)
con_pic = Image.open("connector_2.PNG")
con_render = ImageTk.PhotoImage(con_pic)
lug_pic = Image.open("navilug_1.PNG")
lug_render = ImageTk.PhotoImage(lug_pic)
room_img = Image.open("transfScheme_1.PNG")
room_img_rnd = ImageTk.PhotoImage(room_img)
vlug_img = Image.open("v-lug.PNG")
vlug_img_rnd = ImageTk.PhotoImage(vlug_img)  
lug_img = Image.open("lug_1.PNG")
lug_img_rnd = ImageTk.PhotoImage(lug_img)
lugo_img = Image.open("lugo_1.PNG")
lugo_img_rnd = ImageTk.PhotoImage(lugo_img)
stang_img = Image.open("stang_1.PNG")
stang_rnd = ImageTk.PhotoImage(stang_img)
con_img = Image.open("connect_1.PNG")
con_img_rnd = ImageTk.PhotoImage(con_img)
vcon_img = Image.open("v-connect_1.PNG")
vcon_img_rnd = ImageTk.PhotoImage(vcon_img)
scon_img = Image.open("connect_sbrs.PNG")
scon_img_rnd = ImageTk.PhotoImage(scon_img)
ocon_img = Image.open("connecto_1.PNG")
ocon_img_rnd = ImageTk.PhotoImage(ocon_img)

cons_img = Image.open("cons_blueprint_1.PNG")
cons_img_rnd = ImageTk.PhotoImage(cons_img)
lugl_img = Image.open("lug_blueprint_1.PNG")
lugl_img_rnd = ImageTk.PhotoImage(lugl_img)
luglo_img = Image.open("luglo_blueprint_1.PNG")
luglo_img_rnd = ImageTk.PhotoImage(luglo_img)
lugv_img = Image.open("lugv_blueprint_1.PNG")
lugv_img_rnd = ImageTk.PhotoImage(lugv_img)
conl_img = Image.open("conl_blueprint_1.PNG")
conl_img_rnd = ImageTk.PhotoImage(conl_img)
conltr_img = Image.open("conltr_blueprint_1.PNG")
conltr_img_rnd = ImageTk.PhotoImage(conltr_img) 
conlo_img = Image.open("conlo_blueprint_1.PNG")
conlo_img_rnd = ImageTk.PhotoImage(conlo_img)
conv_img = Image.open("conv_blueprint_1.PNG")
conv_img_rnd = ImageTk.PhotoImage(conv_img)


def navi_frame():
    global zeta_render, blueprint_render, con_render, lug_render
    for widget in frame_0.winfo_children():
        widget.destroy()
    zeta_logo = Label(frame_0, image=zeta_render, background='#f0f0f0')
    zeta_logo.image = zeta_render
    zeta_logo.place(anchor='nw',x=50, y=10)
    title = Label(frame_0, text="ПРОГРАММА КОНТРОЛЯ КОРПУСОВ БОЛТОВЫХ", font='Magistral 40 bold', foreground='#17417b', wraplength=1000, justify='center', background='#f0f0f0')
    title.place(anchor='nw',x=850, y=25)
    btn_blueprint_init = ttk.Button(frame_0, text="Просмотр чертежей", image=blueprint_render, command=lambda: (main_to_blueprint()))
    btn_blueprint_init.image=blueprint_render
    btn_blueprint_init.place(anchor="center", x=250, y=600)
    btn_lug_init = ttk.Button(frame_0, text="Контроль наконечников", image=lug_render, command=lambda: (part_list_query(parttype='lug')))
    btn_lug_init.image = lug_render
    btn_lug_init.place(anchor="center", x=795, y=600)
    btn_con_init = ttk.Button(frame_0, text="Контроль соединителей", image=con_render, command=lambda: (part_list_query(parttype='con')))
    btn_con_init.image=con_render
    btn_con_init.place(anchor="center", x=1500, y=600)
    navi_lbl_blueprint = ttk.Label(frame_0, text='Просмотр чертежей', font='Magistral 30')
    navi_lbl_blueprint.place(anchor='center', x=250, y=260)
    navi_lbl_lug = ttk.Label(frame_0, text='Контроль наконечников', font='Magistral 30')
    navi_lbl_lug.place(anchor='center', x=795, y=260)
    navi_lbl_con = ttk.Label(frame_0, text='Контроль соединителей', font='Magistral 30', wraplength=600, justify='center')
    navi_lbl_con.place(anchor='center', x=1500, y=260)
    time_label = Label(frame_0, font=('Magistral', 30), background='#f0f0f0', foreground='black')
    btn_tab_lug = ttk.Button(frame_0, text="Записи наконечники", style='my.TButton', command=lambda: main_to_tab(dt=timebox.get(), parttype='lug'))
    btn_tab_lug.place(anchor="nw", x=500, y=875)
    btn_tab_con = ttk.Button(frame_0, text="Записи соединители", style='my.TButton', command=lambda: main_to_tab(dt=timebox.get(), parttype='con'))
    btn_tab_con.place(anchor="nw", x=65, y=875)
    def time():
        string = strftime('%H:%M')
        time_label.config(text=string)
        time_label.after(1000, time)
    time_label.place(anchor='nw', x=65, y=170)
    time()   
    date_today = date.today()
    date_yesterday = date_today-timedelta(days=1)
    date_2daysb4 = date_today-timedelta(days=2)
    date_3daysb4 = date_today-timedelta(days=3)
    datesbox=(date_today, date_yesterday, date_2daysb4, date_3daysb4)
    timebox = ttk.Combobox(frame_0, values=datesbox, state='readonly', font='Helvetica 30', width=11)
    timebox.current(0)
    timebox.place(anchor="nw", x=920, y=878)


frame_0.place(x=0, y=0)
navi_frame()


def part_list_query(parttype):
    match parttype:
        case 'lug':
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                sql_fetch_blob_query = """SELECT part_name FROM lugs_max_min"""
                cursor.execute(sql_fetch_blob_query)
                parts_tuple = cursor.fetchall()
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                to_partlist(parttype='lug', parts_tuple=parts_tuple)
        case 'con':
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                sql_fetch_blob_query = """SELECT part_name FROM connectors_max_min"""
                cursor.execute(sql_fetch_blob_query)
                parts_tuple = cursor.fetchall()
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                to_partlist(parttype='con', parts_tuple=parts_tuple)

    
def to_partlist(parttype, parts_tuple):
    for widget in frame_1.winfo_children():
        widget.destroy()
    for widget in frame_11.winfo_children():
        widget.destroy()
    match parttype:
        case 'lug':
            frame_0.place_forget()
            frame_11.place(x=0, y=0)
            partlist = ttk.Combobox(frame_11, values=parts_tuple,
                                    font='Helvetica 30',
                                    width=12,
                                    state='readonly')
            partlist.current(1)
            partlist.place(anchor="nw", x=900, y=10)
            btn_partlist_to_main = ttk.Button(frame_11, text="Назад",
                                              style="my.TButton",
                                              width=6,
                                              command=lambda: partlist_to_main(),
                                              )
            btn_partlist_to_main.place(anchor="nw", x=10, y=10)
            btn_part_to_mach = ttk.Button(frame_11, text='Далее',
                                          style="my.TButton",
                                          width=8,
                                          command=lambda: part_to_mach(parttype='lug',
                                                                       part_name=partlist.get()))
            btn_part_to_mach.place(anchor="ne", x=1905, y=10)
            instr_partlist = Label(frame_11, text='Выберите изделие для контроля:', font='Helvetica 30', background='#f0f0f0')
            instr_partlist.place(anchor='nw', x=250, y=10)
        case 'con':
            frame_0.place_forget()
            frame_1.place(x=0, y=0)
            
            partlist = ttk.Combobox(frame_1, values=parts_tuple,
                                    font='Helvetica 30',
                                    state='readonly',
                                    width=12)
            partlist.current(7)
            partlist.place(anchor="nw", x=900, y=10)
            btn_partlist_to_main = ttk.Button(frame_1, text="Назад",
                                              style="my.TButton",
                                              width=6,
                                              command=lambda: partlist_to_main())
            btn_partlist_to_main.place(anchor="nw", x=10, y=10)
            btn_part_to_mach = ttk.Button(frame_1, text='Далее',
                                          style="my.TButton",
                                          width=8,
                                          command=lambda: part_to_mach(parttype='con',
                                                                       part_name=partlist.get()))
            btn_part_to_mach.place(anchor="ne", x=1905, y=10)
            instr_partlist = Label(frame_1, text='Выберите изделие для контроля:', font='Helvetica 30', background='#f0f0f0')
            instr_partlist.place(anchor='nw', x=250, y=10)


def partlist_to_main():
    frame_1.place_forget()
    frame_11.place_forget()
    frame_0.place(x=0, y=0)
    navi_frame()

    
def part_to_mach(parttype, part_name):
    global room_img_rnd
    for widget in frame_2.winfo_children():
        widget.destroy()
    for widget in frame_22.winfo_children():
        widget.destroy()
    match parttype:
        case 'lug':
            frame_11.place_forget()
            frame_22.place(x=0, y=0)     
            canvas_lug = Canvas(frame_22, width=1920, height=1080, background='#f0f0f0')
            canvas_lug.background = room_img_rnd  # Keep a reference in case this code is put in a function.
            canvas_lug.create_image(0, 192, anchor=NW, image=room_img_rnd)
            canvas_lug.place(x=0, y=0)
            btn_mach_to_fio = [f"btn_mach_to_fio_{i}" for i in range(9)]
            for i in range(3):
                btn_mach_to_fio[i] = Button(canvas_lug, text=f"{i+1}", 
                                                command=lambda i=i+1: fio_query(parttype='lug', part_name=part_name, mach=i))
                btn_mach_to_fio[0]['height']='7'
                btn_mach_to_fio[0]['width']='9'
                btn_mach_to_fio[0]['text']=f'{1}'
                btn_mach_to_fio[0]['font']='Times 20'
                btn_mach_to_fio[0].place(anchor="nw", x=455, y=350)
            for i in range(1,3,1):
                btn_mach_to_fio[i]['height']='5'
                btn_mach_to_fio[i]['width']='8'
                btn_mach_to_fio[i]['text']=f'{i+1}'
                btn_mach_to_fio[i]['font']='Times 20'
                btn_mach_to_fio[1].place(anchor="nw", x=903, y=400)
                btn_mach_to_fio[2].place(anchor="nw", x=1346, y=400)
            btn_mach_to_part = ttk.Button(canvas_lug,
                                          text="Назад",
                                          width=6,
                                          style="my.TButton",
                                          command=lambda: mach_to_part(parttype='lug'))
            btn_mach_to_part.place(anchor="nw", x=10, y=10)
            instr_partlist = Label(canvas_lug, text='Выберите станок схеме и щелкните на него', font='Helvetica 30', background='#f0f0f0')
            instr_partlist.place(anchor='nw', x=500, y=10)            
        case 'con':
            frame_1.place_forget()
            frame_2.place(x=0, y=0)           
            canvas_con = Canvas(frame_2, width=1920, height=1080, background='#f0f0f0')
            canvas_con.background = room_img_rnd  # Keep a reference in case this code is put in a function.
            canvas_con.create_image(0, 192, anchor=NW, image=room_img_rnd)
            canvas_con.place(x=0, y=0)
            btn_mach_to_fio = [f"btn_mach_to_fio_{i}" for i in range(9)]
            for i in range(3):
                btn_mach_to_fio[i] = Button(canvas_con, text=f"{i+1}", 
                                                command=lambda i=i+1: fio_query(parttype='con', part_name=part_name, mach=i))
                btn_mach_to_fio[0]['height']='7'
                btn_mach_to_fio[0]['width']='9'
                btn_mach_to_fio[0]['text']=f'{1}'
                btn_mach_to_fio[0]['font']='Times 20'
                btn_mach_to_fio[0].place(anchor="nw", x=455, y=350)
            for i in range(1,3,1):
                btn_mach_to_fio[i]['height']='5'
                btn_mach_to_fio[i]['width']='8'
                btn_mach_to_fio[i]['text']=f'{i+1}'
                btn_mach_to_fio[i]['font']='Times 20'
                btn_mach_to_fio[1].place(anchor="nw", x=903, y=400)
                btn_mach_to_fio[2].place(anchor="nw", x=1346, y=400)
            btn_mach_to_part = ttk.Button(canvas_con, text="Назад",
                                          width=6,
                                          style="my.TButton",
                                          command=lambda: mach_to_part(parttype='con'))
            btn_mach_to_part.place(anchor="nw", x=10, y=10)          
            instr_partlist = Label(canvas_con, text='Выберите станок и щелкните на него на схеме', font='Helvetica 30', background='#f0f0f0')
            instr_partlist.place(anchor='nw', x=500, y=10)


def mach_to_part(parttype):
    match parttype:
        case 'lug':
            frame_11.place(x=0, y=0)
            frame_22.place_forget()
        case 'con':
            frame_1.place(x=0, y=0)
            frame_2.place_forget()


def fio_to_mach(parttype):
    match parttype:
        case 'lug':
            frame_22.place(x=0, y=0)
            frame_33.place_forget()
        case 'con':
            frame_2.place(x=0, y=0)
            frame_3.place_forget()


def fio_query(parttype, part_name, mach):
    try:
        sqlite_connection = sqlite3.connect('main.db')
        cursor = sqlite_connection.cursor()
        sql_fetch_blob_query = """SELECT Surname FROM Fios"""
        cursor.execute(sql_fetch_blob_query)
        names_tuple = cursor.fetchall()
        cursor.close()
        match parttype:
            case 'lug':
               mach_to_fio(parttype='lug', part_name=part_name, mach=mach, names_tuple=names_tuple) 
            case 'con':
                mach_to_fio(parttype='con', part_name=part_name, mach=mach, names_tuple=names_tuple)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
             sqlite_connection.close()


def mach_to_fio(parttype, part_name, mach, names_tuple):
    for widget in frame_33.winfo_children():
        widget.destroy()
    for widget in frame_3.winfo_children():
        widget.destroy()
    match parttype:
        case 'lug':
            frame_33.place(x=0, y=0)
            surname = ttk.Combobox(frame_33, values=names_tuple, font='Helvetica 30', state='readonly', width=15)
            surname.current(0)
            surname.place(anchor='nw', x=520, y=10)
            def validate_input(text):
                if text.isdigit():
                    return True
                elif text == "":
                    return True
                else:
                    return False
            vcmd = (root.register(validate_input), '%P')
            password = ttk.Entry(frame_33, show='*',font='Helvetica 30',
                                 justify='center', width='6', validate='key', validatecommand=vcmd)
            password.place(anchor='nw', x=1100, y=15)
            btn_fio_to_meas = ttk.Button(frame_33, 
                                         text="Далее", 
                                         style='my.TButton',
                                         width=8,
                                         command=lambda: authentification(parttype='lug',
                                                                          part_name=part_name,
                                                                          mach=mach,
                                                                          surname=surname.get(),
                                                                          password=password.get()))
            btn_fio_to_meas.place(anchor="ne", x=1905, y=10)
            btn_fio_to_mach = ttk.Button(frame_33, text="Назад",
                                         style='my.TButton',
                                         width=6,
                                         command=lambda: fio_to_mach(parttype))
            btn_fio_to_mach.place(anchor="nw", x=10, y=10)
            frame_22.place_forget()
            print(f"Вы выбрали: Станок {parttype} под номером {mach}, болт {part_name}")                       
            instr_partlist_1 = Label(frame_33, text='Ваша фамилия:', font='Helvetica 30', background='#f0f0f0')
            instr_partlist_1.place(anchor='nw', x=200, y=15)  
            instr_partlist_2 = Label(frame_33, text='Пароль:', font='Helvetica 30', background='#f0f0f0')
            instr_partlist_2.place(anchor='nw', x=900, y=15)  
        case 'con':
            frame_3.place(x=0, y=0)
            surname = ttk.Combobox(frame_3,
                                   values=names_tuple,
                                   state='readonly',
                                   font='Helvetica 30',
                                   width=15)
            surname.current(0)
            surname.place(anchor='nw', x=520, y=15)
            def validate_input(text):
                if text.isdigit():
                    return True
                elif text == "":
                    return True
                else:
                    return False
            vcmd = (root.register(validate_input), '%P')
            password = ttk.Entry(frame_3,
                                 show='*',
                                 validate='key',
                                validatecommand=vcmd,
                                font='Helvetica 30',
                                width=6, justify='center')
            password.place(anchor='nw', x=1100, y=15)
            btn_fio_to_meas = ttk.Button(frame_3, text="Далее", 
                                         style='my.TButton',
                                         width=8,
                                         command=lambda: authentification(parttype='con',
                                                                                                  part_name=part_name,
                                                                                                  mach=mach,
                                                                                                  surname=surname.get(),
                                                                                                  password=password.get()))
            btn_fio_to_meas.place(anchor="ne", x=1905, y=10)
            btn_fio_to_mach = ttk.Button(frame_3, text="Назад",
                                         style='my.TButton',
                                         width=6,
                                         command=lambda: fio_to_mach(parttype))
            btn_fio_to_mach.place(anchor="nw", x=10, y=10)
            frame_2.place_forget()
            instr_partlist_1 = Label(frame_3, text='Ваша фамилия:', font='Helvetica 30', background='#f0f0f0')
            instr_partlist_1.place(anchor='nw', x=200, y=15)  
            instr_partlist_2 = Label(frame_3, text='Пароль:', font='Helvetica 30', background='#f0f0f0')
            instr_partlist_2.place(anchor='nw', x=900, y=15)  


def authentification(parttype, part_name, mach, surname, password):
        if password == "":
            showerror(parent=root, title="Ошибка", message="Неверный пароль")
        elif not password.isdigit():
            showerror(parent=root, title="Ошибка", message="Неверный пароль")
        else:
            pass_entered = int(password)
            entry_tuple = (surname, pass_entered)
            print(entry_tuple)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")
                sql_fetch_blob_query = """SELECT Surname, Password, Status from Fios where Surname = ?"""
                cursor.execute(sql_fetch_blob_query, (surname, ))
                outro = cursor.fetchone()
                auth_tuple = (outro[0], outro[1])
                status = outro[2]
                cursor.close()
            except sqlite3.Error as error:
                pass
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                if entry_tuple==auth_tuple:
                    shape_init(parttype=parttype, part_name=part_name, mach=mach, surname=surname, status=status)
                else:
                    showerror(parent=root, title="Ошибка", message="Неверный пароль")

call_count=0


def shape_init(parttype, part_name, mach, surname, status):
    print(parttype, part_name, mach, surname, status)
    match parttype:
        case 'lug':
            try:    
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")
                sql_fetch_blob_query = """SELECT shape from lugs_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, ))
                shape = cursor.fetchone()
                cursor.close()
                print(shape)
            except sqlite3.Error as error:
                print('WRONG')
            finally:
                fio_to_meas(parttype=parttype, part_name=part_name, mach=mach, surname=surname, status=status, shape=shape[0])
        case 'con':
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                sql_fetch_blob_query = """SELECT shape from connectors_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, ))
                shape = cursor.fetchone()
                cursor.close()
                print(shape)
            except sqlite3.Error as error:
                print('WRONG')
            finally:
                fio_to_meas(parttype=parttype, part_name=part_name, mach=mach, surname=surname, status=status, shape=shape[0])




def fio_to_meas(parttype, part_name, mach, surname, status, shape):
    for widget in frame_4.winfo_children():
        widget.destroy()
    for widget in frame_44.winfo_children():
        widget.destroy()
    global stang_rnd
    match parttype:
        case 'lug':
            frame_44.place(x=0, y=0)
            match shape:
                case 'l':
                    global lug_img_rnd
                    canvas_lug = Canvas(frame_44, width=1920, height=1080, background='#f0f0f0')
                    canvas_lug.background = lug_img_rnd
                    canvas_lug.create_image(500, 100, anchor=NW, image=lug_img_rnd)
                    canvas_lug.place(x=0, y=0)
                    btn_fio_to_meas = ttk.Button(canvas_lug,
                                     style='my.TButton',
                                     text="В главное меню",
                                    command=lambda: meas_to_main(parttype='lug'))
                    btn_fio_to_meas.place(anchor="nw", x=10, y=10)
                    parameters_lug = ['d1', 'L', 'W', 'T', 'd2', 't', 'J', 'l2', 'l1', 'Dp31', 'Dp32', 'R1', 'R2', 'S', 'l4', 'B', 'D']
                    def validate_input(text):
                        if text.isdigit():
                            return True
                        elif text.count('.') == 1 and text.replace('.', '', 1).isdigit():
                            return True
                        elif text == "":
                            return True
                        else:
                            return False
                    vcmd = (root.register(validate_input), '%P')

                    entry_parameters_lug = [f"entry_parameters_six_{i}" for i in parameters_lug]
                    for i in range(17):
                        entry_parameters_lug[i] = Entry(canvas_lug, 
                                                        width=5, font='Magistral 20', 
                                                        justify='center', 
                                                        validate="key", 
                                                        validatecommand=vcmd)

                    entry_parameters_lug[0].place(x=645, y=710) #d1
                    entry_parameters_lug[1].place(x=645, y=940) #L
                    entry_parameters_lug[2].place(x=785, y=75) #W
                    entry_parameters_lug[3].place(x=785, y=158) #T
                    entry_parameters_lug[4].place(x=785, y=235) #d2
                    entry_parameters_lug[5].place(x=785, y=310) #t
                    entry_parameters_lug[6].place(x=785, y=435) #J
                    entry_parameters_lug[7].place(x=785, y=503) #l2
                    entry_parameters_lug[8].place(x=785, y=585) #l1
                    entry_parameters_lug[9].place(x=1000, y=860) #Dp31
                    entry_parameters_lug[10].place(x=1155, y=860) #Dp32
                    entry_parameters_lug[11].place(x=785, y=902) #R1
                    entry_parameters_lug[12].place(x=1660, y=170) #R2
                    entry_parameters_lug[13].place(x=1660, y=435) #S
                    entry_parameters_lug[14].place(x=1660, y=503) #l4
                    entry_parameters_lug[15].place(x=1660, y=710) #B
                    entry_parameters_lug[16].place(x=1660, y=860) #D
                    frame_33.place_forget()
                    btn_execute_lug = ttk.Button(canvas_lug, text="Проверить",
                                             style='my.TButton',
                                             width=9,
                                             command=lambda: get_sz_tuple(parttype=parttype, 
                                                                          part_name=part_name, 
                                                                          mach=mach, 
                                                                          surname=surname, 
                                                                          status=status,
                                                                          entry_sz=[entry.get() for entry in entry_parameters_lug],
                                                                          entry_parameters=entry_parameters_lug,
                                                                          btn_execute=btn_execute_lug,
                                                                          canvas=canvas_lug, shape=shape))
                    btn_execute_lug.place(anchor="ne", x=1905, y=10)
                    instr_meas_1 = Label(canvas_lug, text='Произведите замеры, затем запустите проверку', font='Helvetica 30', background='#f0f0f0')
                    instr_meas_1.place(anchor='nw', x=550, y=10)
                    instr_meas_2 = Label(canvas_lug, text='Порядок проведения контроля', font='Helvetica 24 underline', background='#f0f0f0')
                    instr_meas_2.place(anchor='nw', x=10, y=80)
                    instr_meas_3 = Label(canvas_lug, 
                                         text='1. Вынуть готовый корпус из челюстей станка. Обдуть корпус сжатым воздухом.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_3.place(anchor='nw', x=10, y=120)
                    instr_meas_4 = Label(canvas_lug, 
                                         text='2. Проверить геометрию резьб под болты: последовательно вкрутить в каждое из отверстий калибр проходной и непроходной стороной.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_4.place(anchor='nw', x=10, y=190)
                    instr_meas_5 = Label(canvas_lug, 
                                         text='3. Измерить корпус штангенциркулем согласно схеме, внести полученные размеры в поля ввода на экране. Размеры вводить без округления.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_5.place(anchor='nw', x=10, y=320)
                    instr_meas_6 = Label(canvas_lug, 
                                         text='наведите курсор на поле, нажмите левую кнопку мыши и введите размер d1.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_6.place(anchor='nw', x=10, y=670)
                    instr_meas_7 = Label(canvas_lug, 
                                         text='Повторное нажатие Enter переключит вас на следующий размер.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_7.place(anchor='nw', x=10, y=780)
                    
                    instr_meas_6 = Label(canvas_lug, image=stang_rnd, background='#f0f0f0')  
                    instr_meas_6.image=stang_rnd
                    instr_meas_6.place(anchor='nw', x=-5, y=450)
                case 'lo':
                    global lugo_img_rnd
                    canvas_lug = Canvas(frame_44, width=1920, height=1080, background='#f0f0f0')
                    canvas_lug.background = lugo_img_rnd
                    canvas_lug.create_image(500, 100, anchor=NW, image=lugo_img_rnd)
                    canvas_lug.place(x=0, y=0)
                    btn_fio_to_meas = ttk.Button(canvas_lug,
                                     style='my.TButton',
                                     text="В главное меню",
                                    command=lambda: meas_to_main(parttype='lug'))
                    btn_fio_to_meas.place(anchor="nw", x=10, y=10)
                    parameters_lug = ['d1', 'L', 'W', 'T', 'd2', 't', 'J', 'l2', 'l1', 'Dp31', 'Dp32', 'R1', 'R2', 'S', 'l4', 'B', 'D']
                    def validate_input(text):
                        if text.isdigit():
                            return True
                        elif text.count('.') == 1 and text.replace('.', '', 1).isdigit():
                            return True
                        elif text == "":
                            return True
                        else:
                            return False
                    vcmd = (root.register(validate_input), '%P')

                    entry_parameters_lug = [f"entry_parameters_six_{i}" for i in parameters_lug]
                    for i in range(17):
                        entry_parameters_lug[i] = Entry(canvas_lug, 
                                                        width=5, font='Magistral 20', 
                                                        justify='center', 
                                                        validate="key", 
                                                        validatecommand=vcmd)

                    entry_parameters_lug[0].place(x=645, y=710) #d1
                    entry_parameters_lug[1].place(x=645, y=940) #L
                    entry_parameters_lug[2].place(x=785, y=75) #W
                    entry_parameters_lug[3].place(x=785, y=158) #T
                    entry_parameters_lug[4].place(x=785, y=235) #d2
                    entry_parameters_lug[5].place(x=785, y=310) #t
                    entry_parameters_lug[6].place(x=785, y=435) #J
                    entry_parameters_lug[7].insert(0, 0)
                    entry_parameters_lug[8].place(x=785, y=585) #l1
                    entry_parameters_lug[9].place(x=1000, y=860) #Dp31
                    entry_parameters_lug[10].insert(0, 0)
                    entry_parameters_lug[11].place(x=785, y=902) #R1
                    entry_parameters_lug[12].place(x=1660, y=170) #R2
                    entry_parameters_lug[13].place(x=1660, y=435) #S
                    entry_parameters_lug[14].place(x=1660, y=503) #l4
                    entry_parameters_lug[15].place(x=1660, y=710) #B
                    entry_parameters_lug[16].place(x=1660, y=860) #D
                    frame_33.place_forget()
                    btn_execute_lug = ttk.Button(canvas_lug, text="Проверить",
                                             style='my.TButton',
                                             width=9,
                                             command=lambda: get_sz_tuple(parttype=parttype, 
                                                                          part_name=part_name, 
                                                                          mach=mach, 
                                                                          surname=surname, 
                                                                          status=status,
                                                                          entry_sz=[entry.get() for entry in entry_parameters_lug],
                                                                          entry_parameters=entry_parameters_lug,
                                                                          btn_execute=btn_execute_lug,
                                                                          canvas=canvas_lug, shape=shape))
                    btn_execute_lug.place(anchor="ne", x=1905, y=10)
                    instr_meas_1 = Label(canvas_lug, text='Произведите замеры, затем запустите проверку', font='Helvetica 30', background='#f0f0f0')
                    instr_meas_1.place(anchor='nw', x=550, y=10)
                    instr_meas_2 = Label(canvas_lug, text='Порядок проведения контроля', font='Helvetica 24 underline', background='#f0f0f0')
                    instr_meas_2.place(anchor='nw', x=10, y=80)
                    instr_meas_3 = Label(canvas_lug, 
                                         text='1. Вынуть готовый корпус из челюстей станка. Обдуть корпус сжатым воздухом.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_3.place(anchor='nw', x=10, y=120)
                    instr_meas_4 = Label(canvas_lug, 
                                         text='2. Проверить геометрию резьб под болты: последовательно вкрутить в каждое из отверстий калибр проходной и непроходной стороной.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_4.place(anchor='nw', x=10, y=190)
                    instr_meas_5 = Label(canvas_lug, 
                                         text='3. Измерить корпус штангенциркулем согласно схеме, внести полученные размеры в поля ввода на экране. Размеры вводить без округления.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_5.place(anchor='nw', x=10, y=320)
                    instr_meas_6 = Label(canvas_lug, 
                                         text='наведите курсор на поле, нажмите левую кнопку мыши и введите размер d1.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_6.place(anchor='nw', x=10, y=670)
                    instr_meas_7 = Label(canvas_lug, 
                                         text='Повторное нажатие Enter переключит вас на следующий размер.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_7.place(anchor='nw', x=10, y=780)
                    instr_meas_6 = Label(canvas_lug, image=stang_rnd, background='#f0f0f0')  
                    instr_meas_6.image=stang_rnd
                    instr_meas_6.place(anchor='nw', x=-5, y=450)

                case 'v':
                    global vlug_img_rnd
                    canvas_lug = Canvas(frame_44, width=1920, height=1080, background='#f0f0f0')
                    canvas_lug.background = vlug_img_rnd
                    canvas_lug.create_image(500, 100, anchor=NW, image=vlug_img_rnd)
                    canvas_lug.place(x=0, y=0)
                    btn_fio_to_meas = ttk.Button(canvas_lug,
                                             style='my.TButton',
                                             text="В главное меню",
                                            command=lambda: meas_to_main(parttype='lug'))
                    btn_fio_to_meas.place(anchor="nw", x=10, y=10)
                    parameters_lug = ['d1', 'L', 'W', 'T', 'd2', 't', 'J', 'l2', 'l1', 'Dp31', 'Dp32', 'R1', 'R2', 'S', 'l4', 'B', 'D']
                    def validate_input(text):
                        if text.isdigit():
                            return True
                        elif text.count('.') == 1 and text.replace('.', '', 1).isdigit():
                            return True
                        elif text == "":
                            return True
                        else:
                            return False
                    vcmd = (root.register(validate_input), '%P')

                    entry_parameters_lug = [f"entry_parameters_six_{i}" for i in parameters_lug]
                    for i in range(17):
                        entry_parameters_lug[i] = Entry(canvas_lug, 
                                                        width=5, font='Magistral 20', 
                                                        justify='center', 
                                                        validate="key", 
                                                        validatecommand=vcmd)

                    entry_parameters_lug[0].place(x=645, y=710) #d1
                    entry_parameters_lug[1].place(x=645, y=940) #L
                    entry_parameters_lug[2].place(x=785, y=75) #W
                    entry_parameters_lug[3].place(x=785, y=158) #T
                    entry_parameters_lug[4].place(x=785, y=235) #d2
                    entry_parameters_lug[5].place(x=785, y=310) #t
                    entry_parameters_lug[6].place(x=785, y=435) #J
                    entry_parameters_lug[7].place(x=785, y=503) #l2
                    entry_parameters_lug[8].place(x=785, y=585) #l1
                    entry_parameters_lug[9].place(x=1000, y=860) #Dp31
                    entry_parameters_lug[10].place(x=1155, y=860) #Dp32
                    entry_parameters_lug[11].place(x=785, y=902) #R1
                    entry_parameters_lug[12].place(x=1660, y=170) #R2
                    entry_parameters_lug[13].place(x=1660, y=435) #S
                    entry_parameters_lug[14].place(x=1660, y=503) #l4
                    entry_parameters_lug[15].place(x=1660, y=710) #B
                    entry_parameters_lug[16].place(x=1660, y=860) #D
                    frame_33.place_forget()
                    btn_execute_lug = ttk.Button(canvas_lug, text="Проверить",
                                             style='my.TButton',
                                             width=9,
                                             command=lambda: get_sz_tuple(parttype=parttype, 
                                                                          part_name=part_name, 
                                                                          mach=mach, 
                                                                          surname=surname, 
                                                                          status=status,
                                                                          entry_sz=[entry.get() for entry in entry_parameters_lug],
                                                                          entry_parameters=entry_parameters_lug,
                                                                          btn_execute=btn_execute_lug,
                                                                          canvas=canvas_lug, shape=shape))
                    btn_execute_lug.place(anchor="ne", x=1905, y=10)
                    instr_meas_1 = Label(canvas_lug, text='Произведите замеры, затем запустите проверку', font='Helvetica 30', background='#f0f0f0')
                    instr_meas_1.place(anchor='nw', x=550, y=10)
                    instr_meas_2 = Label(canvas_lug, text='Порядок проведения контроля', font='Helvetica 24 underline', background='#f0f0f0')
                    instr_meas_2.place(anchor='nw', x=10, y=80)
                    instr_meas_3 = Label(canvas_lug, 
                                         text='1. Вынуть готовый корпус из челюстей станка. Обдуть корпус сжатым воздухом.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_3.place(anchor='nw', x=10, y=120)
                    instr_meas_4 = Label(canvas_lug, 
                                         text='2. Проверить геометрию резьб под болты: последовательно вкрутить в каждое из отверстий калибр проходной и непроходной стороной.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_4.place(anchor='nw', x=10, y=190)
                    instr_meas_5 = Label(canvas_lug, 
                                         text='3. Измерить корпус штангенциркулем согласно схеме, внести полученные размеры в поля ввода на экране. Размеры вводить без округления.',
                                         wraplength=600,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_5.place(anchor='nw', x=10, y=320)
                    instr_meas_6 = Label(canvas_lug, 
                                         text='наведите курсор на поле, нажмите левую кнопку мыши и введите размер d1.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_6.place(anchor='nw', x=10, y=670)
                    instr_meas_7 = Label(canvas_lug, 
                                         text='Повторное нажатие Enter переключит вас на следующий размер.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_7.place(anchor='nw', x=10, y=780)
                    instr_meas_6 = Label(canvas_lug, image=stang_rnd, background='#f0f0f0')  
                    instr_meas_6.image=stang_rnd
                    instr_meas_6.place(anchor='nw', x=-5, y=450)
        case 'con':
            match shape:
                case 'l':
                    frame_4.place(x=0, y=0)
                    global con_img_rnd
                    canvas_con = Canvas(frame_4, width=1920, height=1080, background='#f0f0f0')
                    canvas_con.background = con_img_rnd
                    canvas_con.create_image(340, 99, anchor=NW, image=con_img_rnd)
                    canvas_con.place(x=0, y=0)
                    parameters_con = ['d1', 'L', 'W', 'T', 'd2','t', 'J', 'l1', 'l2', 'Dp3','R1',
                                      'W', 'T','d2', 't', 'J', 'l1',
                                      'l2', 'Dp3','R1']
                    def validate_input(text):
                        if text.isdigit():
                            return True
                        elif text.count('.') == 1 and text.replace('.', '', 1).isdigit():
                            return True
                        elif text == "":
                            return True
                        else:
                            return False
                    vcmd = (root.register(validate_input), '%P')
                    entry_parameters_con = [f"entry_parameters_six_{i}" for i in parameters_con]
                    for i in range(20):
                        entry_parameters_con[i] = Entry(canvas_con, width=6, font='Magistral 20', justify='center',
                                                        validate="key", 
                                                        validatecommand=vcmd)
                    entry_parameters_con[0].place(x=520, y=737) #d1
                    entry_parameters_con[1].place(x=520, y=938) #L
                    entry_parameters_con[2].place(x=645, y=75) #W
                    entry_parameters_con[3].place(x=645, y=182) #T
                    entry_parameters_con[4].place(x=645, y=267) #d2
                    entry_parameters_con[5].place(x=645, y=340) #t
                    entry_parameters_con[6].place(x=645, y=438) #J
                    entry_parameters_con[7].place(x=645, y=523) #l2
                    entry_parameters_con[8].place(x=645, y=613) #l1
                    entry_parameters_con[9].place(x=645, y=782) #Dp3
                    entry_parameters_con[10].place(x=645, y=889) #R1
                    entry_parameters_con[11].place(x=1610, y=75) #W  
                    entry_parameters_con[12].place(x=1610, y=182) #T
                    entry_parameters_con[13].place(x=1610, y=267) #d2
                    entry_parameters_con[14].place(x=1610, y=340) #t
                    entry_parameters_con[15].place(x=1610, y=438) #J
                    entry_parameters_con[16].place(x=1610, y=523) #l1
                    entry_parameters_con[17].place(x=1610, y=613) #l2
                    entry_parameters_con[18].place(x=1610, y=782) #Dp3
                    entry_parameters_con[19].place(x=1610, y=893) #R1

                    frame_3.place_forget()
                    btn_execute_con = ttk.Button(canvas_con, 
                                                 text="Проверить",
                                                style='my.TButton',
                                                width=9,
                                                command=lambda: get_sz_tuple(parttype=parttype, 
                                                                          part_name=part_name, 
                                                                          mach=mach, 
                                                                          surname=surname, 
                                                                          status=status,
                                                                          entry_sz=tuple(entry.get() for entry in entry_parameters_con),
                                                                          entry_parameters=entry_parameters_con,
                                                                          btn_execute=btn_execute_con,
                                                                          canvas=canvas_con, shape=shape))
                    btn_execute_con.place(anchor="ne", x=1905, y=10)
                    btn_meas_to_main = ttk.Button(canvas_con, text="В главное меню", 
                                                    style='my.TButton', command=lambda: meas_to_main(parttype='con'))
                    btn_meas_to_main.place(anchor="nw", x=10, y=10)
                    instr_meas_1 = Label(canvas_con, text='Произведите замеры, затем запустите проверку', font='Helvetica 30', background='#f0f0f0')
                    instr_meas_1.place(anchor='nw', x=550, y=10)
                    instr_meas_2 = Label(canvas_con, text='Порядок проведения контроля', font='Helvetica 24 underline', background='#f0f0f0')
                    instr_meas_2.place(anchor='nw', x=10, y=80)
                    instr_meas_3 = Label(canvas_con, 
                                         text='1. Вынуть готовый корпус из челюстей станка. Обдуть корпус сжатым воздухом.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_3.place(anchor='nw', x=10, y=120)
                    instr_meas_4 = Label(canvas_con, 
                                         text='2. Проверить геометрию резьб под болты: последовательно вкрутить в каждое из отверстий калибр проходной и непроходной стороной.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_4.place(anchor='nw', x=10, y=190)
                    instr_meas_5 = Label(canvas_con, 
                                         text='3. Измерить корпус штангенциркулем согласно схеме, внести полученные размеры в поля ввода на экране. Размеры вводить без округления.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_5.place(anchor='nw', x=10, y=320)
                    instr_meas_6 = Label(canvas_con, 
                                         text='наведите курсор на поле, нажмите левую кнопку мыши и введите размер d1.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_6.place(anchor='nw', x=10, y=670)
                    instr_meas_7 = Label(canvas_con, 
                                         text='Повторное нажатие Enter переключит вас на следующий размер.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_7.place(anchor='nw', x=10, y=780)
                    #global stang_rnd
                    instr_meas_6 = Label(canvas_con, image=stang_rnd, background='#f0f0f0')  
                    instr_meas_6.image=stang_rnd
                    instr_meas_6.place(anchor='nw', x=10, y=450)
                case 'v':
                    frame_4.place(x=0, y=0)
                    global vcon_img_rnd
                    canvas_con = Canvas(frame_4, width=1920, height=1080, background='#f0f0f0')
                    canvas_con.background = vcon_img_rnd  # Keep a reference in case this code is put in a function.
                    canvas_con.create_image(350, 98, anchor=NW, image=vcon_img_rnd)
                    canvas_con.place(x=0, y=0)
                    parameters_con = ['d1', 'L', 'W', 'T', 'd2','t', 'J', 'l1', 'l2', 'Dp3', 'R1',
                                        'W', 'T','d2', 't', 'J', 'l1',
                                         'l2', 'Dp3', 'R1']
                    def validate_input(text):
                        if text.isdigit():
                            return True
                        elif text.count('.') == 1 and text.replace('.', '', 1).isdigit():
                            return True
                        elif text == "":
                            return True
                        else:
                            return False
                    vcmd = (root.register(validate_input), '%P')
                    entry_parameters_con = [f"entry_parameters_six_{i}" for i in parameters_con]
                    for i in range(20):
                        entry_parameters_con[i] = Entry(canvas_con, width=6, font='Magistral 20', justify='center',
                                                        validate="key", 
                                                        validatecommand=vcmd)
                    entry_parameters_con[0].place(x=521, y=725) #d1
                    entry_parameters_con[1].place(x=521, y=938) #L
                    entry_parameters_con[2].place(x=642, y=77) #W
                    entry_parameters_con[3].place(x=642, y=180) #T
                    entry_parameters_con[4].place(x=642, y=264) #d2
                    entry_parameters_con[5].place(x=642, y=350) #t
                    entry_parameters_con[6].place(x=642, y=457) #J
                    entry_parameters_con[7].place(x=642, y=523) #l2
                    entry_parameters_con[8].place(x=642, y=604) #l1
                    entry_parameters_con[9].place(x=642, y=773) #Dp3
                    entry_parameters_con[10].place(x=642, y=896) #R1
                    entry_parameters_con[11].place(x=1630, y=77) #W  
                    entry_parameters_con[12].place(x=1630, y=180) #T
                    entry_parameters_con[13].place(x=1630, y=264) #d2
                    entry_parameters_con[14].place(x=1630, y=350) #t
                    entry_parameters_con[15].place(x=1630, y=457) #J
                    entry_parameters_con[16].place(x=1630, y=523) #l1
                    entry_parameters_con[17].place(x=1630, y=604) #l2
                    entry_parameters_con[18].place(x=1630, y=773) #Dp3
                    entry_parameters_con[19].place(x=1630, y=896) #R1

                    frame_3.place_forget()
                    btn_execute_con = ttk.Button(canvas_con, 
                                                 text="Проверить",
                                                style='my.TButton',
                                                width=9,
                                                command=lambda: get_sz_tuple(parttype=parttype, 
                                                                          part_name=part_name, 
                                                                          mach=mach, 
                                                                          surname=surname, 
                                                                          status=status,
                                                                          entry_sz=tuple(entry.get() for entry in entry_parameters_con),
                                                                          entry_parameters=entry_parameters_con,
                                                                          btn_execute=btn_execute_con,
                                                                          canvas=canvas_con, shape=shape))
                    btn_execute_con.place(anchor="ne", x=1905, y=10)
                    btn_meas_to_main = ttk.Button(canvas_con, text="В главное меню", 
                                                    style='my.TButton', command=lambda: meas_to_main(parttype='con'))
                    btn_meas_to_main.place(anchor="nw", x=10, y=10)
                    instr_meas_1 = Label(canvas_con, text='Произведите замеры, затем запустите проверку', font='Helvetica 30', background='#f0f0f0')
                    instr_meas_1.place(anchor='nw', x=550, y=10)
                    instr_meas_2 = Label(canvas_con, text='Порядок проведения контроля', font='Helvetica 24 underline', background='#f0f0f0')
                    instr_meas_2.place(anchor='nw', x=10, y=80)
                    instr_meas_3 = Label(canvas_con, 
                                         text='1. Вынуть готовый корпус из челюстей станка. Обдуть корпус сжатым воздухом.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_3.place(anchor='nw', x=10, y=120)
                    instr_meas_4 = Label(canvas_con, 
                                         text='2. Проверить геометрию резьб под болты: последовательно вкрутить в каждое из отверстий калибр проходной и непроходной стороной.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_4.place(anchor='nw', x=10, y=190)
                    instr_meas_5 = Label(canvas_con, 
                                         text='3. Измерить корпус штангенциркулем согласно схеме, внести полученные размеры в поля ввода на экране. Размеры вводить без округления.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_5.place(anchor='nw', x=10, y=320)
                    instr_meas_6 = Label(canvas_con, 
                                         text='Нажмите Enter и введите размер d1.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_6.place(anchor='nw', x=10, y=670)
                    instr_meas_7 = Label(canvas_con, 
                                         text='Повторное нажатие Enter переключит вас на следующий размер.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_7.place(anchor='nw', x=10, y=770)
                    #global stang_rnd
                    instr_meas_6 = Label(canvas_con, image=stang_rnd, background='#f0f0f0')  
                    instr_meas_6.image=stang_rnd
                    instr_meas_6.place(anchor='nw', x=10, y=450)
                case 's':
                    frame_4.place(x=0, y=0)
                    global scon_img_rnd      
                    canvas_con = Canvas(frame_4, width=1920, height=1080, background='#f0f0f0')
                    canvas_con.background = scon_img_rnd
                    canvas_con.create_image(400, 120, anchor=NW, image=scon_img_rnd)
                    canvas_con.place(x=0, y=0)
                    parameters_con = ['d1', 'W', 'T', 'd2','t', 'J', 'l1', 'l2', 'Dp3','R1']
                    def validate_input(text):
                        if text.isdigit():
                            return True
                        elif text.count('.') == 1 and text.replace('.', '', 1).isdigit():
                            return True
                        elif text == "":
                            return True
                        else:
                            return False
                    vcmd = (root.register(validate_input), '%P')
                    entry_parameters_con = [f"entry_parameters_six_{i}" for i in parameters_con]
                    for i in range(10):
                        entry_parameters_con[i] = Entry(canvas_con, width=6, font='Magistral 20', justify='center',
                                                        validate="key", 
                                                        validatecommand=vcmd)
                    entry_parameters_con[0].place(x=560, y=795) #d1
                    entry_parameters_con[1].place(x=1590, y=95) #W  
                    entry_parameters_con[2].place(x=1590, y=270) #T
                    entry_parameters_con[3].place(x=1590, y=355) #d2
                    entry_parameters_con[4].place(x=1590, y=425) #t
                    entry_parameters_con[5].place(x=1590, y=515) #J
                    entry_parameters_con[6].place(x=1590, y=595) #l2
                    entry_parameters_con[7].place(x=1590, y=680) #l1
                    entry_parameters_con[8].place(x=1590, y=840) #Dp3
                    entry_parameters_con[9].place(x=1590, y=960) #R1
                    frame_3.place_forget()
                    btn_execute_con = ttk.Button(canvas_con, 
                                                 text="Проверить",
                                                style='my.TButton',
                                                width=9,
                                                command=lambda: get_sz_tuple(parttype=parttype, 
                                                                          part_name=part_name, 
                                                                          mach=mach, 
                                                                          surname=surname, 
                                                                          status=status,
                                                                          entry_sz=tuple(entry.get() for entry in entry_parameters_con),
                                                                          entry_parameters=entry_parameters_con,
                                                                          btn_execute=btn_execute_con,
                                                                          canvas=canvas_con, shape=shape))
                    btn_execute_con.place(anchor="ne", x=1905, y=10)
                    btn_meas_to_main = ttk.Button(canvas_con, text="В главное меню", 
                                                    style='my.TButton', command=lambda: meas_to_main(parttype='con'))
                    btn_meas_to_main.place(anchor="nw", x=10, y=10)
                    instr_meas_1 = Label(canvas_con, text='Произведите замеры, затем запустите проверку', font='Helvetica 30', background='#f0f0f0')
                    instr_meas_1.place(anchor='nw', x=550, y=10)
                    instr_meas_2 = Label(canvas_con, text='Порядок проведения контроля', font='Helvetica 24 underline', background='#f0f0f0')
                    instr_meas_2.place(anchor='nw', x=10, y=80)
                    instr_meas_3 = Label(canvas_con, 
                                         text='1. Вынуть готовый корпус из челюстей станка. Обдуть корпус сжатым воздухом.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_3.place(anchor='nw', x=10, y=120)
                    instr_meas_4 = Label(canvas_con, 
                                         text='2. Проверить геометрию резьб под болты: последовательно вкрутить в каждое из отверстий калибр проходной и непроходной стороной.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_4.place(anchor='nw', x=10, y=190)
                    instr_meas_5 = Label(canvas_con, 
                                         text='3. Измерить корпус штангенциркулем согласно схеме, внести полученные размеры в поля ввода на экране. Размеры вводить без округления.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_5.place(anchor='nw', x=10, y=320)
                    instr_meas_6 = Label(canvas_con, 
                                         text='наведите курсор на поле, нажмите левую кнопку мыши и введите размер d1.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_6.place(anchor='nw', x=10, y=670)
                    instr_meas_7 = Label(canvas_con, 
                                         text='Повторное нажатие Enter переключит вас на следующий размер.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_7.place(anchor='nw', x=10, y=750)
                    #global stang_rnd
                    instr_meas_6 = Label(canvas_con, image=stang_rnd, background='#f0f0f0')  
                    instr_meas_6.image=stang_rnd
                    instr_meas_6.place(anchor='nw', x=10, y=450)

                case 'lo':
                    frame_4.place(x=0, y=0)
                    global ocon_img_rnd      
                    canvas_con = Canvas(frame_4, width=1920, height=1080, background='#f0f0f0')
                    canvas_con.background = ocon_img_rnd
                    canvas_con.create_image(340, 99, anchor=NW, image=ocon_img_rnd)
                    canvas_con.place(x=0, y=0)
                    parameters_con = ['d1', 'L', 'W', 'T', 'd2','t', 'J', 'l1', 'l2', 'Dp3', 'R1',
                                        'W', 'T','d2', 't', 'J', 'l1',
                                         'l2', 'Dp3', 'R1']
                    def validate_input(text):
                        if text.isdigit():
                            return True
                        elif text.count('.') == 1 and text.replace('.', '', 1).isdigit():
                            return True
                        elif text == "":
                            return True
                        else:
                            return False
                    vcmd = (root.register(validate_input), '%P')
                    entry_parameters_con = [f"entry_parameters_six_{i}" for i in parameters_con]
                    for i in range(20):
                        entry_parameters_con[i] = Entry(canvas_con, width=6, font='Magistral 20', justify='center',
                                                        validate="key", 
                                                        validatecommand=vcmd)
                    entry_parameters_con[0].place(x=520, y=737) #d1
                    entry_parameters_con[1].place(x=520, y=938) #L
                    entry_parameters_con[2].place(x=645, y=75) #W
                    entry_parameters_con[3].place(x=645, y=182) #T
                    entry_parameters_con[4].place(x=645, y=267) #d2
                    entry_parameters_con[5].place(x=645, y=340) #t
                    entry_parameters_con[6].place(x=645, y=438) #J
                    entry_parameters_con[7].insert(0,0) #l2
                    entry_parameters_con[8].place(x=645, y=613) #l1
                    entry_parameters_con[9].place(x=645, y=782) #Dp3
                    entry_parameters_con[10].place(x=645, y=889) #R1
                    entry_parameters_con[11].place(x=1610, y=75) #W  
                    entry_parameters_con[12].place(x=1610, y=182) #T
                    entry_parameters_con[13].place(x=1610, y=267) #d2
                    entry_parameters_con[14].place(x=1610, y=340) #t
                    entry_parameters_con[15].place(x=1610, y=438) #J
                    entry_parameters_con[16].insert(0,0) #l2
                    entry_parameters_con[17].place(x=1610, y=613) #l1
                    entry_parameters_con[18].place(x=1610, y=782) #Dp3
                    entry_parameters_con[19].place(x=1610, y=893) #R1
                    frame_3.place_forget()
                    btn_execute_con = ttk.Button(canvas_con, 
                                                 text="Проверить",
                                                style='my.TButton',
                                                width=9,
                                                command=lambda: get_sz_tuple(parttype=parttype, 
                                                                          part_name=part_name, 
                                                                          mach=mach, 
                                                                          surname=surname, 
                                                                          status=status,
                                                                          entry_sz=tuple(entry.get() for entry in entry_parameters_con),
                                                                          entry_parameters=entry_parameters_con,
                                                                          btn_execute=btn_execute_con,
                                                                          canvas=canvas_con, shape=shape))
                    btn_execute_con.place(anchor="ne", x=1905, y=10)
                    btn_meas_to_main = ttk.Button(canvas_con, text="В главное меню", 
                                                    style='my.TButton', command=lambda: meas_to_main(parttype='con'))
                    btn_meas_to_main.place(anchor="nw", x=10, y=10)
                    instr_meas_1 = Label(canvas_con, text='Произведите замеры, затем запустите проверку', font='Helvetica 30', background='#f0f0f0')
                    instr_meas_1.place(anchor='nw', x=550, y=10)
                    instr_meas_2 = Label(canvas_con, text='Порядок проведения контроля', font='Helvetica 24 underline', background='#f0f0f0')
                    instr_meas_2.place(anchor='nw', x=10, y=80)
                    instr_meas_3 = Label(canvas_con, 
                                         text='1. Вынуть готовый корпус из челюстей станка. Обдуть корпус сжатым воздухом.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_3.place(anchor='nw', x=10, y=120)
                    instr_meas_4 = Label(canvas_con, 
                                         text='2. Проверить геометрию резьб под болты: последовательно вкрутить в каждое из отверстий калибр проходной и непроходной стороной.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_4.place(anchor='nw', x=10, y=190)
                    instr_meas_5 = Label(canvas_con, 
                                         text='3. Измерить корпус штангенциркулем согласно схеме, внести полученные размеры в поля ввода на экране. Размеры вводить без округления.',
                                         wraplength=622,
                                         justify='left',
                                         font='Helvetica 20', background='#f0f0f0')
                    instr_meas_5.place(anchor='nw', x=10, y=320)
                    instr_meas_6 = Label(canvas_con, 
                                         text='наведите курсор на поле, нажмите левую кнопку мыши и введите размер d1.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_6.place(anchor='nw', x=10, y=670)
                    instr_meas_7 = Label(canvas_con, 
                                         text='Повторное нажатие Enter переключит вас на следующий размер.',
                                         wraplength=500,
                                         justify='left',
                                         font='Helvetica 18', background='#f0f0f0')
                    instr_meas_7.place(anchor='nw', x=10, y=780)
                    instr_meas_6 = Label(canvas_con, image=stang_rnd, background='#f0f0f0')  
                    instr_meas_6.image=stang_rnd
                    instr_meas_6.place(anchor='nw', x=10, y=450)


def get_sz_tuple(parttype, part_name, mach, surname, status, entry_sz, entry_parameters, btn_execute, canvas, shape):
    match parttype:
        case 'lug':
            if '' not in entry_sz:
                entry_sz_fl = list(map(float, entry_sz))
                size_check(parttype=parttype, 
                           part_name=part_name,
                           mach=mach, 
                           surname=surname, 
                           status=status, 
                           entry_sz_fl=entry_sz_fl,
                           entry_parameters=entry_parameters,
                           btn_execute=btn_execute,
                           canvas=canvas, shape=shape)
            else:
                showerror(parent=root, title="Ошибка", message="Все поля должны быть заполнены!")        
        case 'con':
            if '' not in entry_sz:
                entry_sz_fl = list(map(float, entry_sz))
                size_check(parttype=parttype,
                           part_name=part_name,
                           mach=mach, surname=surname,
                           status=status,
                           entry_sz_fl=entry_sz_fl,
                           entry_parameters=entry_parameters,
                           btn_execute=btn_execute,
                           canvas=canvas, shape=shape)
            else:
                showerror(parent=root, title="Ошибка", message="Все поля должны быть заполнены!")


def size_check(parttype, part_name, mach, surname, status, entry_sz_fl, entry_parameters, btn_execute, canvas, shape):
    global call_count
    match parttype:
        case 'lug':      
            try:
                call_count += 1
                if call_count >= 2:
                    btn_execute.config(state='disabled')
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                sql_fetch_blob_query = """SELECT * from lugs_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, ))
                record = cursor.fetchone()
                index_max = [2,7,11,5,3,4,6,9,8,17,18,15,16,14,10,13,12]
                sizes_max = [record[i] for i in index_max]
                print(f'sizes_max are: {sizes_max}')
                index_min = [19,24,28,22,20,21,23,26,25,34,35,32,33,31,27,30,29]
                sizes_min = [record[i] for i in index_min]
                print(f'sizes_ent are: {entry_sz_fl}')
                print(f'sizes_min are: {sizes_min}')
                tab_sizes_max = [f'tab_size_max_{i}' for i in range (17)]
                tab_sizes_min = [f'tab_size_min_{i}' for i in range (17)]
                for i in range(17):
                    tab_sizes_max[i] = ttk.Label(canvas, text=sizes_max[i],anchor='center', width=5, justify='center', 
                                                 font='Helvetica 22')
                    tab_sizes_min[i] = ttk.Label(canvas, text=sizes_min[i],anchor='center', width=5, justify='center', 
                                                 font='Helvetica 22')
                match shape:
                    case 'l':
                        tab_sizes_min[0].place(anchor='nw',x=480, y=715) #d1
                        tab_sizes_min[1].place(anchor='nw',x=480,  y=945) #L
                        tab_sizes_min[2].place(anchor='nw',x=620, y=80) #W
                        tab_sizes_min[3].place(anchor='nw',x=620, y=163) #T
                        tab_sizes_min[4].place(anchor='nw',x=620, y=240) #d2
                        tab_sizes_min[5].place(anchor='nw',x=620, y=315) #t
                        tab_sizes_min[6].place(anchor='nw',x=620, y=443) #J
                        tab_sizes_min[7].place(anchor='nw',x=620, y=512) #l2
                        tab_sizes_min[8].place(anchor='nw',x=620, y=590) #l1
                        tab_sizes_min[9].place(anchor='nw',x=620,  y=810) #Dp31
                        tab_sizes_min[11].place(anchor='nw',x=620, y=885) #R1
                        tab_sizes_min[12].place(anchor='nw',x=1760,y=175) #R2
                        tab_sizes_min[13].place(anchor='nw',x=1760,y=443) #S
                        tab_sizes_min[14].place(anchor='nw',x=1760,y=510) #l4
                        tab_sizes_min[15].place(anchor='nw',x=1760,y=715) #B
                        tab_sizes_min[16].place(anchor='nw',x=1760,y=865) #D           
                        tab_sizes_max[0].place(anchor='nw',x=560, y=715) #d1
                        tab_sizes_max[1].place(anchor='nw',x=560,  y=945) #L
                        tab_sizes_max[2].place(anchor='nw',x=695, y=80) #W
                        tab_sizes_max[3].place(anchor='nw',x=695, y=163) #T
                        tab_sizes_max[4].place(anchor='nw',x=695, y=240) #d2
                        tab_sizes_max[5].place(anchor='nw',x=695, y=315) #t
                        tab_sizes_max[6].place(anchor='nw',x=695, y=443) #J
                        tab_sizes_max[7].place(anchor='nw',x=695, y=512) #l2
                        tab_sizes_max[8].place(anchor='nw',x=695, y=590) #l1
                        tab_sizes_max[9].place(anchor='nw',x=695,  y=810) #Dp31
                        tab_sizes_max[11].place(anchor='nw',x=695,y=885) #R1
                        tab_sizes_max[12].place(anchor='nw',x=1830,y=175) #R2
                        tab_sizes_max[13].place(anchor='nw',x=1830,y=443) #S
                        tab_sizes_max[14].place(anchor='nw',x=1830,y=510) #l4
                        tab_sizes_max[15].place(anchor='nw',x=1830,y=715) #B
                        tab_sizes_max[16].place(anchor='nw',x=1830,y=865) #D
               
                    case 'v':
                        tab_sizes_min[0].place(anchor='nw',x=480, y=715) #d1
                        tab_sizes_min[1].place(anchor='nw',x=480,  y=945) #L
                        tab_sizes_min[2].place(anchor='nw',x=620, y=80) #W
                        tab_sizes_min[3].place(anchor='nw',x=620, y=163) #T
                        tab_sizes_min[4].place(anchor='nw',x=620, y=240) #d2
                        tab_sizes_min[5].place(anchor='nw',x=620, y=315) #t
                        tab_sizes_min[6].place(anchor='nw',x=620, y=443) #J
                        tab_sizes_min[7].place(anchor='nw',x=620, y=512) #l2
                        tab_sizes_min[8].place(anchor='nw',x=620, y=590) #l1
                        tab_sizes_min[9].place(anchor='nw',x=620,  y=810) #Dp31
                        tab_sizes_min[11].place(anchor='nw',x=620, y=885) #R1
                        tab_sizes_min[12].place(anchor='nw',x=1760,y=175) #R2
                        tab_sizes_min[13].place(anchor='nw',x=1760,y=443) #S
                        tab_sizes_min[14].place(anchor='nw',x=1760,y=510) #l4
                        tab_sizes_min[15].place(anchor='nw',x=1760,y=715) #B
                        tab_sizes_min[16].place(anchor='nw',x=1760,y=865) #D   
                        tab_sizes_max[0].place(anchor='nw',x=560, y=715) #d1
                        tab_sizes_max[1].place(anchor='nw',x=560,  y=945) #L
                        tab_sizes_max[2].place(anchor='nw',x=695, y=80) #W
                        tab_sizes_max[3].place(anchor='nw',x=695, y=163) #T
                        tab_sizes_max[4].place(anchor='nw',x=695, y=240) #d2
                        tab_sizes_max[5].place(anchor='nw',x=695, y=315) #t
                        tab_sizes_max[6].place(anchor='nw',x=695, y=443) #J
                        tab_sizes_max[7].place(anchor='nw',x=695, y=512) #l2
                        tab_sizes_max[8].place(anchor='nw',x=695, y=590) #l1
                        tab_sizes_max[9].place(anchor='nw',x=695,  y=810) #Dp31
                        tab_sizes_max[11].place(anchor='nw',x=695,y=885) #R1
                        tab_sizes_max[12].place(anchor='nw',x=1830,y=175) #R2
                        tab_sizes_max[13].place(anchor='nw',x=1830,y=443) #S
                        tab_sizes_max[14].place(anchor='nw',x=1830,y=510) #l4
                        tab_sizes_max[15].place(anchor='nw',x=1830,y=715) #B
                        tab_sizes_max[16].place(anchor='nw',x=1830,y=865) #D
                
                    case 'lo':
                        tab_sizes_min[0].place(anchor='nw',x=480, y=715) #d1
                        tab_sizes_min[1].place(anchor='nw',x=480,  y=945) #L
                        tab_sizes_min[2].place(anchor='nw',x=620, y=80) #W
                        tab_sizes_min[3].place(anchor='nw',x=620, y=163) #T
                        tab_sizes_min[4].place(anchor='nw',x=620, y=240) #d2
                        tab_sizes_min[5].place(anchor='nw',x=620, y=315) #t
                        tab_sizes_min[6].place(anchor='nw',x=620, y=443) #J
                        #tab_sizes_min[7].place(anchor='nw',x=620, y=512) #l2
                        tab_sizes_min[8].place(anchor='nw',x=620, y=590) #l1
                        tab_sizes_min[9].place(anchor='nw',x=620,  y=810) #Dp31
                        tab_sizes_min[11].place(anchor='nw',x=620, y=885) #R1
                        tab_sizes_min[12].place(anchor='nw',x=1760,y=175) #R2
                        tab_sizes_min[13].place(anchor='nw',x=1760,y=443) #S
                        tab_sizes_min[14].place(anchor='nw',x=1760,y=510) #l4
                        tab_sizes_min[15].place(anchor='nw',x=1760,y=715) #B
                        tab_sizes_min[16].place(anchor='nw',x=1760,y=865) #D   
                        tab_sizes_max[0].place(anchor='nw',x=560, y=715) #d1
                        tab_sizes_max[1].place(anchor='nw',x=560,  y=945) #L
                        tab_sizes_max[2].place(anchor='nw',x=695, y=80) #W
                        tab_sizes_max[3].place(anchor='nw',x=695, y=163) #T
                        tab_sizes_max[4].place(anchor='nw',x=695, y=240) #d2
                        tab_sizes_max[5].place(anchor='nw',x=695, y=315) #t
                        tab_sizes_max[6].place(anchor='nw',x=695, y=443) #J
                        #tab_sizes_max[7].place(anchor='nw',x=695, y=512) #l2
                        tab_sizes_max[8].place(anchor='nw',x=695, y=590) #l1
                        tab_sizes_max[9].place(anchor='nw',x=695,  y=810) #Dp31
                        tab_sizes_max[11].place(anchor='nw',x=695,y=885) #R1
                        tab_sizes_max[12].place(anchor='nw',x=1830,y=175) #R2
                        tab_sizes_max[13].place(anchor='nw',x=1830,y=443) #S
                        tab_sizes_max[14].place(anchor='nw',x=1830,y=510) #l4
                        tab_sizes_max[15].place(anchor='nw',x=1830,y=715) #B
                        tab_sizes_max[16].place(anchor='nw',x=1830,y=865) #D

                imprtnt = [1,3,4,5,6,7,8,15,16]
                unimprtnt = [0,2,9,10,11,12,13,14]
                for i in imprtnt:
                    if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                        entry_parameters[i]['background']="#00FF00"
                    else:
                        entry_parameters[i]['background']="red"
                for i in unimprtnt:
                    if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                        entry_parameters[i]['background']="#00FF00"
                    else:
                        entry_parameters[i]['background']="yellow"

                sz_letters = ['d1', 'L', 'W', 'T', 'd2','t','J','l2','l1','Dp31','R1', 'R2', 'S', 'l4', 'B', 'D']
                failed_sz=[]
                
                for i in range(16):
                    if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                        pass
                    else:
                        failed_sz.append(f'{sz_letters[i]}:{sizes_min[i]}...{sizes_max[i]}')
                comment_line = f'{", ".join(failed_sz)}'

                if sizes_min[1]<=entry_sz_fl[1]<=sizes_max[1] \
                and sizes_min[2]<=entry_sz_fl[2]<=sizes_max[2] \
                and sizes_min[3]<=entry_sz_fl[3]<=sizes_max[3] \
                and sizes_min[4]<=entry_sz_fl[4]<=sizes_max[4] \
                and sizes_min[5]<=entry_sz_fl[5]<=sizes_max[5] \
                and sizes_min[6]<=entry_sz_fl[6]<=sizes_max[6] \
                and sizes_min[7]<=entry_sz_fl[7]<=sizes_max[7] \
                and sizes_min[0]<=entry_sz_fl[0]<=sizes_max[0]:
                    showinfo(title="Успешная проверка", message="Все ключевые размеры соответствуют чертежу, можно приступать к работе.")
                    success_mark = 1
                else:
                    showinfo(title="Проверка не пройдена", 
                              message="Присутствуют несоответствия в ключевых размерах. Произведите подналадку либо проконсультируйтесь с технологом/мастером.")
                    success_mark = 2
                cursor.close()
                size_insert(parttype=parttype, 
                           part_name=part_name,
                           mach=mach, 
                           surname=surname, 
                           status=status, 
                           entry_sz_fl=entry_sz_fl,
                           success_mark=success_mark,
                           shape=shape,
                           comment=comment_line)
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Действие завершено. Соединение с SQLite закрыто")
        case 'con':
            try:
                call_count += 1
                if call_count >= 2:
                    btn_execute.config(state='disabled')
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                sql_fetch_blob_query = """SELECT * from connectors_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, ))
                record = cursor.fetchone()
                match shape:
                    case 'l':
                        tab_index_max = [2,7,10,5,3,4,6,8,9,12,11,10,5,3,4,6,8,9,12,11]
                        index_max = [2,7,10,5,3,4,6,9,8,12,11,10,5,3,4,6,9,8,12,11]
                        sizes_max = [record[i] for i in index_max]
                        tab_sizes_max = [record[i] for i in tab_index_max]
                        print(f'sizes_max are: {sizes_max}')
                        tab_index_min = [13,18,21,16,14,15,17,19,20,23,22,21,16,14,15,17,19,20,23,22]
                        tab_sizes_min = [record[i] for i in tab_index_min]
                        index_min = [13,18,21,16,14,15,17,20,19,23,22,21,16,14,15,17,20,19,23,22]
                        sizes_min = [record[i] for i in index_min]
                        print(f'sizes_ent are: {entry_sz_fl}')
                        print(f'sizes_min are: {sizes_min}')

                        tb_sizes_max = [f'tab_size_max_{i}' for i in tab_index_max]  
                        tb_sizes_min = [f'tab_size_min_{i}' for i in tab_index_min]
                        for i in range(11):
                            tb_sizes_max[i] = ttk.Label(canvas, text=tab_sizes_max[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')
                            tb_sizes_min[i] = ttk.Label(canvas, text=tab_sizes_min[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')
                    case 'lo':
                        tab_index_max = [2,7,10,5,3,4,6,8,9,12,11,10,5,3,4,6,8,9,12,11]
                        index_max = [2,7,10,5,3,4,6,9,8,12,11,10,5,3,4,6,9,8,12,11]
                        sizes_max = [record[i] for i in index_max]
                        tab_sizes_max = [record[i] for i in tab_index_max]
                        print(f'sizes_max are: {sizes_max}')
                        tab_index_min = [13,18,21,16,14,15,17,19,20,23,22,21,16,14,15,17,19,20,23,22]
                        tab_sizes_min = [record[i] for i in tab_index_min]
                        index_min = [13,18,21,16,14,15,17,20,19,23,22,21,16,14,15,17,20,19,23,22]
                        sizes_min = [record[i] for i in index_min]
                        print(f'sizes_ent are: {entry_sz_fl}')
                        print(f'sizes_min are: {sizes_min}')

                        tb_sizes_max = [f'tab_size_max_{i}' for i in tab_index_max]  
                        tb_sizes_min = [f'tab_size_min_{i}' for i in tab_index_min]
                        for i in range(11):
                            tb_sizes_max[i] = ttk.Label(canvas, text=tab_sizes_max[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')
                            tb_sizes_min[i] = ttk.Label(canvas, text=tab_sizes_min[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')
                    case 'v':
                        tab_index_max = [2,7,10,5,3,4,6,8,9,12,11,10,5,3,4,6,8,9,12,11]
                        index_max = [2,7,10,5,3,4,6,9,8,12,11,10,5,3,4,6,9,8,12,11]
                        sizes_max = [record[i] for i in index_max]
                        tab_sizes_max = [record[i] for i in tab_index_max]
                        print(f'sizes_max are: {sizes_max}')
                        tab_index_min = [13,18,21,16,14,15,17,19,20,23,22,21,16,14,15,17,19,20,23,22]
                        tab_sizes_min = [record[i] for i in tab_index_min]
                        index_min = [13,18,21,16,14,15,17,20,19,23,22,21,16,14,15,17,20,19,23,22]
                        sizes_min = [record[i] for i in index_min]
                        print(f'sizes_ent are: {entry_sz_fl}')
                        print(f'sizes_min are: {sizes_min}')

                        tb_sizes_max = [f'tab_size_max_{i}' for i in tab_index_max]  
                        tb_sizes_min = [f'tab_size_min_{i}' for i in tab_index_min]
                        for i in range(11):
                            tb_sizes_max[i] = ttk.Label(canvas, text=tab_sizes_max[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')
                            tb_sizes_min[i] = ttk.Label(canvas, text=tab_sizes_min[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')   
                    case 's':
                        tab_index_max = [2,10,5,3,4,6,8,9,11,12]
                        index_max = [2,10,5,3,4,6,9,8,12,11]
                        sizes_max = [record[i] for i in index_max]
                        tab_sizes_max = [record[i] for i in tab_index_max]
                        print(f'sizes_max are: {sizes_max}')
                        tab_index_min = [13,21,16,14,15,17,19,20,22,23]
                        tab_sizes_min = [record[i] for i in tab_index_min]
                        index_min = [13,21,16,14,15,17,20,19,23,22]
                        sizes_min = [record[i] for i in index_min]
                        print(f'sizes_ent are: {entry_sz_fl}')
                        print(f'sizes_min are: {sizes_min}')

                        tb_sizes_max = [f'tab_size_max_{i}' for i in tab_index_max]  
                        tb_sizes_min = [f'tab_size_min_{i}' for i in tab_index_min]
                        for i in range(10):
                            tb_sizes_max[i] = ttk.Label(canvas, text=tab_sizes_max[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')
                            tb_sizes_min[i] = ttk.Label(canvas, text=tab_sizes_min[i],anchor='center', width=5, justify='center', 
                                                         font='Helvetica 24')   

                match shape:
                    case 'l':
                        tb_sizes_max[0].place(anchor='nw', x=420,  y=740) #d1
                        tb_sizes_max[1].place(anchor='nw', x=420,  y=941) #L
                        tb_sizes_max[2].place(anchor='nw', x=1810, y=78)#W
                        tb_sizes_max[3].place(anchor='nw', x=1810, y=185)#T
                        tb_sizes_max[4].place(anchor='nw', x=1810, y=270)#d2
                        tb_sizes_max[5].place(anchor='nw', x=1810, y=343)#t
                        tb_sizes_max[6].place(anchor='nw', x=1810, y=441)#J
                        tb_sizes_max[7].place(anchor='nw', x=1810, y=616)#l1
                        tb_sizes_max[8].place(anchor='nw', x=1810, y=526)#l2
                        tb_sizes_max[9].place(anchor='nw', x=1810, y=785)#Dp3                        
                        tb_sizes_max[10].place(anchor='nw',x=1810, y=892)#R1
                        tb_sizes_min[0].place(anchor='nw', x=320,  y=740) #d1
                        tb_sizes_min[1].place(anchor='nw', x=320,  y=941) #L
                        tb_sizes_min[2].place(anchor='nw', x=1720, y=78)#W
                        tb_sizes_min[3].place(anchor='nw', x=1720, y=185)#T
                        tb_sizes_min[4].place(anchor='nw', x=1720, y=270)#d2
                        tb_sizes_min[5].place(anchor='nw', x=1720, y=343)#t
                        tb_sizes_min[6].place(anchor='nw', x=1720, y=441)#J
                        tb_sizes_min[7].place(anchor='nw', x=1720, y=616)#l2
                        tb_sizes_min[8].place(anchor='nw', x=1720, y=526)#l1
                        tb_sizes_min[9].place(anchor='nw', x=1720, y=785)#Dp3
                        tb_sizes_min[10].place(anchor='nw',x=1720, y=892)#R1
                    
                    case 'lo':
                        tb_sizes_max[0].place(anchor='nw', x=420,  y=740) #d1
                        tb_sizes_max[1].place(anchor='nw', x=420,  y=941) #L
                        tb_sizes_max[2].place(anchor='nw', x=1810, y=78)#W
                        tb_sizes_max[3].place(anchor='nw', x=1810, y=185)#T
                        tb_sizes_max[4].place(anchor='nw', x=1810, y=270)#d2
                        tb_sizes_max[5].place(anchor='nw', x=1810, y=343)#t
                        tb_sizes_max[6].place(anchor='nw', x=1810, y=441)#J
                        tb_sizes_max[7].place(anchor='nw', x=1810, y=616)#l1
                        #tb_sizes_max[8].place(anchor='nw', x=1810, y=526)#l2
                        tb_sizes_max[9].place(anchor='nw', x=1810, y=785)#Dp3                        
                        tb_sizes_max[10].place(anchor='nw',x=1810, y=892)#R1
                        tb_sizes_min[0].place(anchor='nw', x=320,  y=740) #d1
                        tb_sizes_min[1].place(anchor='nw', x=320,  y=941) #L
                        tb_sizes_min[2].place(anchor='nw', x=1720, y=78)#W
                        tb_sizes_min[3].place(anchor='nw', x=1720, y=185)#T
                        tb_sizes_min[4].place(anchor='nw', x=1720, y=270)#d2
                        tb_sizes_min[5].place(anchor='nw', x=1720, y=343)#t
                        tb_sizes_min[6].place(anchor='nw', x=1720, y=441)#J
                        tb_sizes_min[7].place(anchor='nw', x=1720, y=616)#l2
                        #tb_sizes_min[8].place(anchor='nw', x=1720, y=526)#l1
                        tb_sizes_min[9].place(anchor='nw', x=1720, y=785)#Dp3
                        tb_sizes_min[10].place(anchor='nw',x=1720, y=892)#R1
                    case 'v':
                        tb_sizes_max[0].place(anchor='n',x=470, y=728) #d1
                        tb_sizes_max[1].place(anchor='n',x=470,  y=941) #L
                        tb_sizes_max[2].place(anchor='n',x=1870, y=80)#W
                        tb_sizes_max[3].place(anchor='n',x=1870, y=182)#T
                        tb_sizes_max[4].place(anchor='n',x=1870, y=267)#d2
                        tb_sizes_max[5].place(anchor='n',x=1870, y=352)#t
                        tb_sizes_max[6].place(anchor='n',x=1870, y=460)#J
                        tb_sizes_max[7].place(anchor='n',x=1870, y=607)#l1
                        tb_sizes_max[8].place(anchor='n',x=1870, y=525)#l2
                        tb_sizes_max[9].place(anchor='n',x=1870, y=777)#R1
                        tb_sizes_max[10].place(anchor='n',x=1870,y=898)#Dp3
                        tb_sizes_min[0].place(anchor='n',x=370, y=727) #d1
                        tb_sizes_min[1].place(anchor='n',x=370,  y=940) #L
                        tb_sizes_min[2].place(anchor='n',x=1790, y=79)#W
                        tb_sizes_min[3].place(anchor='n',x=1790, y=182)#T
                        tb_sizes_min[4].place(anchor='n',x=1790, y=267)#d2
                        tb_sizes_min[5].place(anchor='n',x=1790, y=352)#t
                        tb_sizes_min[6].place(anchor='n',x=1790, y=459)#J
                        tb_sizes_min[7].place(anchor='n',x=1790, y=607)#l2
                        tb_sizes_min[8].place(anchor='n',x=1790, y=525)#l1
                        tb_sizes_min[9].place(anchor='n',x=1790, y=777)#R1
                        tb_sizes_min[10].place(anchor='n',x=1790,y=898)#Dp3
                    case 's':
                        tb_sizes_max[0].place(anchor='n',x=515, y=795) #d1
                        tb_sizes_max[1].place(anchor='n',x=1870, y=95)#W
                        tb_sizes_max[2].place(anchor='n',x=1870, y=270)#T
                        tb_sizes_max[3].place(anchor='n',x=1870, y=355)#d2
                        tb_sizes_max[4].place(anchor='n',x=1870, y=425)#t
                        tb_sizes_max[5].place(anchor='n',x=1870, y=515)#J
                        tb_sizes_max[6].place(anchor='n',x=1870, y=680)#l1
                        tb_sizes_max[7].place(anchor='n',x=1870, y=595)#l2
                        tb_sizes_max[8].place(anchor='n',x=1870, y=960)#R1
                        tb_sizes_max[9].place(anchor='n',x=1870,y=840)#Dp3
                        tb_sizes_min[0].place(anchor='n',x=430, y=795) #d1
                        tb_sizes_min[1].place(anchor='n',x=1790, y=95)#W
                        tb_sizes_min[2].place(anchor='n',x=1790, y=270)#T
                        tb_sizes_min[3].place(anchor='n',x=1790, y=355)#d2
                        tb_sizes_min[4].place(anchor='n',x=1790, y=425)#t
                        tb_sizes_min[5].place(anchor='n',x=1790, y=515)#J
                        tb_sizes_min[6].place(anchor='n',x=1790, y=680)#l2
                        tb_sizes_min[7].place(anchor='n',x=1790, y=595)#l1
                        tb_sizes_min[8].place(anchor='n',x=1790, y=960)#R1
                        tb_sizes_min[9].place(anchor='n',x=1790,y=840)#Dp3
                match shape:    
                    case 'l':
                        unimportant_szs = [0,2,9,10,11,18,19]
                        important_szs = [1,3,4,5,6,7,8,12,13,14,15,16,17] 
                        for i in important_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="red"
                        for i in unimportant_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="yellow"

                        sz_letters = ['d1', 'L', 'W1', 'T1', 'd21','t1','J1','l21','l11','Dp31','R11', 'W2', 'T2', 'd22','t2','J2','l22','l12','Dp32','R12']
                        failed_sz=[]

                        for i in range(20):
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                pass
                            else:
                                failed_sz.append(f'{sz_letters[i]}:{sizes_min[i]}...{sizes_max[i]}')
                        comment_line = f'{", ".join(failed_sz)}'

                        if sizes_min[1]<=entry_sz_fl[1]<=sizes_max[1] \
                        and sizes_min[3]<=entry_sz_fl[3]<=sizes_max[3] \
                        and sizes_min[4]<=entry_sz_fl[4]<=sizes_max[4] \
                        and sizes_min[5]<=entry_sz_fl[5]<=sizes_max[5] \
                        and sizes_min[6]<=entry_sz_fl[6]<=sizes_max[6] \
                        and sizes_min[7]<=entry_sz_fl[7]<=sizes_max[7] \
                        and sizes_min[8]<=entry_sz_fl[8]<=sizes_max[8] \
                        and sizes_min[12]<=entry_sz_fl[12]<=sizes_max[12] \
                        and sizes_min[13]<=entry_sz_fl[13]<=sizes_max[13] \
                        and sizes_min[14]<=entry_sz_fl[14]<=sizes_max[14] \
                        and sizes_min[15]<=entry_sz_fl[15]<=sizes_max[15] \
                        and sizes_min[16]<=entry_sz_fl[16]<=sizes_max[16] \
                        and sizes_min[17]<=entry_sz_fl[17]<=sizes_max[17]:
                            showinfo(title="Успешная проверка", message="Все ключевые размеры соответствуют чертежу, можно приступать к работе.")
                            success_mark = 1
                        else:
                            showinfo(title="Проверка не пройдена", 
                                      message="Присутствуют несоответствия в ключевых размерах. Произведите подналадку либо проконсультируйтесь с технологом/мастером.")
                            success_mark = 2
                        cursor.close()
                    case 'lo':
                        unimportant_szs = [0,2,9,10,11,18,19]
                        important_szs = [1,3,4,5,6,7,8,12,13,14,15,16,17] 
                        for i in important_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="red"
                        for i in unimportant_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="yellow"

                        sz_letters = ['d1', 'L', 'W1', 'T1', 'd21','t1','J1','l21','l11','Dp31','R11', 'W2', 'T2', 'd22','t2','J2','l22','l12','Dp32','R12']
                        failed_sz=[]

                        for i in range(20):
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                pass
                            else:
                                failed_sz.append(f'{sz_letters[i]}:{sizes_min[i]}...{sizes_max[i]}')
                        comment_line = f'{", ".join(failed_sz)}'

                        if sizes_min[1]<=entry_sz_fl[1]<=sizes_max[1] \
                        and sizes_min[3]<=entry_sz_fl[3]<=sizes_max[3] \
                        and sizes_min[4]<=entry_sz_fl[4]<=sizes_max[4] \
                        and sizes_min[5]<=entry_sz_fl[5]<=sizes_max[5] \
                        and sizes_min[6]<=entry_sz_fl[6]<=sizes_max[6] \
                        and sizes_min[7]<=entry_sz_fl[7]<=sizes_max[7] \
                        and sizes_min[8]<=entry_sz_fl[8]<=sizes_max[8] \
                        and sizes_min[12]<=entry_sz_fl[12]<=sizes_max[12] \
                        and sizes_min[13]<=entry_sz_fl[13]<=sizes_max[13] \
                        and sizes_min[14]<=entry_sz_fl[14]<=sizes_max[14] \
                        and sizes_min[15]<=entry_sz_fl[15]<=sizes_max[15] \
                        and sizes_min[16]<=entry_sz_fl[16]<=sizes_max[16] \
                        and sizes_min[17]<=entry_sz_fl[17]<=sizes_max[17]:
                            showinfo(title="Успешная проверка", message="Все ключевые размеры соответствуют чертежу, можно приступать к работе.")
                            success_mark = 1
                        else:
                            showinfo(title="Проверка не пройдена", 
                                      message="Присутствуют несоответствия в ключевых размерах. Произведите подналадку либо проконсультируйтесь с технологом/мастером.")
                            success_mark = 2
                        cursor.close()
                    case 'v':
                        unimportant_szs = [0,2,9,10,11,18,19]
                        important_szs = [1,3,4,5,6,7,8,12,13,14,15,16,17] 
                        for i in important_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="red"
                        for i in unimportant_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="yellow"

                        sz_letters = ['d1', 'L', 'W1', 'T1', 'd21','t1','J1','l21','l11','Dp31','R11', 'W2', 'T2', 'd22','t2','J2','l22','l12','Dp32','R12']
                        failed_sz=[]

                        for i in range(20):
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                pass
                            else:
                                failed_sz.append(f'{sz_letters[i]}:{sizes_min[i]}...{sizes_max[i]}')
                        comment_line = f'{", ".join(failed_sz)}'

                        if sizes_min[1]<=entry_sz_fl[1]<=sizes_max[1] \
                        and sizes_min[3]<=entry_sz_fl[3]<=sizes_max[3] \
                        and sizes_min[4]<=entry_sz_fl[4]<=sizes_max[4] \
                        and sizes_min[5]<=entry_sz_fl[5]<=sizes_max[5] \
                        and sizes_min[6]<=entry_sz_fl[6]<=sizes_max[6] \
                        and sizes_min[7]<=entry_sz_fl[7]<=sizes_max[7] \
                        and sizes_min[8]<=entry_sz_fl[8]<=sizes_max[8] \
                        and sizes_min[12]<=entry_sz_fl[12]<=sizes_max[12] \
                        and sizes_min[13]<=entry_sz_fl[13]<=sizes_max[13] \
                        and sizes_min[14]<=entry_sz_fl[14]<=sizes_max[14] \
                        and sizes_min[15]<=entry_sz_fl[15]<=sizes_max[15] \
                        and sizes_min[16]<=entry_sz_fl[16]<=sizes_max[16] \
                        and sizes_min[17]<=entry_sz_fl[17]<=sizes_max[17]:
                            showinfo(title="Успешная проверка", message="Все ключевые размеры соответствуют чертежу, можно приступать к работе.")
                            success_mark = 1
                        else:
                            showinfo(title="Проверка не пройдена", 
                                      message="Присутствуют несоответствия в ключевых размерах. Произведите подналадку либо проконсультируйтесь с технологом/мастером.")
                            success_mark = 2
                        cursor.close()
                    case 's':
                        unimportant_szs = [0,1,8,9]
                        important_szs = [2,3,4,5,6,7]
                        for i in important_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="red"
                        for i in unimportant_szs:
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                entry_parameters[i]['background']="#00FF00"
                            else:
                                entry_parameters[i]['background']="yellow"

                        sz_letters = ['d1', 'W', 'T', 'd2', 't','J','l2','l1','Dp31','R1']
                        failed_sz=[]

                        for i in range(10):
                            if sizes_min[i]<=entry_sz_fl[i]<=sizes_max[i]:
                                pass
                            else:
                                failed_sz.append(f'{sz_letters[i]}:{sizes_min[i]}...{sizes_max[i]}')
                        comment_line = f'{", ".join(failed_sz)}'

                        if sizes_min[2]<=entry_sz_fl[2]<=sizes_max[2] \
                        and sizes_min[3]<=entry_sz_fl[3]<=sizes_max[3] \
                        and sizes_min[4]<=entry_sz_fl[4]<=sizes_max[4] \
                        and sizes_min[5]<=entry_sz_fl[5]<=sizes_max[5] \
                        and sizes_min[6]<=entry_sz_fl[6]<=sizes_max[6] \
                        and sizes_min[7]<=entry_sz_fl[7]<=sizes_max[7]:
                            showinfo(title="Успешная проверка", message="Все ключевые размеры соответствуют чертежу, можно приступать к работе.")
                            success_mark = 1
                        else:
                            showinfo(title="Проверка не пройдена", 
                                      message="Присутствуют несоответствия в ключевых размерах. Произведите подналадку либо проконсультируйтесь с технологом/мастером.")
                            success_mark = 2
                        cursor.close()

                size_insert(parttype=parttype, 
                           part_name=part_name,
                           mach=mach, 
                           surname=surname, 
                           status=status, 
                           entry_sz_fl=entry_sz_fl, 
                           success_mark=success_mark, 
                           shape=shape, 
                           comment=comment_line)
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Действие завершено. Соединение с SQLite закрыто") #Функция проверки введенных размеров


def size_insert(parttype, part_name, mach, surname, status, entry_sz_fl, success_mark,shape,comment):
    match parttype:
        case 'lug':
            match success_mark:
                case 1:
                    verdict = 'B'
                case 2:
                    verdict = 'H'
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                sqlite_insert_query = """INSERT INTO lugs_results
                          (mach, Fio, status, Date, Time, name, verdict,d1,L,W,tb,d2,t,J,l2,l1,Dp31,Dp32,R1,R2,S,l4,B,D,comment)
                          VALUES
                          (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

                current_time = datetime.now().strftime("%H:%M:%S")
                to_insert = (mach, surname, status, date.today(), current_time, part_name, verdict, *entry_sz_fl, comment)                  
                cursor.execute(sqlite_insert_query, to_insert)
                sqlite_connection.commit()
                print("Запись успешно вставлена ​​в таблицу cnc_results ", cursor.rowcount)
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Соединение с SQLite закрыто")                    
        case 'con':
            match success_mark:
                case 1:
                    verdict = 'B'
                case 2:
                    verdict = 'H'
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                match shape:
                    case 'l':
                        sqlite_insert_query = """INSERT INTO connectors_results
                                  (mach, Fio, status, Date, Time, part_name, verdict, d1, L, W1, tb1, d21, t1, J1, l21, l11, Dp31, R11, W2, tb2, d22, t2, J2, l22, l12, Dp32, R12, comment)
                                  VALUES
                                  (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
                    case 'lo':
                        sqlite_insert_query = """INSERT INTO connectors_results
                                  (mach, Fio, status, Date, Time, part_name, verdict, d1, L, W1, tb1, d21, t1, J1, l21, l11, Dp31, R11, W2, tb2, d22, t2, J2, l22, l12, Dp32, R12, comment)
                                  VALUES
                                  (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""    
                    case 'v':
                        sqlite_insert_query = """INSERT INTO connectors_results
                                  (mach, Fio, status, Date, Time, part_name, verdict, d1, L, W1, tb1, d21, t1, J1, l21, l11, Dp31, R11, W2, tb2, d22, t2, J2, l22, l12, Dp32, R12, comment)
                                  VALUES
                                  (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
                    case 's':
                        sqlite_insert_query = """INSERT INTO connectors_results
                                  (mach, Fio, status, Date, Time, part_name, verdict, d1, L, W1, tb1, d21, t1, J1, l21, l11, Dp31, R11, W2, tb2, d22, t2, J2, l22, l12, Dp32, R12, comment)
                                  VALUES
                                  (?,?,?,?,?,?,?,?,0,?,?,?,?,?,?,?,?,?,0,0,0,0,0,0,0,0,0,?);"""


                current_time = datetime.now().strftime("%H:%M:%S")
                to_insert = (mach, surname, status, date.today(), current_time, part_name, verdict, *entry_sz_fl, comment)                  
                cursor.execute(sqlite_insert_query, to_insert)
                sqlite_connection.commit()
                print("Запись успешно вставлена ​​в таблицу connectors_results ", cursor.rowcount)
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Соединение с SQLite закрыто")


def meas_to_main(parttype):
    global call_count
    call_count=0
    match parttype:
        case 'lug':
            frame_44.place_forget()
            frame_0.place(x=0, y=0)
            navi_frame()
        case 'con':    
            frame_4.place_forget()
            frame_0.place(x=0, y=0)
            navi_frame()


def main_to_blueprint():
    for widget in frame_6.winfo_children():
        widget.destroy()
    try:
        frame_6.place(x=0,y=0)
        frame_0.place_forget()
        sqlite_connection = sqlite3.connect('pics.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_fetch_blob_query = """SELECT part_name FROM pics"""
        cursor.execute(sql_fetch_blob_query)
        parts_tuple = cursor.fetchall()
        part_list = ttk.Combobox(frame_6,font='Helvetica 30', 
                                 width=15, height=31, 
                                 values=parts_tuple, 
                                 state='readonly') #Выпадающий список с номенклатурой
        part_list.current(1)
        part_list.place(anchor='w', x=10, y=50)
        cursor.close()
        ex_pic_button = ttk.Button(frame_6, 
                                   text='Отобразить эскиз',
                                   style='my.TButton',
                                   width=15,
                                   command=lambda: parttype_get(part_name=part_list.get()))
        ex_pic_button.place(anchor=NW, x=10, y=100)
        btn_menu = ttk.Button(frame_6,
                              text='В главное меню',
                              style='my.TButton',                              
                              width=15, 
                              command=lambda: pics_to_main())
        btn_menu.place(anchor='sw', x=10, y=1000)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Действие завершено. Соединение с SQLite закрыто") #Запрос на список деталей

def parttype_get(part_name):
    try:
        sqlite_connection = sqlite3.connect('pics.db')
        cursor = sqlite_connection.cursor()
        sql_fetch_blob_query = """SELECT parttype FROM pics WHERE part_name=?"""
        cursor.execute(sql_fetch_blob_query, (part_name, ))
        query_rslt = cursor.fetchone()
        parttype = query_rslt[0]
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Действие завершено. Соединение с SQLite закрыто")
            print(f"{parttype}")
    show_blueprint(part_name=part_name, parttype=parttype)





def show_blueprint(part_name, parttype):
    info_canvas = Canvas(frame_6, width=500, height=750, background='#f0f0f0', highlightthickness=0)
    info_canvas.place (x=10,y=160)
    tech_req_1 = Label(info_canvas, text='1. Данный эскиз отражает табличные значения предельных размеров. Применяется в справочных целях.', wraplength=500, font='Helvetica 20', background='#f0f0f0', justify='left')
    tech_req_1.place(anchor='nw', x=0, y=10)
    tech_req_2 = Label(info_canvas, text='2. Перед началом работы получить чертеж и эскиз в бумажном исполнении. Произвести настройку оборудования.', font='Helvetica 20', background='#f0f0f0', wraplength=500, justify='left')
    tech_req_2.place(anchor='nw', x=0, y=100)
    tech_req_2 = Label(info_canvas, text='3. Провести контроль изделия в программе. При несоответствии размеров на чертеже и в программе сообщить технологу.', font='Helvetica 20', background='#f0f0f0', wraplength=500, justify='left')
    tech_req_2.place(anchor='nw', x=0, y=220)
    
    match parttype:
        case 'lugl':
            global lugl_img_rnd
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0', highlightthickness=0)
            canvas.background = lugl_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=lugl_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT * from lugs_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','l4','W','D','B','S','R1','R2','Dp31']
            
            line_d1 = f"Ø {record[19]} ... {record[2]}"
            line_d2 = f"Ø {record[20]} ... {record[3]}"
            line_t = f"{record[21]} ... {record[4]}"
            line_tb = f"{record[22]} ... {record[5]}"
            line_J = f"{record[23]} ... {record[6]}"
            line_L = f"{record[24]} ... {record[7]}"
            line_l1 = f"{record[25]} ... {record[8]}"
            line_l2 = f"{record[26]} ... {record[9]}"
            line_l4 = f"{record[27]} ... {record[10]}"
            line_W = f"{record[28]} ... {record[11]}"
            line_D = f"Ø {record[29]} ... {record[12]}"
            line_B = f"{record[30]} ... {record[13]}"
            line_S = f"{record[31]} ... {record[14]}"
            line_R1 = f"{record[32]} ... {record[15]}"
            line_R2 = f"{record[33]} ... {record[16]}"
            line_Dp = f"Ø {record[34]} ... {record[17]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_l4,line_W,line_D,line_B,line_S,line_R1,line_R2,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(16):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
                
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=710)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=225)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=310)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=150)#tb
            sz_lbl[4].place(anchor= 'nw',    x=490,     y=430)#J
            sz_lbl[5].place(anchor= 'nw',    x=630,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=580)#l1
            sz_lbl[7].place(anchor= 'nw',    x=55,      y=500)#l2
            sz_lbl[8].place(anchor= 'nw',    x=1100,    y=500)#l4
            sz_lbl[9].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[10].place(anchor='nw',    x=1045,    y=855)#D
            sz_lbl[11].place(anchor='nw',    x=1060,    y=710)#B
            sz_lbl[12].place(anchor='nw',    x=1100,    y=430)#S
            sz_lbl[13].place(anchor='nw',    x=55,      y=900)#R1
            sz_lbl[14].place(anchor='nw',    x=1100,    y=165)#R2
            sz_lbl[15].place(anchor='nw',    x=55,      y=800)#Dp
        case 'luglo':            
            global luglo_img_rnd
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0',highlightthickness=0)
            canvas.background = luglo_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=luglo_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT * from lugs_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','l4','W','D','B','S','R1','R2','Dp31']
            
            line_d1 = f"Ø {record[19]} ... {record[2]}"
            line_d2 = f"Ø {record[20]} ... {record[3]}"
            line_t = f"{record[21]} ... {record[4]}"
            line_tb = f"{record[22]} ... {record[5]}"
            line_J = f"{record[23]} ... {record[6]}"
            line_L = f"{record[24]} ... {record[7]}"
            line_l1 = f"{record[25]} ... {record[8]}"
            line_l2 = f"{record[26]} ... {record[9]}"
            line_l4 = f"{record[27]} ... {record[10]}"
            line_W = f"{record[28]} ... {record[11]}"
            line_D = f"Ø {record[29]} ... {record[12]}"
            line_B = f"{record[30]} ... {record[13]}"
            line_S = f"{record[31]} ... {record[14]}"
            line_R1 = f"{record[32]} ... {record[15]}"
            line_R2 = f"{record[33]} ... {record[16]}"
            line_Dp = f"Ø {record[34]} ... {record[17]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_l4,line_W,line_D,line_B,line_S,line_R1,line_R2,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(16):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
                
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=710)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=225)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=310)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=150)#tb
            sz_lbl[4].place(anchor= 'nw',    x=490,     y=430)#J
            sz_lbl[5].place(anchor= 'nw',    x=640,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=580)#l1
            sz_lbl[8].place(anchor= 'nw',    x=1100,    y=500)#l4
            sz_lbl[9].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[10].place(anchor='nw',    x=1045,    y=855)#D
            sz_lbl[11].place(anchor='nw',    x=1060,    y=710)#B
            sz_lbl[12].place(anchor='nw',    x=1100,    y=430)#S
            sz_lbl[13].place(anchor='nw',    x=55,      y=900)#R1
            sz_lbl[14].place(anchor='nw',    x=1100,    y=165)#R2
            sz_lbl[15].place(anchor='nw',    x=55,      y=800)#Dp
        case 'lugv':
            global lugv_img_rnd            
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0', highlightthickness=0)
            canvas.background = lugv_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=lugv_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT * from lugs_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','l4','W','D','B','S','R1','R2','Dp31']
            
            line_d1 = f"Ø {record[19]} ... {record[2]}"
            line_d2 = f"Ø {record[20]} ... {record[3]}"
            line_t = f"{record[21]} ... {record[4]}"
            line_tb = f"{record[22]} ... {record[5]}"
            line_J = f"{record[23]} ... {record[6]}"
            line_L = f"{record[24]} ... {record[7]}"
            line_l1 = f"{record[25]} ... {record[8]}"
            line_l2 = f"{record[26]} ... {record[9]}"
            line_l4 = f"{record[27]} ... {record[10]}"
            line_W = f"{record[28]} ... {record[11]}"
            line_D = f"Ø {record[29]} ... {record[12]}"
            line_B = f"{record[30]} ... {record[13]}"
            line_S = f"{record[31]} ... {record[14]}"
            line_R1 = f"{record[32]} ... {record[15]}"
            line_R2 = f"{record[33]} ... {record[16]}"
            line_Dp = f"Ø {record[34]} ... {record[17]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_l4,line_W,line_D,line_B,line_S,line_R1,line_R2,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(16):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=710)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=225)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=310)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=150)#tb
            sz_lbl[4].place(anchor= 'nw',    x=490,     y=430)#J
            sz_lbl[5].place(anchor= 'nw',    x=620,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=580)#l1
            sz_lbl[7].place(anchor= 'nw',    x=55,      y=500)#l2
            sz_lbl[8].place(anchor= 'nw',    x=1100,    y=500)#l4
            sz_lbl[9].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[10].place(anchor='nw',    x=1045,    y=855)#D
            sz_lbl[11].place(anchor='nw',    x=1060,    y=710)#B
            sz_lbl[12].place(anchor='nw',    x=1080,    y=430)#S
            sz_lbl[13].place(anchor='nw',    x=55,      y=880)#R1
            sz_lbl[14].place(anchor='nw',    x=1100,    y=165)#R2
            sz_lbl[15].place(anchor='nw',    x=55,      y=800)#Dp
        case 'conl':
            global conl_img_rnd            
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0', highlightthickness=0)
            canvas.background = conl_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=conl_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")
                sql_fetch_blob_query = """SELECT * from connectors_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','W','R1','Dp31']
            
            line_d1 = f"Ø {record[13]} ... {record[2]}"
            line_d2 = f"Ø {record[14]} ... {record[3]}"
            line_t = f"{record[15]} ... {record[4]}"
            line_tb = f"{record[16]} ... {record[5]}"
            line_J = f"{record[17]} ... {record[6]}"
            line_L = f"{record[18]} ... {record[7]}"
            line_l1 = f"{record[19]} ... {record[8]}"
            line_l2 = f"{record[20]} ... {record[9]}"
            line_W = f"{record[21]} ... {record[10]}"
            line_R1 = f"{record[22]} ... {record[11]}"
            line_Dp = f"Ø {record[23]} ... {record[12]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_W,line_R1,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(11):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
                
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=680)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=245)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=310)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=167)#tb
            sz_lbl[4].place(anchor= 'nw',    x=480,     y=430)#J
            sz_lbl[5].place(anchor= 'nw',    x=600,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=560)#l1
            sz_lbl[7].place(anchor= 'nw',    x=55,      y=480)#l2
            sz_lbl[8].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[9].place(anchor='nw',    x=55,      y=850)#R1
            sz_lbl[10].place(anchor='nw',    x=760,      y=480)#Dp
        case 'conltr':
            global conltr_img_rnd
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0', highlightthickness=0)
            canvas.background = conltr_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=conltr_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT * from connectors_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','W','R1','Dp31']
            
            line_d1 = f"Ø {record[13]} ... {record[2]}"
            line_d2 = f"Ø {record[14]} ... {record[3]}"
            line_t = f"{record[15]} ... {record[4]}"
            line_tb = f"{record[16]} ... {record[5]}"
            line_J = f"{record[17]} ... {record[6]}"
            line_L = f"{record[18]} ... {record[7]}"
            line_l1 = f"{record[19]} ... {record[8]}"
            line_l2 = f"{record[20]} ... {record[9]}"
            line_W = f"{record[21]} ... {record[10]}"
            line_R1 = f"{record[22]} ... {record[11]}"
            line_Dp = f"Ø {record[23]} ... {record[12]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_W,line_R1,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(11):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
                
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=680)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=245)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=310)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=167)#tb
            sz_lbl[5].place(anchor= 'nw',    x=620,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=560)#l1
            sz_lbl[7].place(anchor= 'nw',    x=55,      y=480)#l2
            sz_lbl[8].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[9].place(anchor='nw',    x=55,      y=850)#R1
            sz_lbl[10].place(anchor='nw',    x=750,      y=480)#Dp
        case 'conlo':
            global conlo_img_rnd
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0',highlightthickness=0)
            canvas.background = conlo_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=conlo_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT * from connectors_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','W','R1','Dp31']
            
            line_d1 = f"Ø {record[13]} ... {record[2]}"
            line_d2 = f"Ø {record[14]} ... {record[3]}"
            line_t = f"{record[15]} ... {record[4]}"
            line_tb = f"{record[16]} ... {record[5]}"
            line_J = f"{record[17]} ... {record[6]}"
            line_L = f"{record[18]} ... {record[7]}"
            line_l1 = f"{record[19]} ... {record[8]}"
            line_l2 = f"{record[20]} ... {record[9]}"
            line_W = f"{record[21]} ... {record[10]}"
            line_R1 = f"{record[22]} ... {record[11]} x 45°"
            line_Dp = f"Ø {record[23]} ... {record[12]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_W,line_R1,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(11):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
                
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=680)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=245)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=310)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=167)#tb
            sz_lbl[4].place(anchor= 'nw',    x=500,     y=430)#J
            sz_lbl[5].place(anchor= 'nw',    x=650,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=560)#l1
            sz_lbl[8].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[9].place(anchor='nw',    x=55,      y=850)#R1
            sz_lbl[10].place(anchor='nw',    x=780,      y=480)#Dp
        case 'conv':
            global conv_img_rnd           
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0', highlightthickness=0)
            canvas.background = conv_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=conv_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT * from connectors_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','W','R1','Dp31']
            
            line_d1 = f"Ø {record[13]} ... {record[2]}"
            line_d2 = f"Ø {record[14]} ... {record[3]}"
            line_t = f"{record[15]} ... {record[4]}"
            line_tb = f"{record[16]} ... {record[5]}"
            line_J = f"{record[17]} ... {record[6]}"
            line_L = f"{record[18]} ... {record[7]}"
            line_l1 = f"{record[19]} ... {record[8]}"
            line_l2 = f"{record[20]} ... {record[9]}"
            line_W = f"{record[21]} ... {record[10]}"
            line_R1 = f"{record[22]} ... {record[11]}"
            line_Dp = f"Ø {record[23]} ... {record[12]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_W,line_R1,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(11):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
                
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=680)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=245)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=320)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=167)#tb
            sz_lbl[4].place(anchor= 'nw',    x=470,     y=430)#J
            sz_lbl[5].place(anchor= 'nw',    x=620,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=560)#l1
            sz_lbl[7].place(anchor= 'nw',    x=55,      y=480)#l2
            sz_lbl[8].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[9].place(anchor='nw',    x=55,      y=830)#R1
            sz_lbl[10].place(anchor='nw',    x=860,      y=480)#Dp
        case 'cons':
            global cons_img_rnd
            canvas = Canvas(frame_6, width=1920, height=1080, background='#f0f0f0', highlightthickness=0)
            canvas.background = cons_img_rnd
            canvas.create_image(50, 100, anchor=NW, image=cons_img_rnd)
            canvas.place(x=500, y=0)
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                #print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT * from connectors_max_min where part_name = ?"""
                cursor.execute(sql_fetch_blob_query, (part_name, )) 
                record = cursor.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                pass
                #print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    #print("Действие завершено. Соединение с SQLite закрыто")
                    #print(f"{record}")
            parameters = ['d1','d2','t','tb','J','L','l1','l2','W','R1','Dp31']
            
            line_d1 = f"Ø {record[13]} ... {record[2]}"
            line_d2 = f"Ø {record[14]} ... {record[3]}"
            line_t = f"{record[15]} ... {record[4]}"
            line_tb = f"{record[16]} ... {record[5]}"
            line_J = f"{record[17]} ... {record[6]}"
            line_L = f"{record[18]} ... {record[7]}"
            line_l1 = f"{record[19]} ... {record[8]}"
            line_l2 = f"{record[20]} ... {record[9]}"
            line_W = f"{record[21]} ... {record[10]}"
            line_R1 = f"{record[22]} ... {record[11]}"
            line_Dp = f"Ø {record[23]} ... {record[12]}"
            lines = [line_d1,line_d2,line_t,line_tb,line_J,line_L,line_l1,line_l2,line_W,line_R1,line_Dp]
            sz_lbl = [f'sz_{i}' for i in parameters]
            for i in range(11):
                sz_lbl[i] = Label(canvas, text=lines[i], justify='left', 
                                                 font='Helvetica 24 italic', background='#f0f0f0')
                
            sz_lbl[0].place(anchor= 'nw',    x=55,      y=680)#d1
            sz_lbl[1].place(anchor= 'nw',    x=55,      y=245)#d2
            sz_lbl[2].place(anchor= 'nw',    x=55,      y=320)#t
            sz_lbl[3].place(anchor= 'nw',    x=55,      y=167)#tb
            sz_lbl[4].place(anchor= 'nw',    x=470,     y=430)#J
            sz_lbl[5].place(anchor= 'nw',    x=620,     y=940)#L
            sz_lbl[6].place(anchor= 'nw',    x=55,      y=560)#l1
            sz_lbl[7].place(anchor= 'nw',    x=55,      y=480)#l2
            sz_lbl[8].place(anchor= 'nw',    x=55,      y=75)#W
            sz_lbl[9].place(anchor='nw',    x=55,      y=830)#R1
            sz_lbl[10].place(anchor='nw',    x=860,      y=480)#Dp                   



def pics_to_main():
    frame_6.place_forget()
    gc.collect()
    frame_0.place(x=0, y=0)
    navi_frame()


def main_to_tab(dt,parttype):
    frame_0.place_forget()
    for widget in frame_7.winfo_children():
        widget.destroy()
    for widget in frame_77.winfo_children():
        widget.destroy()
    match parttype:
        case 'lug':
            frame_7.place(x=0, y=0) 
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")

                sql_fetch_blob_query = """SELECT mach, Fio, Date, Time,
                 name,d1,d2,t,tb,J,L,l1,l2,l4,W,D,B,S,R1,R2,Dp31,Dp32 FROM lugs_results WHERE Date = ? ORDER BY name"""
                cursor.execute(sql_fetch_blob_query, (dt, )) 
                record = cursor.fetchall()
                print(record)
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Действие завершено. Соединение с SQLite закрыто")
                tab_style = ttk.Style()
                tab_style.configure("Custom.Treeview.Heading", font=('Helvetica bold', 15))
                tab_style.configure("Custom.Treeview", rowheight=40, font=('Helvetica bold', 15))
                tab_style.map("Custom.Treeview.Cell", foreground=[('selected', 'white')], background=[('selected', 'blue')])
                columns = ("mach", "fio", "date", "time", "name",
                           "d1","d2","t","tb","J","L","l1","l2",
                           "l4","W","D","B","S","R1","R2","Dp31",
                           "Dp32")
                tree_lug = ttk.Treeview(frame_7, columns=columns, show="headings",
                                        height=22, style="Custom.Treeview")
                
                tree_lug.column(columns[0], width=80, anchor=CENTER)
                tree_lug.column(columns[1], width=135, anchor=CENTER)
                tree_lug.column(columns[2], width=135, anchor=CENTER)
                tree_lug.column(columns[3], width=115, anchor=CENTER)
                tree_lug.column(columns[4], width=140, anchor=CENTER)
                tree_lug.column(columns[5], width=75, anchor=CENTER)
                tree_lug.column(columns[6], width=75, anchor=CENTER)
                tree_lug.column(columns[7], width=75, anchor=CENTER)
                tree_lug.column(columns[8], width=75, anchor=CENTER)
                tree_lug.column(columns[9], width=75, anchor=CENTER)
                tree_lug.column(columns[10], width=75, anchor=CENTER)
                tree_lug.column(columns[11], width=75, anchor=CENTER)
                tree_lug.column(columns[12], width=75, anchor=CENTER)
                tree_lug.column(columns[13], width=75, anchor=CENTER)
                tree_lug.column(columns[14], width=75, anchor=CENTER)
                tree_lug.column(columns[15], width=75, anchor=CENTER)
                tree_lug.column(columns[16], width=75, anchor=CENTER)
                tree_lug.column(columns[17], width=75, anchor=CENTER)
                tree_lug.column(columns[18], width=75, anchor=CENTER)
                tree_lug.column(columns[19], width=75, anchor=CENTER)
                tree_lug.column(columns[20], width=75, anchor=CENTER)
                tree_lug.column(columns[21], width=75, anchor=CENTER)
                tree_lug.heading("mach", text="Станок")
                tree_lug.heading("fio", text="Фамилия")
                tree_lug.heading("date", text="Дата")
                tree_lug.heading("time", text="Время")
                tree_lug.heading("name", text="Корпус")
                tree_lug.heading("d1", text="d1")
                tree_lug.heading("d2", text="d2")
                tree_lug.heading("t", text="t")
                tree_lug.heading("tb", text="tb")
                tree_lug.heading("J", text="J")
                tree_lug.heading("L", text="L")
                tree_lug.heading("l1", text="l1")
                tree_lug.heading("l2", text="l2")
                tree_lug.heading("l4", text="l4")
                tree_lug.heading("W", text="W")
                tree_lug.heading("D", text="D")
                tree_lug.heading("B", text="B")
                tree_lug.heading("S", text="S")
                tree_lug.heading("R1", text="R1")
                tree_lug.heading("R2", text="R2")
                tree_lug.heading("Dp31", text="Dp31")
                tree_lug.heading("Dp32", text="Dp32")
                #scrollbar = Scrollbar(size_checking_frame_20, orient="vertical", command=tree_lug.yview)
                #scrollbar.place(x=1840, y=90, height=786)
                #tree_lug.configure(yscrollcommand=scrollbar.set)
                btn_tab_to_main = ttk.Button(frame_7,
                                             style='my.TButton',
                                             text="В главное меню",
                                            command=lambda: tab_to_main())
                btn_tab_to_main.place(anchor="nw", x=10, y=10)
                for record in record:
                    tree_lug.insert("", END, values=record)
                tree_lug.place(x=10, y=90)
        case 'con':
            frame_77.place(x=0, y=0) 
            try:
                sqlite_connection = sqlite3.connect('main.db')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                sql_fetch_blob_query = """SELECT mach, Fio, Date, Time,
                 part_name,d1,L,d21,t1,tb1,J1,l11,l21,W1,R11,Dp31,d22,t2,tb2,J2,l12,l22,W2,R12,Dp32 FROM connectors_results WHERE Date = ? ORDER BY part_name ASC"""
                cursor.execute(sql_fetch_blob_query, (dt, )) 
                records = cursor.fetchall()
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Действие завершено. Соединение с SQLite закрыто")
                tab_style = ttk.Style()
                tab_style.configure("Custom.Treeview.Heading", font=('Helvetica bold', 16))
                tab_style.configure("Custom.Treeview", rowheight=40, font=('Helvetica bold', 15))
                tab_style.map("Custom.Treeview.Cell", foreground=[('selected', 'white')], background=[('selected', 'blue')])
                columns = ("mach", "fio", "date", "time", "part_name", "d1","L","d21","t1","tb1","J1","l11","l21","W1",
                           "R11","Dp31","d22","t2","tb2","J2","l12","l22","W2","R12","Dp32")
                tree_con = ttk.Treeview(frame_77, columns=columns, show="headings",
                                        height=22, style="Custom.Treeview")
                tree_con.column(columns[0], width=85, anchor=CENTER)
                tree_con.column(columns[1], width=130, anchor=CENTER)
                tree_con.column(columns[2], width=130, anchor=CENTER)
                tree_con.column(columns[3], width=110, anchor=CENTER)
                tree_con.column(columns[4], width=135, anchor=CENTER)
                tree_con.column(columns[5], width=65, anchor=CENTER)
                tree_con.column(columns[6], width=65, anchor=CENTER)
                tree_con.column(columns[7], width=65, anchor=CENTER)
                tree_con.column(columns[8], width=65, anchor=CENTER)
                tree_con.column(columns[9], width=65, anchor=CENTER)
                tree_con.column(columns[10], width=65, anchor=CENTER)
                tree_con.column(columns[11], width=65, anchor=CENTER)
                tree_con.column(columns[12], width=65, anchor=CENTER)
                tree_con.column(columns[13], width=65, anchor=CENTER)
                tree_con.column(columns[14], width=65, anchor=CENTER)
                tree_con.column(columns[15], width=65, anchor=CENTER)
                tree_con.column(columns[16], width=65, anchor=CENTER)
                tree_con.column(columns[17], width=65, anchor=CENTER)
                tree_con.column(columns[18], width=65, anchor=CENTER)
                tree_con.column(columns[19], width=65, anchor=CENTER)
                tree_con.column(columns[20], width=65, anchor=CENTER)
                tree_con.column(columns[21], width=65, anchor=CENTER)
                tree_con.column(columns[22], width=65, anchor=CENTER)
                tree_con.column(columns[23], width=65, anchor=CENTER)
                tree_con.column(columns[24], width=65, anchor=CENTER)
                tree_con.heading("mach", text="Станок")
                tree_con.heading("fio", text="Фамилия")
                tree_con.heading("date", text="Дата")
                tree_con.heading("time", text="Время")
                tree_con.heading("part_name", text="Корпус")
                tree_con.heading("d1", text="d1")
                tree_con.heading("L", text="L")
                tree_con.heading("d21", text="d2")
                tree_con.heading("t1", text="t")
                tree_con.heading("tb1", text="T")
                tree_con.heading("J1", text="J")
                tree_con.heading("l11", text="l1")
                tree_con.heading("l21", text="l2")
                tree_con.heading("W1", text="W")
                tree_con.heading("R11", text="R1")
                tree_con.heading("Dp31", text="Dp3")
                tree_con.heading("d22", text="d2")
                tree_con.heading("t2", text="t")
                tree_con.heading("tb2", text="T")
                tree_con.heading("J2", text="J")
                tree_con.heading("l12", text="l1")
                tree_con.heading("l22", text="l2")
                tree_con.heading("W2", text="W")
                tree_con.heading("R12", text="R1")
                tree_con.heading("Dp32", text="Dp3")
                #scrollbar = Scrollbar(size_checking_frame_201, orient="vertical", command=tree_con.yview)
                #scrollbar.place(x=1850, y=90, height=786)
                #tree_con.configure(yscrollcommand=scrollbar.set)
                btn_tab_to_main = ttk.Button(frame_77,
                                             style='my.TButton',
                                             text="В главное меню",
                                            command=lambda: tab_to_main())
                btn_tab_to_main.place(anchor="nw", x=10, y=10)
                for record in records:
                    tree_con.insert("", END, values=record)
                tree_con.place(x=10, y=90)


def tab_to_main():
    frame_7.place_forget()
    frame_77.place_forget()
    frame_0.place(x=0, y=0)
    navi_frame()
    
root.mainloop()