class tv:
    company = 'mega'
    color = 'red'
    size = 50

    def __init__(self):
        print('tv가 만들어졌습니다.')

    def on(self):
        print('tv를 켜다')

    def off(self):
        print('tv를 끄다')

    def __str__(self):
        return self.company + "," + self.color + "," + str(self.size)