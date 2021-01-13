# 뱀표기법, snake _
# tuple(읽기 전용)
read_only = ('감자', '고구마', '양파')
print(read_only)
print(type(read_only))
#read_only[0] = '물'

food = ['감자', '고구마', '양파', '양파', '양파', '양파', '감자']
food.append('물')
food2 = tuple(food)
print(food2)

food3 = list(read_only)
food3.remove('감자')
food4 = tuple(food3)

food5 = set(food)
print(food5)
print(len(food5))

