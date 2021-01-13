def friend(name, info):
    print(name +'과의 관계는 '+ info+' 입니다.')

def pay(a):
    price = 10000
    print('영화를 {0}명이 같이 볼꺼에요. 금액은 총{1}원입니다.'.format(a, (a * price)))