food = ['감자','고구마','양파'] # 0~2

life = [] #life = list() 함수로 만들 수 있다.
print(food)
print(food[0])
print(len(food))
print(food[-1])
print(food[:2]) #앞이 없으면 처음부터 가져와라 0, 1 / 자바의 subString과 같다.
food[0] = 'cake'
print(food)
food.append('coffee') #자바에서의 list의 add와 같다.
print(food)

food.insert(0,'rice') #인덱스 기준으로 값 바꾸기
print(food)

food.remove('rice') #값을 가지고 삭제
print(food)

del food[0] # del은 인덱스를 가지고 삭제
print(food) 

life.append('여행')
print(life)

print(food + life)

total = food + life
print(total)

total2 = food*2
print(total2) # 반복해서 넣어준다.

#life에 값을 5개 추가하고, 내용확인
life.append('미술')
life.append('운동')
life.append('코딩')
life.append('휴식')
print(life)
# 마지막 넣은 값을 삭제하고, 내용확인
life.remove('휴식')
print(life)
# 첫번째 넣은 값을 다른 내용을 수정하고, 내용확인
life.insert(0,'휴식')
print(life)
# 두번째 넣은 값 앞에 하나 더 내용 추가하고, 내용확인
life.insert(1,'게임')
print(life)
#total3에 내가 먹고 싶은 음식 목록과 내 인색 목록을 모두 모아서, 내용확인,
total3 = food+life
print(total3)
#몇개 되는지 확인
print(len(total3))

mylist = "This is a book That is a pencil".split()
i = mylist.index('book')  # i = 3
n = mylist.count('is')    # n = 2
print(i, n)
print(type(mylist)) #타입을 확인하는 함수
print(mylist)

#먹고 싶은 음식 종류를 입력 받아서
foodType = input('먹고 싶은 음식 종류를 입력해주세요.').split()
print(len(foodType))