import tkinter as tk
from tkinter import ttk
import os
import sys
from playsound import playsound
from datetime import datetime as dt
import csv

num = {0: "no_zero", 1: "no_one", 2: "no_two", 3: "no_three", 4: "no_four", 5: "no_five", 6: "no_six", 7: "no_seven",
       8: "no_eight", 9: "no_nine", 10: "no_10", 11: "no_11", 12: "no_12", 13: "no_13", 14: "no_14", 15: "no_15",
       16: "no_16", 17: "no_17", 18: "no_18", 19: "no_19", 20: "no_20", 21: "no_21", 22: "no_22", 23: "no_23",
       24: "no_24", 25: "no_25", 26: "no_26", 27: "no_27", 28: "no_28", 29: "no_29", 30: "no_30", 31: "no_31",
       32: "no_32", 33: "no_33", 34: "no_34", 35: "no_35", 36: "no_36", 37: "no_37", 38: "no_38", 39: "no_39",
       40: "no_40", 41: "no_41", 42: "no_42", 43: "no_43", 44: "no_44", 45: "no_45", 46: "no_46", 47: "no_47",
       48: "no_48", 49: "no_49", 50: "no_50", 51: "no_51", 52: "no_52", 53: "no_53", 54: "no_54", 55: "no_55",
       56: "no_56", 57: "no_57", 58: "no_58", 59: "no_59"}


def nothing():
    pass

def arrive_at():
    playsound(r"C:\\voice\\" + num[int(h)] + ".wav")
    playsound(r"C:\voice\time_hours.wav")

    playsound(r"C:\\voice\\" + num[int(m)] + ".wav")
    playsound(r"C:\voice\time_min.wav")

    playsound(r"C:\voice\on_pfno.wav")
    playsound(r"C:\\voice\\" + num[int(p)] + ".wav")


def leaving_at():
    playsound(r"C:\\voice\\" + num[int(h)] + ".wav")
    playsound(r"C:\voice\time_hours.wav")

    playsound(r"C:\\voice\\" + num[int(m)] + ".wav")
    playsound(r"C:\voice\time_min.wav")

    playsound(r"C:\voice\from_pfno.wav")
    playsound(r"C:\\voice\\" + num[int(p)] + ".wav")


def late_by():
    playsound(r"C:\\voice\\" + num[int(h)] + ".wav")
    playsound(r"C:\voice\time_hours.wav")

    playsound(r"C:\\voice\\" + num[int(m)] + ".wav")
    playsound(r"C:\voice\time_min.wav")


def has_left():
    playsound(r"C:\voice\wish_comfortable_happy_journey.wav")

def hin_arrive_at():
    playsound(r"C:\voice\hindi\train_is_arriving.wav")
    playsound(r"C:\voice\hindi\this_train.wav")

    playsound(r"C:\\voice\\hindi\\" + h +".wav")
    playsound(r"C:\voice\hindi\hour.wav")
    playsound(r"C:\\voice\\hindi\\" + m +".wav")
    playsound(r"C:\voice\hindi\minute.wav")
    playsound(r"C:\voice\hindi\per.wav")
    playsound(r"C:\voice\hindi\platform_no.wav")
    playsound(r"C:\\voice\\hindi\\" + p +".wav")
    playsound(r"C:\voice\hindi\will_arrive.wav")

def hin_late_by():
    if (h != 0):
        playsound(r"C:\\voice\\hindi\\" + h + ".wav")
        playsound(r"C:\voice\hindi\hours.wav")
    playsound(r"C:\\voice\\hindi\\" + m + ".wav")
    playsound(r"C:\voice\hindi\minute.wav")
    playsound(r"C:\voice\hindi\running_late.wav")
    playsound(r"C:\voice\hindi\regretted_inconvenience.wav")

def hin_leaving_at():
    playsound(r"C:\voice\hindi\leave_time.wav")
    playsound(r"C:\\voice\\hindi\\" + h + ".wav")
    playsound(r"C:\voice\hindi\hour.wav")
    playsound(r"C:\\voice\\hindi\\" + m + ".wav")
    playsound(r"C:\voice\hindi\minute.wav")
    playsound(r"C:\voice\hindi\per.wav")
    playsound(r"C:\voice\hindi\platform_no.wav")
    playsound(r"C:\\voice\\hindi\\" + p + ".wav")
    playsound(r"C:\voice\hindi\ready_to_leave.wav")

def hin_has_left():
    playsound(r"C:\voice\hindi\ja_chuki_hai.wav")

def hin_cancelled():
    playsound(r"C:\voice\hindi\cancelled.wav")

def announcement(tname, ttype, tto, tfrom, tnumber, time_type, hours,
                 minutes, platform, special_type, hindi, english):

    global  h, m, p
    h = hours
    m = minutes
    p = platform

    if (english == 1):
        playsound(r"C:\\voice\\kind_att_passengers.wav")
        playsound(r"C:\\voice\\trainno_voice1.wav")

        for i in tnumber:
            playsound(r"C:\\voice\\" + num[int(i)] + ".wav")

        playsound(r"C:\\voice\\TrainNames\\" + tname + ".wav")
        playsound(r"C:\\voice\\train_type\\" + ttype + ".wav")

        playsound(r"C:\\voice\\from.wav")
        playsound(r"C:\\voice\\StationNames\\" + tfrom + ".wav")

        playsound(r"C:\\voice\\to.wav")
        playsound(r"C:\\voice\\StationNames\\" + tto + ".wav")

        playsound(r"C:\\voice\\" + time_type + ".wav")
        switch = {"is_exp_to_arrive_at": arrive_at,
                  "is_running_late_by": late_by,
                  "is_sch_leave_at": leaving_at, "has_left": has_left, "has_been_cancelled_today" : nothing}
        switch[time_type]()
        if (special_type != "No special announcement"):
            playsound(r"C:\\voice\\special_messages\\English\\" + special_type + ".wav")

    if (hindi == 1):
        playsound(r"C:\voice\hindi\hin_kind_attn.wav")

        playsound(r"C:\\voice\\StationNames\\" + tfrom + ".wav")
        playsound(r"C:\voice\hindi\se_chalkar.wav")

        playsound(r"C:\\voice\\StationNames\\" + tto + ".wav")
        playsound(r"C:\voice\hindi\ko_jaane_waali.wav")

        playsound(r"C:\voice\hindi\train_name.wav")
        for i in tnumber:
            playsound(r"C:\\voice\\hindi\\" + i + ".wav")

        playsound(r"C:\\voice\\TrainNames\\" + tname + ".wav")
        playsound(r"C:\\voice\\train_type\\" + ttype + ".wav")

        switcher = {"is_exp_to_arrive_at": hin_arrive_at,
                  "is_running_late_by": hin_late_by,
                  "is_sch_leave_at": hin_leaving_at, "has_left": hin_has_left, "has_been_cancelled_today": hin_cancelled}
        switcher[time_type]()

        if (special_type != "No special announcement"):
            playsound(r"C:\\voice\\special_messages\\Hindi\\" + special_type + ".wav")

def name_error():
    os.startfile(r"C:\voice\TrainNames")
    os.startfile(r"C:\voice\Help.txt")


def type_error():
    os.startfile(r"C:\voice\train_type")
    os.startfile(r"C:\voice\Help.txt")


def station_error():
    os.startfile(r"C:\voice\StationNames")
    os.startfile(r"C:\voice\Help.txt")


def set_time(tname, ttype, tto, tfrom, tnumber):
    time = tk.Tk()
    time.title("Time?")
    time.geometry("480x600+400+80")

    style = ttk.Style()
    style.theme_use("clam")

    tk.Label(time, text=tname + " " + ttype + " from " + tfrom + " to " + tto, font="bold", bd=7, bg="white",
             width=480).pack()

    def jump_function():
        announcement(tname, ttype, tto, tfrom, tnumber, time_type.get(), hours.get(),
                     minutes.get(), platform.get(), special_type.get(), hindi.get(), english.get())

    def save():
        with open(r"C:\voice\data\save.csv", 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([tnumber, tname+" "+ttype, tfrom, tto, time_type.get(),hours.get(), minutes.get(), platform.get(), special_type.get(), "Play"])
            top = tk.Toplevel(time)
            top.title("Done")
            top.geometry("200x100+585+321")
            tk.Label(top, text = "Saved Successfully", bg = "Yellow", fg = "black", font = "bold").pack()
            top.resizable(0,0)
            top.mainloop()

    ann = tk.Label(time, text="Announcement Type", bg="blue", font="bold", fg="white", bd=5)
    ann.place(x=40, y=60)
    time_type = tk.StringVar()
    a_type = ttk.Combobox(time, width=25, textvariable=time_type)
    a_type['values'] = ["is_exp_to_arrive_at", "is_running_late_by", "is_sch_leave_at", "has_left",
                        "has_been_cancelled_today"]
    a_type.place(x=300, y=62)
    a_type.current(0)

    arr = tk.Label(time, text="Arriving at", bg="red", fg="white", width=12)
    arr.place(x=80, y=120)
    hours = tk.StringVar(time, name = "hours")
    hour = ttk.Combobox(time, textvariable=hours, width=5)
    hour['values'] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23']
    hour.place(x=300, y=122)
    hour_label = tk.Label(time, text="hours", fg="black")
    hour_label.place(x=370, y=122)
    hour.current()

    minutes = tk.StringVar(time, name = 'minutes')
    minute = ttk.Combobox(time, textvariable=minutes, width=5)
    minute['values'] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
                        '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48',
                        '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
    minute.place(x=300, y=162)
    min_label = tk.Label(time, text="min", fg="black")
    min_label.place(x=370, y=162)
    minute.current()

    plat = tk.Label(time, text="Enter Platform", bg="red", fg="white", width=12)
    plat.place(x=80, y=240)

    platform = tk.StringVar(time, name="platform")
    pl = ttk.Combobox(time, textvariable=platform, width=5)
    pl["values"] = ('1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')
    pl.current(0)
    pl.place(x=300, y=240)

    special = tk.Label(time, text="Special Annoucement", bg="blue", font="bold", fg="white", bd=5)
    special.place(x=40, y=320)

    def detect(event):
        l = []
        special_ann["values"] = []
        for i in a:
            if (special_type.get() == i[:len(special_type.get())]):
                l.append(i)
            elif (special_type.get() in i.split()):
                l.append(i)
        special_ann["values"] = tuple(l)

    special_type = tk.StringVar()
    special_ann = ttk.Combobox(time, width=25, textvariable=special_type)
    special_ann["values"] = ["No special announcement", 'be aware of pick poketers', 'belongings_strangers',
                             'donot any food articles from unknown', 'donot throw waste materials',
                             'donot use latrine', 'empty rack', 'engage_licence_coolie_only',
                             'fir is available with the train conductor',
                             'handicapped persons are requested to travel', 'inconvenience caused is deeply',
                             'India is one, Indian railways', 'ladies to avoid sleeping or sitting',
                             'may have ur attention pls the coolie charges',
                             'passengers are requested to engage', 'pls donot carr inflaimable & dangerous',
                             'pls donot enter when train is in motion', 'pls donot pull alarm chain', 'plz donot buy any food stuff',
                             'plz donot entrust ur belongings', 'plz enter the platform with proper ticket', 'plz help us to keep the premises clean',
                             'premises_clean', 'self service trolleys are available', 'senior citizens availing concessional travel',
                             'smoking on the platform and the compartment', 'students are requested to travel', 'take_care_belongings',
                             'ticketless travel is a social evil', 'trains are our nations property', 'use_trash',
                             'wish u a happy journey', 'women passengers plz take care of ur jewellry']
    special_ann.place(x=300, y=320)
    special_ann.current(0)
    global a
    a = ["No special announcement", 'be aware of pick poketers', 'belongings_strangers', 'donot any food articles from unknown', 
    'donot throw waste materials', 'donot use latrine', 'empty rack', 'engage_licence_coolie_only',
     'fir is available with the train conductor', 'handicapped persons are requested to travel',
      'inconvenience caused is deeply', 'India is one, Indian railways', 'ladies to avoid sleeping or sitting',
       'may have ur attention pls the coolie charges', 'passengers are requested to engage', 'pls donot carr inflaimable & dangerous',
        'pls donot enter when train is in motion', 'pls donot pull alarm chain', 'plz donot buy any food stuff',
         'plz donot entrust ur belongings', 'plz enter the platform with proper ticket', 'plz help us to keep the premises clean',
          'premises_clean', 'self service trolleys are available', 'senior citizens availing concessional travel', 
          'smoking on the platform and the compartment', 'students are requested to travel', 'take_care_belongings', 
          'ticketless travel is a social evil', 'trains are our nations property', 'use_trash', 'wish u a happy journey',
           'women passengers plz take care of ur jewellry']
    special_ann.bind('<KeyRelease>', detect)
    lang = tk.Label(time, text="Language", fg="green", font="bold", width=12)
    lang.place(x=70, y=420)

    english = tk.IntVar()
    eng_checkbutton = tk.Checkbutton(time, text="English", variable=english, onvalue=1,
                                     offvalue=0, height=2, width=10)
    eng_checkbutton.place(x=300, y=414)

    hindi = tk.IntVar()
    hin_checkbutton = tk.Checkbutton(time, text="Hindi  ", variable=hindi,
                                     onvalue=1, offvalue=0, height=2, width=10)
    hin_checkbutton.place(x=300, y=448)

    pic = tk.PhotoImage(file=r"C:\voice\data\images\ann.png")
    announce = tk.Button(time, image=pic, command=jump_function)
    announce.place(x=80, y=527)

    queue = tk.Button(time, text="Add to Queue", bg="white", fg="black", activebackground="blue",
                      font="bold", command = save)
    queue.place(x=300, y=530)

    def disable_time_select(event):
        if (time_type.get() == "has_left") or (time_type.get() == "has_been_cancelled_today"):
            hour["state"] = "disabled"
            minute["state"] = "disabled"
            arr["state"] = "disabled"

            hour_label["state"] = "disabled"
            min_label["state"] = "disabled"

            pl["state"] = "disabled"
            plat["state"] = "disabled"

            time.setvar(name="hours", value="")
            time.setvar(name = "minutes", value="")
            time.setvar(name = "platform", value = "")

        elif (time_type.get() == "is_sch_leave_at"):
            hour["state"] = "normal"
            minute["state"] = "normal"
            arr["state"] = "normal"
            arr["text"] = "Leaving at"

            hour_label["state"] = "normal"
            min_label["state"] = "normal"

            pl["state"] = "normal"
            plat["state"] = "normal"

        elif (time_type.get() == "is_exp_to_arrive_at"):
            hour["state"] = "normal"
            minute["state"] = "normal"
            arr["state"] = "normal"
            arr["text"] = "Arriving at"

            hour_label["state"] = "normal"
            min_label["state"] = "normal"

            pl["state"] = "normal"
            plat["state"] = "normal"

        else:
            hour["state"] = "normal"
            minute["state"] = "normal"
            arr["state"] = "normal"
            arr["text"] = "Late by"

            hour_label["state"] = "normal"
            min_label["state"] = "normal"

            pl["state"] = "disabled"
            plat["state"] = "disabled"

            time.setvar(name = "platform", value = "")

    a_type.bind("<<ComboboxSelected>>", disable_time_select)
    time.mainloop()



def timewin():
    tnumber = number.get()
    tname = name.get()
    ttype = Type.get()
    tfrom = From.get()
    tto = to.get()
    window.destroy()

    if (not (os.path.exists(r"C:\\voice\\TrainNames\\" + tname + ".wav"))):
        error = tk.Tk()
        error.title("Missing Database")
        error.geometry("400x100+452+296")
        tk.Label(error, text="Train name entered is not in the database!!!", font="bold", bg="yellow").pack()
        enter = tk.Button(error, text="Add Train", font="bold", command=name_error)
        enter.pack()
        error.resizable(0, 0)
        error.focus()
        error.mainloop()

    elif (not (os.path.exists(r"C:\\voice\\train_type\\" + ttype + ".wav"))):
        error = tk.Tk()
        error.title("Missing Database")
        error.geometry("400x100+452+296")
        tk.Label(error, text="Train type entered is not in the database!!!", font="bold", bg="yellow").pack()
        enter = tk.Button(error, text="Add Type", font="bold", command=type_error)
        enter.pack()
        error.resizable(0, 0)
        error.focus()
        error.mainloop()

    elif (not (os.path.exists(r"C:\\voice\\StationNames\\" + tfrom + ".wav") | (
    os.path.exists(r"C:\\voice\\StationNames\\" + tfrom + ".wav")))):
        error = tk.Tk()
        error.title("Missing Database")
        error.geometry("400x100+452+296")
        tk.Label(error, text="'From' station entered is not in the database!!!", font="bold", bg="yellow").pack()
        enter = tk.Button(error, text="Add Station", font="bold", command=station_error)
        enter.pack()
        error.resizable(0, 0)
        error.focus()
        error.mainloop()

    elif (not (os.path.exists(r"C:\\voice\\StationNames\\" + tto + ".mp3") | (
    os.path.exists(r"C:\\voice\\StationNames\\" + tto + ".wav")))):
        error = tk.Tk()
        error.title("Missing Database")
        error.geometry("400x100+452+296")
        tk.Label(error, text="'To' station entered is not in the database!!!", font="bold", bg="yellow").pack()
        enter = tk.Button(error, text="Add Station", font="bold", command=station_error)
        enter.pack()
        error.resizable(0, 0)
        error.focus()
        error.mainloop()

    else:
        set_time(tname, ttype, tto, tfrom, tnumber)

def csv_del(index):
    index = index
    l = []
    count = 0
    with open (r"C:\voice\data\save.csv", 'r', newline='') as file:
        csv_reader = csv.reader(file)
        f = next(csv_reader)
        for i in csv_reader:
            if (index != count):
                l.append(i)
            count = count + 1
    with open (r"C:\voice\data\save.csv", 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Number','Name','From','To','Status','Hours',
                             'Minutes','Platform','Special_announcement','Play'])
        csv_writer.writerows(l)

def queues():
    window.destroy()
    l = []
    with open(r"C:\voice\data\save.csv", 'r') as file:
        csv_reader = csv.reader(file)
        filed = next(csv_reader)
        for i in csv_reader:
            l.append(i)

    def switch(event):
        item = treev.focus()
        al = treev.item(item)["values"]
        index = treev.index(item)

        lis = al[:9]
        if (al[9] == "Play"):
            lis.append("")
        else:
            lis.append("Play")

        csv_del(index)
        with open(r"C:\voice\data\save.csv", 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(lis)

        treev.insert("", 'end', values=tuple(lis), tags = ('edit',))
        treev.delete(item)

    def edit(event):
        item = treev.focus()
        al = treev.item(item)["values"]
        index = treev.index(item)

        change = tk.Toplevel()
        change.title("Change")
        change.geometry("330x250+"+str(x)+"+"+str(y))

        tk.Label(change, text="Status", bg="red", fg="white").place(x=40, y=35)
        status = tk.StringVar(change)
        ann_type = ttk.Combobox(change, textvariable=status, width="25")
        ann_type.place(x=100, y=35)
        ann_type["values"] = ["is_exp_to_arrive_at", "is_running_late_by", "is_sch_leave_at", "has_left",
                              "has_been_cancelled_today"]
        ann_type.current(ann_type["values"].index(al[4]))

        hour = tk.StringVar(change)
        minute = tk.StringVar(change)
        tk.Label(change, text="Time", bg="red", fg="white").place(x=40, y=75)
        hours = ttk.Combobox(change, width="3", textvariable=hour)
        hours.place(x=100, y=75)
        hours["values"] = ('', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                           '16',
                           '17', '18', '19', '20', '21', '22', '23')
        hours.current(hours["values"].index(str(al[5])))

        tk.Label(change, text="hrs").place(x=150, y=75)
        minutes = ttk.Combobox(change, width="3", textvariable=minute)
        minutes.place(x=180, y=75)
        tk.Label(change, text="mins").place(x=235, y=75)
        minutes["values"] = ('', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                             '16',
                             '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
                             '32',
                             '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47',
                             '48',
                             '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
        minutes.current(minutes["values"].index(str(al[6])))

        platform = tk.StringVar(change)
        tk.Label(change, text="Platform", bg="red", fg="white").place(x=40, y=115)
        plat = ttk.Combobox(change, width="3", textvariable=platform)
        plat.place(x=100, y=115)
        plat["values"] = ('', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                          '14', '15', '16', '17', '18', '19', '20')
        plat.current(plat["values"].index(str(al[7])))

        special = tk.StringVar(change)
        tk.Label(change, text="Special", bg="red", fg="white").place(x=40, y=155)
        special_ann = ttk.Combobox(change, width="25", textvariable=special)
        special_ann.place(x=100, y=155)
        special_ann["values"] = ['No special announcement', 'be aware of pick poketers', 'belongings_strangers',
                                 'donot any food articles from unknown', 'donot throw waste materials',
                                 'donot use latrine', 'empty rack', 'engage_licence_coolie_only',
                                 'fir is available with the train conductor',
                                 'handicapped persons are requested to travel', 'inconvenience caused is deeply',
                                 'India is one, Indian railways', 'ladies to avoid sleeping or sitting',
                                 'may have ur attention pls the coolie charges', 'passengers are requested to engage',
                                 'pls donot carr inflaimable & dangerous', 'pls donot enter when train is in motion',
                                 'pls donot pull alarm chain', 'plz donot buy any food stuff',
                                 'plz donot entrust ur belongings', 'plz enter the platform with proper ticket',
                                 'plz help us to keep the premises clean', 'premises_clean',
                                 'self service trolleys are available', 'senior citizens availing concessional travel',
                                 'smoking on the platform and the compartment', 'students are requested to travel',
                                 'take_care_belongings', 'ticketless travel is a social evil',
                                 'trains are our nations property', 'use_trash', 'wish u a happy journey',
                                 'women passengers plz take care of ur jewellry']
        special_ann.current(special_ann["values"].index(al[8]))

        def save_changes():
            lis = [status.get(), hour.get(), minute.get(), platform.get(), special.get(), "Play"]
            lis = al[:4] + lis

            csv_del(index)
            with open(r"C:\voice\data\save.csv", 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(lis)

            treev.insert("", 'end', values=tuple(lis), tags = ('edit',))
            treev.delete(item)
            change.destroy()

        def removes():
            csv_del(index)
            treev.delete(item)
            change.destroy()

        save = tk.Button(change, text="Change", activebackground="blue", command=save_changes)
        save.place(x=40, y=205)
        remove = tk.Button(change, text="Delete", activebackground="blue", command=removes)
        remove.place(x = 120, y = 205)
        change.mainloop()

    def play_all():
        with open(r"C:\voice\data\save.csv", 'r', newline="") as file:
            csv_read = csv.reader(file)
            f = next(csv_read)
            row = []
            for i in csv_read:
                if (i[9] == "Play"):
                    row.append(i)
        for i in row:
            string = i[1].split(" ")
            train_name, train_type = string[0], string[1]
            announcement(train_name, train_type, i[3], i[2], i[0], i[4],
                             i[5], i[6], i[7], i[8], hindi.get(), english.get())


    wind = tk.Tk()
    wind.title("Queue")
    wind.geometry("1360x680+0+0")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview")
    style.map("Treeview", background = [("selected", "blue")])

    treev = ttk.Treeview(wind, selectmode='browse', height=20)
    treev.place(x=0, y=0)
    verscrlbar = ttk.Scrollbar(wind,
                               orient="vertical",
                               command=treev.yview)

    verscrlbar.pack(side='right', fill="both")

    treev.configure(xscrollcommand=verscrlbar.set)

    english = tk.IntVar(wind)
    eng_checkbutton = tk.Checkbutton(wind, text="English", variable=english, onvalue=1,
                                     offvalue=0, height=2, width=10)
    eng_checkbutton.place(x=500, y=500)

    hindi = tk.IntVar(wind)
    hin_checkbutton = tk.Checkbutton(wind, text="Hindi  ", variable=hindi, onvalue=1,
                                     offvalue=0, height=2, width=10)
    hin_checkbutton.place(x=500, y=540)

    play = tk.PhotoImage(file = r"C:\voice\data\images\green-play-button-png.png")
    play_button = tk.Button(wind, image = play, bd = 0, command = play_all)
    play_button.place(x = 640, y = 517)

    treev["columns"] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

    treev['show'] = 'headings'

    treev.column("1", width=135, anchor='c')
    treev.column("2", width=135, anchor='c')
    treev.column("3", width=135, anchor='c')
    treev.column("4", width=135, anchor='c')
    treev.column("5", width=135, anchor='c')
    treev.column("6", width=135, anchor='c')
    treev.column("7", width=135, anchor='c')
    treev.column("8", width=135, anchor='c')
    treev.column("9", width=135, anchor='c')
    treev.column("10", width=135, anchor='c')

    treev.heading("1", text="Number")
    treev.heading("2", text="Name")
    treev.heading("3", text="From")
    treev.heading("4", text="To")
    treev.heading("5", text="Status")
    treev.heading("6", text="Hours")
    treev.heading("7", text="Minutes")
    treev.heading("8", text="Platform")
    treev.heading("9", text="Special Announcement")
    treev.heading("10", text="Play")

    treev.tag_configure("edit", background="green")
    treev.tag_configure("oddrow", background = "silver")
    treev.tag_configure("evenrow", background = "white")
    ct = 1
    for i in l:
        if (ct % 2 == 0):
            treev.insert("", 'end', values=tuple(i), tags = ('evenrow',))
        else:
            treev.insert("", 'end', values=tuple(i), tags=('oddrow',))
        ct = ct + 1

    def coordinates(event):
        global x
        global y
        x = event.x
        y = event.y

    treev.bind('<Double-Button-1>', edit)
    treev.bind('<Button-3>', switch)
    wind.bind("<Motion>", coordinates)
    wind.mainloop()

window = tk.Tk()
window.title("Announcment")
window.geometry("480x480+432+109")
style = ttk.Style()
style.theme_use("clam")

background_image = tk.PhotoImage(file=r"C:\voice\data\images\rsz_unnamed.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.resizable(0, 0)

no = tk.Label(text="TRAIN No.", bg="green", fg="white", font="bold").place(x=40, y=40)
number = tk.StringVar()
tno = tk.Entry(window, textvariable=number).place(x=300, y=42)

na = tk.Label(text="TRAIN Name", bg="green", fg="white", font="bold").place(x=40, y=100)
name = tk.StringVar()
tname = tk.Entry(window, textvariable=name).place(x=300, y=102)

ty = tk.Label(text="TYPE", bg="green", fg="white", font="bold").place(x=40, y=160)
Type = tk.StringVar()
typ = ttk.Combobox(window, textvariable=Type, width=17)
typ['values'] = ["Express", "Super_Fast_Exp", "Local"]
typ.place(x=300, y=162)
typ.current()

fr = tk.Label(text="FROM", bg="green", fg="white", font="bold").place(x=40, y=220)
From = tk.StringVar()
fro = tk.Entry(window, textvariable=From).place(x=300, y=222)

t = tk.Label(text="TO", bg="green", fg="white", font="bold").place(x=40, y=280)
to = tk.StringVar()
too = tk.Entry(window, textvariable=to).place(x=300, y=282)

time_image = tk.PhotoImage(file=r"C:\voice\data\images\rsz_icon_fastsetting2-512 (1).png")
time = tk.Button(window, image=time_image, command=timewin)
view_queue = tk.Button(window, text = "View Queue>>", font = "bold", bg = "white", activebackground = "blue", command = queues)
view_queue.place(x=300, y=392)
time.place(x = 40, y = 382)

window.mainloop()
