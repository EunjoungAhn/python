from tkinter import *

def login():
    get_id_entry = id_entry.get()
    get_pw_entry = pw_entry.get()
    if(get_id_entry == 'root' and get_pw_entry == '123'):
        print("로그인이 되었습니다.")
    else:
        print('아이디와, 비번을 확인해 주세요.')

def reset():
    id_entry.delete(0, END)
    pw_entry.delete(0, END)

w = Tk()
w.geometry('600x300')
w.config(bg = 'lime')

id_label = Label(w, text = 'id', font=('굴림', 50), width=5)
pw_label = Label(w, text = 'pw', font=('굴림', 50), width=5)

id_entry = Entry(w, font=('굴림', 50), width=7, bg='yellow')
pw_entry = Entry(w, font=('굴림', 50), width=7, bg='yellow')

button = Button(w, text = '로그인', font=('굴림', 50), width=7, bg='pink', command=login)
button2 = Button(w, text = '초기화', font=('굴림', 50), width=7, bg='pink', command=reset)

id_label.grid(row=0, column=0)
id_entry.grid(row=0, column=1)
pw_label.grid(row=1, column=0)
pw_entry.grid(row=1, column=1)
button.grid(row=2, column=0)
button2.grid(row=2, column=1)


w.mainloop()
