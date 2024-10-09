import tkinter
from tkinter import *

from tkcalendar import DateEntry

def get_request():
    base = Tk()
    base.geometry("500x500")
    base.configure(background='pink')
    base.title("request form")
    name = StringVar()
    phone = StringVar()
    day = StringVar()
    hours = StringVar()
    city = StringVar()
    comment = StringVar()
    list = []

    lb = Label(base, text="Babysitting Request Form", width=25, font=("arial", 20), background='pink')
    lb.place(x=50, y=15)

    lb1 = Label(base, text="Name", width=13, font=("arial", 12), background='pink')
    lb1.place(x=20, y=60)
    en1 = Entry(base)
    en1.place(x=200, y=60)
    name = en1.get()

    # lb3 = Label(base, text="Enter Email", width=10, font=("arial", 12))
    # lb3.place(x=19, y=160)
    # en3 = Entry(base)
    # en3.place(x=200, y=160)

    lb3 = Label(base, text="Contact Number", width=13, font=("arial", 12), background='pink')
    lb3.place(x=19, y=100)
    en3 = Entry(base)
    en3.place(x=200, y=100)
    phone.set(en3.get())

    def get_selected_date():
        selected_date = en4.get_date()
        return selected_date

    lb4 = Label(base, text="date", width=13, font=("arial", 12), background='pink')
    lb4.place(x=19, y=140)
    en4 = DateEntry(base, width=12, background="darkblue", foreground="white", borderwidth=2)
    en4.pack(padx=10, pady=10)
    en4.place(x=200, y=140)
    date = get_selected_date()

    # lb4 = Label(base, text="date", width=13, font=("arial", 12))
    # lb4.place(x=19, y=140)
    # en4 = Entry(base)
    # en4.place(x=200, y=140)

    # lb5 = Label(base, text="Select Gender", width=15, font=("arial", 12))
    # lb5.place(x=5, y=240)
    # vars = IntVar()
    # Radiobutton(base, text="Male", padx=5, variable=vars, value=1).place(x=180, y=240)
    # Radiobutton(base, text="Female", padx=10, variable=vars, value=2).place(x=240, y=240)
    # Radiobutton(base, text="others", padx=15, variable=vars, value=3).place(x=310, y=240)

    list_of_day = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    cv = StringVar()
    drplist = OptionMenu(base, cv, *list_of_day)
    drplist.config(width=15)
    cv.set("Sunday")
    lb2 = Label(base, text="Select day", width=13, font=("arial", 12), background='pink')
    lb2.place(x=14, y=180)
    drplist.place(x=195, y=180)
    day.set(cv.get())

    lb6 = Label(base, text="hours", width=13, font=("arial", 12), background='pink')
    lb6.place(x=19, y=230)
    en6 = Entry(base)
    en6.place(x=200, y=230)
    hours.set(en6.get())

    lb7 = Label(base, text="city     ", width=15, font=("arial", 12), background='pink')
    lb7.place(x=21, y=270)
    en7 = Entry(base)
    en7.place(x=200, y=270)
    city.set(en7.get())

    lb8 = Label(base, text="comment", width=15, font=("arial", 12), background='pink')
    lb8.place(x=15, y=310)
    en8 = tkinter.Text(base, width=25, height=4)
    en8.place(x=200, y=310)
    comment.set(en8.get("1.0", 'end-1c'))

    def get_into_list():
        array = [name, phone, date, day, hours, city, comment]
        print(array)

    def clicked():
        get_into_list()

    Button(base, text="Register", width=10, command=clicked).place(x=200, y=400)

    base.mainloop()

get_request()