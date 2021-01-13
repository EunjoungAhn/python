food = ['감자', '고마마','양파']
#for, for-each
#1. for-each
for x in food:
    print(x, end=' ') #옆으로 출력하고 싶을때

print()#공백 역할

#2. for
for i in range(0,3): # 0~2까지
    print(food[i])

print()#공백 역할

for i in [0,1,2]: # 0~2까지
    print(food[i])

subject = []
#입력을 5번 받아서, 리스트에 넣어세요.
#2가지 방법으로 프린트
subject = input('과목을 입력해주세요.')
for x in subject:
    print(x, end=' ')

print()

for i in range(len(subject)):
    print(subject[i])

jumsu = []
#리스트에 넣은 점수를 합해서 평균만들고 프린트 하기
sum_avg = 0;
num = int(input('점수 입력할 과목수를 입력해주세요'))
for x in range(0,num):
    sum_avg = float(input('점수를 입력해주세요'))
    jumsu.append(sum_avg)

for x in range(0,num-1): #인덱스 0부터 시작이기 때문에 num-1만큼만 반복
    sum_avg += jumsu[x]
    print(jumsu[x])#찍어서 값 확인
print('총 점수는', sum_avg)
print('평균점수는', sum_avg / num)