class cake:
    price = 8000

    def __init__(self, type, order):
        self.type = type
        self.order = order

    def __str__(self):
        return '손님이 {0}케익을 {1}개 주문하셨습니다'.format(self.type, self.order)

    def pay(self, num):
        self.num = num
        print('총{0}원입니다.'.format(num * self.price))