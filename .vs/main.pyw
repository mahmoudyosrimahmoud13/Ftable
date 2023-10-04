from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector


#Time
now = datetime.now()

# Database:
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="121212",
    database="Ftable"
)
mycursor = db.cursor()



# Windows:
def main():
    main = Toplevel()
    main.geometry("700x600")
    main.title("F table")
    main.configure(background=color)
    main.iconphoto(False, logo)
    main.resizable(False,False)
    global prand_im

    prand_img = PhotoImage(file="prand.png")
    prand = Label(main, image=prand_img,background=color).place(x=200, y=10)

    frame1 = Frame(main, bg="#CBCBCB", width=680, height=100).place(x=10, y=180)

    user = username_value.get()
    admin_name = f"admin: {user}"
    admin = Label(main, frame1, text=admin_name, font="Bahnschrift 13", bg="#CBCBCB", fg="#ff7b1a").place(x=10, y=190)

    mycursor.execute(F"SELECT id FROM admin WHERE username = '{user}'")
    id = mycursor.fetchone()


    id_num = F"id: {id[0]}"
    id = Label(main, frame1, text=id_num, font="Bahnschrift 13", bg="#CBCBCB", fg="#ff7b1a").place(x=10, y=235)

    day_name = strftime("Day: %A")
    day = Label(main, frame1, text=day_name, font="Bahnschrift 13", bg="#CBCBCB", fg="#ff7b1a").place(x=500, y=190)

    date_num = strftime("Date: %D")
    date = Label(main, frame1, text=date_num, font="Bahnschrift 13", bg="#CBCBCB", fg="#ff7b1a").place(x=500, y=235)

    frame2 = Frame(main, bg="#D2D2D2", width=680, height=240).place(x=10, y=290)

    agent = Label(main, frame2, text="Agent Data", bg="#D2D2D2", font="Bahnschrift 18", fg="#732588").place(x=10, y=300)

    agent_name_value = StringVar()
    id_value = IntVar()

    agent_name = Label(main, text="Agent username", background="#D2D2D2", foreground="#ff7b1a", font="Bahnschrift 13", )
    agent_name.place(x=10, y=370)
    agent_name_entry = ttk.Entry(main, textvariable=agent_name_value)
    agent_name_entry.place(x=150, y=373)
    id_label = Label(main, frame2, text="Agent ID", bg="#D2D2D2", font="Bahnschrift 13", fg="#ff7b1a")
    id_label.place(x=10, y=400)
    id_entry = ttk.Entry(main, textvariable=id_value)
    id_entry.place(x=150, y=403)

    error = Label(main,frame2,text='', bg="#D2D2D2", font="Bahnschrift 13", fg="red")
    error.place(x=150,y=443)

    def enter():
        user = agent_name_value.get()
        id = id_value.get()
        try:
            mycursor.execute(f"SELECT id FROM agent WHERE username = '{user}'")
            if id == int(mycursor.fetchone()[0]):
                error.destroy()
                agent_name.destroy()
                agent_name_entry.destroy()
                id_label.destroy()
                id_entry.destroy()
                enter_btn.destroy()
                add_btn.destroy()
                confirm_btn_1.destroy()

                user_name_agent_value = "Username: " + agent_name_value.get()
                id_agent_value = "ID: " + str(id_value.get())

                # Meals and drinks Lists:
                mycursor.execute("SELECT lunch_meal FROM menu")
                list_luanch_meals = mycursor.fetchall()
                mycursor.execute("SELECT lunch_drink FROM menu ")
                list_luanch_drinks = mycursor.fetchall()
                mycursor.execute("SELECT breakfast_meal FROM menu ")
                list_breakfast_meals = mycursor.fetchall()
                mycursor.execute("SELECT breakfast_drink FROM menu ")
                list_breakfast_drinks = mycursor.fetchall()

                #Day list:
                day_list_value = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']


                #Window:
                user_name_agent = Label(main, text=user_name_agent_value, background="#D2D2D2", foreground="blue",
                                        font="Bahnschrift 10", )
                user_name_agent.place(x=10, y=335)
                id_agent = Label(main, text=str(id_agent_value), background="#D2D2D2", foreground="blue",
                                 font="Bahnschrift 10", )
                id_agent.place(x=500, y=335)

                launch = Label(main, frame2, text="Launch: ", bg="#D2D2D2", font="Bahnschrift 13", fg="#ff7b1a")
                launch.place(x=10, y=360)

                meal_1 = Label(main, frame2, text="Mael", bg="#D2D2D2", font="Bahnschrift 13 bold", fg="green")
                meal_1.place(x=10, y=390)
                list_l_m = ttk.Combobox(main, value=list_luanch_meals)
                list_l_m.place(x=75, y=395)
                list_l_m.set("Meal")

                drink_1 = Label(main, frame2, text="Drink", bg="#D2D2D2", font="Bahnschrift 13 bold", fg="green")
                drink_1.place(x=450, y=390)
                drink_l = ttk.Combobox(main, value=list_luanch_drinks)
                drink_l.place(x=500, y=395)
                drink_l.set("Drink")

                break_fast = Label(main, frame2, text="Breakfast: ", bg="#D2D2D2", font="Bahnschrift 13", fg="#ff7b1a")
                break_fast.place(x=10, y=430)

                meal_2 = Label(main, frame2, text="Mael", bg="#D2D2D2", font="Bahnschrift 13 bold", fg="green")
                meal_2.place(x=10, y=460)
                list_b_m = ttk.Combobox(main, value=list_breakfast_meals)
                list_b_m.place(x=75, y=465)
                list_b_m.set("Meal")

                drink_2 = Label(main, frame2, text="Drink", bg="#D2D2D2", font="Bahnschrift 13 bold", fg="green")
                drink_2.place(x=450, y=460)
                drink_b = ttk.Combobox(main, value=list_breakfast_drinks)
                drink_b.place(x=500, y=465)
                drink_b.set("Drink")


                day = Label(main, frame2, text="Day: ", bg="#D2D2D2", font="Bahnschrift 13", fg="green")
                day.place(x=250 , y=390)

                day_list = ttk.Combobox(main,values=day_list_value)
                day_list.place(x=250,y=420)
                day_list.set("Day")

            else:
                error.config(text='ID is not correct')

        except:
            error.config(text="Username or ID is wrong")


        def confirm():
            # lists variables :
            user = agent_name_value.get()
            launch_meal = list_l_m.get()
            luanch_drink = drink_l.get()
            breakfast_meal = list_b_m.get()
            breakfast_drink = drink_b.get()
            day = day_list.get()
            print(day)
            main.destroy()
            done()

        confirm_btn = ttk.Button(main, text="Confirm", command=confirm)
        confirm_btn.place(x=600, y=540)

    enter_btn = ttk.Button(main, text="Enter", command=enter)
    enter_btn.place(x=600, y=490)

    add_btn = ttk.Button(main,text="Add",command=add)
    add_btn.place(x=600,y=465)

    def quit_main():
        main.destroy()

    confirm_btn_1 = ttk.Button(main, text="Confirm", state=DISABLED)
    confirm_btn_1.place(x=600, y=540)

    quit_btn_main = ttk.Button(main, text="Quit", command=quit_main).place(x=600, y=567)

    info = ttk.Button(main, text="User info", command=user_info).place(x=20, y=540)

    search = ttk.Button(main,text="Search",command = search_win).place(x=20 ,y=567)

    main.mainloop()

def add ():
   add = Toplevel()
   add.geometry("420x130")
   add.title("Add a new agent")
   add.configure(background=color)
   add.iconphoto(False,logo)
   add.resizable(False,False)



   agent_user = StringVar()
   agent_phone = IntVar()

   def add_button_command():
       empty = ""
       try:
           if agent_user.get() == empty:
               error.config(text="Agent username cannot be empty")
           else:
               sql = "INSERT INTO agent (username,phone) VALUES(%s,%s)"
               data = (agent_user.get(), str(agent_phone.get()))
               mycursor.execute(sql, data)
               db.commit()

               add.destroy()
               done()
       except:
           error.config(text="Something went wrong")



   label = Label(add,text="Adding a new agent", fg="#732588", font="Bauhaus93 16 bold",padx=60,bg=color)
   label.place(x=50,y=10)
   agent_user_label = Label(add,text="user: ", fg="#ff7b1a", font="Bauhaus93 13 bold",bg=color)
   agent_user_label.place(x=10,y=45)
   agent_user_entry = ttk.Entry(add,textvariable=agent_user)
   agent_user_entry.place(x=70,y=45)

   agent_phone_label = Label(add, text="phone: ", fg="#ff7b1a", font="Bauhaus93 13 bold",bg=color)
   agent_phone_label.place(x=10,y=75)
   agent_phone_entry = ttk.Entry(add, textvariable=agent_phone)
   agent_phone_entry.place(x=70,y=75)

   error = Label(add, text="",fg="red", font="Bauhaus93 10 ",bg=color)
   error.place(x=10 , y=95)

   add_button = ttk.Button(add,text="Add",command=add_button_command)
   add_button.place(x=320,y=90)

   add.mainloop()

def user_info():
    user_info = Toplevel()
    user_info.geometry("500x500")
    user_info.title("User information")
    user_info.configure(background=color)
    user_info.iconphoto(False, logo)
    user_info.resizable(False,False)




    tabs = ttk.Notebook(user_info)
    tabs.pack()

    agent_info_tab = Frame(user_info, width=500, height=500, background="#cccccc",bg=color)
    admin_info_tab = Frame(user_info, width=500, height=500, background="#cccccc",bg=color)
    data_tab = Frame(user_info, width=500, height=500, background="#cccccc",bg=color)


    # Menu:
    menue_tab = Frame(user_info, width=500, height=500, background="#cccccc",bg=color)

    #breakfast meals:
    mycursor.execute("SELECT breakfast_meal FROM menu")
    breakfast_meal_label = Label(menue_tab, text="Breakfast meals:", background="#cccccc", foreground="#732588",
                         font="Bauhaus93 14 bold",bg=color).pack()
    for item in mycursor.fetchall():
        none = "None"
        if str(item[0]) != none:
            item_label = Label(menue_tab, text=str(item[0]), background="#cccccc", font="Bauhaus93 11 bold",
                              foreground="#ff7b1a",bg=color).pack()

    #breakfast drinks:
    mycursor.execute("SELECT breakfast_drink FROM menu")
    breakfast_drinks_label = Label(menue_tab, text="Breakfast drinks:", background="#cccccc", foreground="#732588",
                                 font="Bauhaus93 14 bold",bg=color).pack()
    for item in mycursor.fetchall():
        none = "None"
        if str(item[0]) != none:
            item_label = Label(menue_tab, text=str(item[0]), background="#cccccc", font="Bauhaus93 11 bold",
                              foreground="#ff7b1a",bg=color).pack()

    # lunch meals:
    mycursor.execute("SELECT lunch_meal FROM menu")
    lunch_meal_label = Label(menue_tab, text="Lunch meals:", background="#cccccc", foreground="#732588",
                                       font="Bauhaus93 14 bold",bg=color).pack()
    for item in mycursor.fetchall():
        none = "None"
        if str(item[0]) != none:
            item_label = Label(menue_tab, text=str(item[0]), background="#cccccc", font="Bauhaus93 11 bold",
                               foreground="#ff7b1a",bg=color).pack()

    # lunch drinks:
    mycursor.execute("SELECT lunch_drink FROM menu")
    lunch_drinks_label = Label(menue_tab, text="Lunch drinks:", background="#cccccc", foreground="#732588",
                                       font="Bauhaus93 14 bold",bg=color).pack()
    for item in mycursor.fetchall():
        none = "None"
        if str(item[0]) != none:
            item_label = Label(menue_tab, text=str(item[0]), background="#cccccc", font="Bauhaus93 11 bold",
                               foreground="#ff7b1a",bg=color).pack()


    # history_log
    history_log = Frame(user_info, width=500, height=500, background="#cccccc",bg=color)

    #login
    log_in_label = Label(history_log,text="Login history:", background="#cccccc", foreground="#732588", font="Bauhaus93 16 bold",bg=color).pack()
    table_login = ttk.Treeview(history_log)
    table_login.heading('#0', text='Login')
    table_login.column('#0', anchor=CENTER, width=400)

    mycursor.execute("SELECT login FROM history_log")
    id = 0
    for log in mycursor.fetchall():
        if str(log[0]) != 'None':
            table_login.insert(parent='', index=id, iid=id, text=log)
            id += 1
    table_login.pack()
    scale_login = ttk.Scrollbar(history_log,orient='vertical', command=table_login.yview).place(x=25, y=30, height=230)

    #logout
    log_out_label = Label(history_log,text="Logout history:", background="#cccccc", foreground="#732588", font="Bauhaus93 16 bold",bg=color).pack()
    table_logout = ttk.Treeview(history_log)
    table_logout.heading('#0', text='Logout')
    table_logout.column('#0', anchor=CENTER, width=400)

    mycursor.execute("SELECT logout FROM history_log")
    id = 0
    for log in mycursor.fetchall():
        if str(log[0]) != 'None':
            table_logout.insert(parent='', index=id, iid=id, text=log)
            id += 1
    table_logout.pack()
    scale_logout= ttk.Scrollbar(history_log, orient='vertical', command=table_logout.yview).place(x=25, y=290, height=180)




    tabs.add(menue_tab, text="Menu")
    tabs.add(agent_info_tab, text="Agent Info")
    tabs.add(admin_info_tab, text="Admin Info")
    tabs.add(history_log,text="History log")
    tabs.add(data_tab,text="Data")


    user_info.mainloop()

def search_win ():
    search = Toplevel()
    search.title("Search")
    search.geometry("500x500")
    search.configure(background=color)
    search.iconphoto(False,logo)
    search.resizable(False,False)

    search_img = PhotoImage(file="seaech.png")
    search_box = StringVar()

    def search_commdand():
        print("hi")


    search_label = Label(search,text="Search: ", fg="#ff7b1a", font="Bauhaus93 13 bold",bg=color).place(x=5,y=10)
    search_box_entry = ttk.Entry(search,textvariable=search_box,width=75)
    search_box_entry.place(x=5 , y=30)
    search_button = ttk.Button(search,cursor="hand2",image=search_img,command=search_commdand)
    search_button.place(x=465,y=30)



    search.mainloop()

def done():
    messagebox.showinfo("F table", "Done")

def information():
    information = Toplevel()
    information.title("Information")
    information.configure(background=color)
    information.iconphoto(False, i_icon)
    information.resizable(False,False)
    global information_img
    information_img = PhotoImage(file="information_img.png")
    image = Label(information, image=information_img,bg=color).pack()
    Label(information, text="(Nutrition application for student house):", font="Bauhaus93 18 bold", fg="#732588",bg=color).pack(
        pady=5)
    information_l = Label(information, fg="#ff7b1a",
                          text="application that helps the officials with the right confirmation and automation the registration of \nthe students With avoiding the human error and save the food amount without\n any wasting in the resources and budget",
                          font="18",bg=color)
    information_l.pack(padx=10, pady=15)


def sign_in():
    sign_in = Toplevel()
    sign_in.geometry("500x290")
    sign_in.title("Sign_up")
    sign_in.configure(background=color)
    Label(sign_in, text="Sign in", font="Berlin 20 bold", fg="#732588",bg=color).grid(row=0, column=3)
    sign_in.iconphoto(False, logo)
    sign_in.resizable(False,False)


    firistname_value = StringVar()
    lastname_value = StringVar()
    user_name_value = StringVar()
    emergancy_value = IntVar()
    phone_number_value = IntVar()
    password_sign_value = StringVar()
    password_c_sign_value = StringVar()
    gender_value = BooleanVar()
    gender = ''

    get_value = BooleanVar()

    firstname = Label(sign_in, text="First name", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=1, column=3)
    fristname_entry = ttk.Entry(sign_in, textvariable=firistname_value).grid(row=1, column=4)

    lastname = Label(sign_in, text="last name", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=3, column=3)
    lastname_entry = ttk.Entry(sign_in, textvariable=lastname_value).grid(row=3, column=4)

    user_name = Label(sign_in, text="Username", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=5, column=3)
    user_name_entry = ttk.Entry(sign_in, textvariable=user_name_value).grid(row=5, column=4)

    emergancy = Label(sign_in, text="Emergancy number", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=7, column=3)
    fristname_entry = ttk.Entry(sign_in, textvariable=emergancy_value).grid(row=7, column=4)

    phone_number = Label(sign_in, text="phone number", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=9, column=3)
    fristname_entry = ttk.Entry(sign_in, textvariable=phone_number_value).grid(row=9, column=4)

    password_sign = Label(sign_in, text="Password:", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=11, column=3)
    password_entry_sign = ttk.Entry(sign_in, textvariable=password_sign_value, show="*").grid(row=11, column=4)

    password_c_sign = Label(sign_in, text="Confirm your password:", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=13,
                                                                                                             column=3)
    password_c_entry_sign = ttk.Entry(sign_in, textvariable=password_c_sign_value, show="*").grid(row=13, column=4)

    gender = Label(sign_in, text="Gender:", fg="#ff7b1a", font="Bauhaus93 13 ",bg=color).grid(row=14, column=3)
    male = ttk.Radiobutton(sign_in, text="Male", value=TRUE).place(x=180, y=215)
    female = ttk.Radiobutton(sign_in, text="Female", value=False).place(x=240, y=215)
    if gender_value ==TRUE:gender = 'Male'
    else:gender='Female'
    chekbox = ttk.Checkbutton(sign_in, text="Remember me?", variable=get_value).grid(row=15, column=4)

    reg_img = PhotoImage(file="reg.png")
    reg_img_label = Label(sign_in, image=reg_img,bg=color).place(x=300, y=-85)

    error = Label(sign_in,text="", fg="red", font="Bauhaus93 10 ",bg=color)
    error.place(x=320, y=240)

    def submet ():
        password = password_c_sign_value.get()

        if password_c_sign_value.get() != password_sign_value.get():
            error.config(text="password not match")
        elif len(password) < 8 :
            error.config(text="Your password is too short")
        else:
            sql = "INSERT INTO admin (firistname,lastname,emergancy,phone,username,password,gender) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            data = (firistname_value.get(), lastname_value.get(), emergancy_value.get(), phone_number_value.get(),
                    user_name_value.get()
                    , password_c_sign_value.get(), str(gender))
            mycursor.execute(sql, data)
            db.commit()
            sign_in.destroy()
            done()



    submit = ttk.Button(sign_in, text="submit", cursor="hand2", command=submet).grid(row=16, column=4)


    sign_in.mainloop()


root = Tk()
root.geometry("300x520")
root.title("Wellcome")
logo = PhotoImage(file="logo.png")
root.iconphoto(False, logo)
root.resizable(False,False)

username_value = StringVar()
password_value = StringVar()
get_value = StringVar()
login_file = PhotoImage(file="login.png")
Label(root, text="Sign in", font="Berlin 20 bold", foreground="#732588").pack(pady=17)
login_img = Label(root, image=login_file, width=100, height=100).pack(pady=15)
username = Label(root, text="Username:", fg="#ff7b1a", font="Bauhaus93 13 bold").pack(pady=10)
username_entry = ttk.Entry(root, textvariable=username_value)
username_entry.pack()
password_entry_root = Label(root, text="Password:", fg="#ff7b1a", font="Bauhaus93 13 bold").pack(pady=10)
password_entry = ttk.Entry(root, textvariable=password_value, show="*")
password_entry.pack()
error = Label(root,text='', fg="red", font="Bauhaus93 8 ")
error.pack()

def login():
    user = username_value.get()
    password = password_value.get()
    date = str(now.date())
    time = str(now.time())
    try:
        mycursor.execute(F"SELECT password FROM admin WHERE username = '{user}'")
        password_db = ''.join(mycursor.fetchone())
        if password_db == password :
            username_entry.config(state=DISABLED)
            password_entry.config(state=DISABLED)
            error.destroy()
            chekbtn.destroy()
            sign_up_btn.destroy()
            root.geometry("300x400")
            quit_btn.place(x=220, y=360)
            login_btn.config(text="New")
            mycursor.execute(f"INSERT INTO history_log (login) VALUES ('{user} Log in at {date} in Time: {time}')")
            db.commit()
            main()
        else:
            error.config(text="Please enter the corecct password")

    except:
        error.config(text="username or password is wrong")





chekbtn = ttk.Checkbutton(root,text="Remember me?", variable=get_value,offvalue="off",onvalue="on")
chekbtn.pack()
login_btn = ttk.Button(root, text="Login", command=login, cursor="hand2")
login_btn.pack(pady=5)
sign_up_btn = ttk.Button(root, text="Sign up", command=sign_in, cursor="hand2")
sign_up_btn.pack(pady=10)


def quit_app():
    try:
        user = username_value.get()
        mycursor.execute(F"SELECT username FROM admin WHERE username = '{user}'")
        date = str(now.date())
        time = str(now.time())

        if user == ''.join(mycursor.fetchone()):
            mycursor.execute(f"INSERT INTO history_log (logout) VALUES ('{user} Log out at {date} in Time: {time}')")
            db.commit()
            root.destroy()
    except:
        root.destroy()



quit_btn = ttk.Button(text="Quit", command=quit_app)
quit_btn.place(x=220, y=480)

i_icon = PhotoImage(file="I.png")
information_btn = ttk.Button(root, image=i_icon, command=information, cursor="hand2").place(x=265, y=20)




#dark mode:
color = None
def dar_mode_off():
    dark_mode_btn.config(image=dark_mode_on_img,command=dark_mode_on)
    global color
    color =  None
    s = ttk.Style()
    s.configure(root, background='#f0f0f0')
def dark_mode_on():
    dark_mode_btn.config(image=dark_mode_off_img,command=dar_mode_off)
    global color
    color = "#444444"
    s = ttk.Style()
    s.configure(root, background=color)
dark_mode_on_img = PhotoImage(file="moon.png")
dark_mode_off_img = PhotoImage(file="sun.png")
dark_mode_btn = ttk.Button(root,image=dark_mode_on_img,command=dark_mode_on)
dark_mode_btn.place(x=265, y=50)
s = ttk.Style()
s.configure(root, background=color)




#Time & date
def time():
    clock = strftime("Date: %D\nTime: %I:%M %p")
    clock_text.config(text=clock)


clock_text = Label(root,font="Bauhaus93 8 bold")
clock_text.place(x=0, y=15)
clock_text.after(1000, time())
time()


root.mainloop()