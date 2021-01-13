#1번 문제 주민등록 확인
human = input('주민번호를 번호만 입력해 주세요.')
if human[6] == str(1):
    print('남성 입니다.')
elif human[6] == str(2):
    print('여성 입니다.')
else:
    print('제대로 입력해주세요')

#2번 문제 현재 시간 확인
time = int(input('현재 시간을 시간만! 입력해 주세요.'))
if time <= 11:
        print('굿모닝')
elif time <= 15:
    print('굿애프터눈')
elif time <= 20:
    print('굿이브님')
else:
    print('굿나잇')

#3번 문제 인기투표 시스템
star = ['아이유', '공유', '유재석']
vote = [0, 0, 0]
while True:
    print("1) 아이유 2) 공유 3) 유재석 0) 종료")
    user = input()
    if user == '1':
        vote[0] += 1
    elif user == '2':
        vote[1] += 1
    elif user == '3':
        vote[2] += 1
    elif user == '0':
        break
    else:
        print("번호 중 입력해 주세요.")
print(f'아이유: {vote[0]}표, 공유: {vote[1]}표, 유재석: {vote[2]}표')