#1학기 성적
#2학기 성적
term1 = {10,20,30,40}
term2 = {11,20,33,40}
#교집합을 찾아준다 &
print(term1 & term2) #비파괴 ram을 건드리지 않는건
print(term1 | term2) #교집합은 제거 후 출력
print(term1 - term2)

#파괴함수, 비파괴함수
#파라미터에 따라 다른다 string이면 call by reference
#int 면 call by value


#딕셔너리(사전 형식)
jumsu = {'철수':100, '영희':90}
print(jumsu['철수'])
jumsu['영희'] = 100
print(jumsu)

#딕셔너리를 함수처럼 사용해서 쓸 수 있다.
jumsu2 = dict(철수 = 100, 영희 = 90)
print(jumsu2)

del jumsu2['철수']
print(jumsu2)

jumsu2['순희'] = 80
jumsu2['갑순'] = 88
print(jumsu2)

for key in jumsu2:
    print(key, jumsu2[key]) # , 쉼표를 찍어서 구분하면 공백이 추가되어서 출력된다.

from tkinter import messagebox
messagebox.showinfo("it's me!!!")
result = messagebox.askquestion("ok?","really?")
print(result)
if result == 'yes':
    print('확인 완료')
else:
    print('다시 확인 필요')


data = (1,2,3)
data2 = {1,2,3}
data3 = [1,2,3]
data4 = {'name':'hong','age':100}
print(type(data))
print(type(data2))
print(type(data3))
print(type(data4))
