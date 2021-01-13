#첫 줄에는 별 1개부터 시작하여 10번째 줄에는 별 10개가 찍히게!
print('1번 문제')
for i in range(10):
    print('*' * (i+1))#문자열 곱해서 반복이 가능하기 때문에
    #for문에서 i값을 기준으로 '*'을 곱해서 range만큼 반복한다.
    # * x 1 = 1이기 때문에 한번 찍고 시작한다.

#이름, 나이, 성별, 좌우명 입력 받고 한번에 출력
print('2번 문제')
name = input('나의 이름은: ')
age = int(input('나의 나이는: '))
gender = input('나의 성별은: ')
moto = input('나의 좌우명은: ')
print('나는{0}이고, 내 나이는{1}세, 내년 나이는 {2}세가 될 예정이고,'
      ' 나는 {3} 야!, 나는{4}가 내 좌우명!'.format(name,age,str(age+1),gender,moto))

#콘솔에서 당신의 이름을 입력, 콘솔에서 당신이 관심사를 입력
#메세지박스로 이름과 관심사를 출력
#관심사가 파이썬이라면 '분석가가 되실 거군'
#아니라면 '개발자가 되실거군'
print('3번 문제')
name = input('당신의 이름은: ')
hobby = input('당신의 관심사는: ')
if hobby == '파이썬':
    print('{0}님은 분석가가 되실 거군'.format(name))
else:
    print('{0}님은 개발자가 되실거군'.format(name))

#오늘 날짜와 시각을 datatime라이브러리를 이용해 찍으세요.
#3~5월이면 봄, 6~8월이면 여름, 9~11월이면 가을, 나머지는 겨울
print('4번 문제')
import datetime
#datetime 파일안에 datetime 클래스가 있고, 그안에 now()함수가 있어서 사용한다.
#자바보다 한 단계 더 들어간 느낌이다.
now_month = datetime.datetime.now()
if 3 <= now_month.month <= 5:
    season = '봄'
elif 6 <= now_month.month <= 8:
    season = '여름'
elif 9 <= now_month.month <= 11:
    season = '가을'
else:
    season = '겨울'

print("지금은{0}이네요.".format(season))

#55부터 688까지 3씩 점프하면서 모두 더해보세요.
print('5번 문제')
sum = 0
#range(star, stop, step) step = 숫자 간격을 말한다.
for num in range(55,688,3):
    sum += num
print(sum)

#선수의 이름을 입력 계속 받고, x를 누르면 종료
print('6번 문제')
player = []
while True:
    human = input('선수의 이름을 입력해주세요. 종료하시려면 x를 입력해주세요.')
    player.append(human)
    if human == 'x':
        break
print(f'첫번째 선수는{player[0]}, 세번째 선수는{player[2]}')