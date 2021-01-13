class coffee:
    price = 5000

    def __init__(self, type, num):
        self.type = type
        self.num = num

    def __str__(self):
        return '손님의 주문 음료는 {0}커피 이며 총 {1}개 주문하셨습니다.'.format(self.type, self.num)

    def pay(self, num):
        self.num = num
        print('총{0}원입니다.'.format(num * self.price))