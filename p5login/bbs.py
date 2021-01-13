from tkinter import *

def read_file():
#day_input에 입력한 값을 가진 파일을
#한줄씩 읽어서, Entry에 텍스트로 집어 넣는다.
#day_input.insert(0, '한줄읽어온 내용')
    day_data = day_input.get()
    file = open(day_data + '.txt', 'r')

    day_input.delete(0, END)
    title_input.delete(0, END)
    content_input.delete(0, END)

    #파일을 한 줄씩 읽어오기
    day_line = file.readline()
    title_line = file.readline()
    content_line = file.readline()


    day_input.insert(0, day_line)
    title_input.insert(0, title_line)
    content_input.insert(0, content_line)


def save_file():
    #파일로 저장하는 처리 값 가져오기
    day_data = day_input.get()
    title_data = title_input.get()
    content_data = content_input.get()

    #파일에 저장하기, w 는 쓰기 전용으로 쓰겠다.
    file = open(day_data + ".txt", 'w')
    file.write(day_data + '\n')
    file.write(title_data + '\n')
    file.write(content_data + '\n')
    file.close()

    #파일을 저장했으면, 지워라
    day_input.delete(0, END)
    title_input.delete(0, END)
    content_input.delete(0, END)

    day_input.insert(0, '날짜입력')


w = Tk()
#라벨 4개
img = PhotoImage(file='dog2.png')
top = Label(w, image=img)
top.pack()


day = Label(w, text = '날짜:', font = ('궁서', 30))
title = Label(w, text = '제목:',font = ('궁서', 30))
content = Label(w, text = '내용:',font = ('궁서', 30))
#입력 3개
day_input = Entry(w, font=('궁서', 30), bg='yellow')
title_input = Entry(w, font=('궁서', 30), bg='yellow')
content_input = Entry(w, font=('궁서', 30), bg='yellow')

#버튼 2개
save = Button(w, text='파일로 저장', font=('궁서', 30), bg='lime', command = save_file)
read = Button(w, text='파일로 읽기', font=('궁서', 30), bg='lime', command = read_file)


day.pack()
day_input.pack()
title.pack()
title_input.pack()
content.pack()
content_input.pack()
save.pack()
read.pack()


w.mainloop()