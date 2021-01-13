from mega2.py06 import tv

lgTv = tv()
appleTv = tv()
#클래스의 변수를 가져와 초기화가 가능하다.
appleTv.company = 'apple'
appleTv.color = 'green'

lgTv.on()
lgTv.off()
print(lgTv)


appleTv.on()
appleTv.off()
print(appleTv)
# __str__은 자바의 toString 같은 것이다.
