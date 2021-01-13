from tkinter import *
from tkinter.ttk import *
import random
import time
import threading


class Car():
    label = None
    thread1 = None
    thread2 = None
    thread3 = None

    def __init__(self, parent, icon, x1, y1):
        self.label = Label(parent, image=icon)
        self.thread1 = threading.Thread(target=self.fast_run, args=(self.label, x1, y1,))
        self.thread2 = threading.Thread(target=self.opp_run, args=(self.label, x1, y1,))
        self.thread3 = threading.Thread(target=self.boom_boom)
        self.thread1.start()
        self.thread2.start()
        self.thread3.start()

    def fast_run(self, label, x1, y1):
        while True:
            jump = random.randrange(0, 10)
            x1 = x1 + jump
            label.place(x=x1, y=y1)
            time.sleep(0.5)

    def opp_run(self, label, x1, y1):
        while True:
            jump = random.randrange(0, 10)
            x1 = x1 - jump
            label.place(x=x1, y=y1)
            time.sleep(0.5)

    def boom_boom(self):
        time.sleep(0.10)


def run_car():
    car_r = Car(window, r_car, 450, 150)
    car_l = Car(window, l_car, 30, 150)
    car_boom = Car(window, boom, 50, 20)


if __name__ == '__main__':
    window = Tk()
    window.geometry("600x500")
    window.title('멀티 스레드')

    r_car = PhotoImage(file='warrior2.gif')
    l_car = PhotoImage(file='warrior/.gif')
    boom = PhotoImage(file='effe.gif')

    button = Button(window, text="자동차 달리자!!!", command=run_car)
    button.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)

    window.mainloop()
