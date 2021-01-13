#print('welcome!!')

#명령어 == 함수 == 메서드
#기능을 사용함.
#파이썬에서 함수를 만들때 def를 사용

#기능을 정의한. 함수를 정의한다.
#def 함수명():
#    들여쓰기한 다음 실행하는 것 쭉 구현
def print2():
    print('나는 프린트를 2번 하겠음.')

#클래스 사용법
class Dog:
    name = '홍길동'

    def __init__(self):
        print('내가 생성자!!!')
    
    def bark(self):
        print('강아지가 짖다')

    #멤버변수는 self를 붙여야 한다.
    #__str__은 자바의 toString 같은 것이다.
    def __str__(self):
        return self.name

#이것만 실행하고 싶을때 main을 따로 설정해서 실행해준다.
if __name__ == '__main__':
    dog1 = Dog()
    dog1.bark()
    print(dog1)
    print2() #호출한다 (call)
# print2()
# print2()

