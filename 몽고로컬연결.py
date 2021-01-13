# Requires pymongo 3.6.0+
from pymongo import MongoClient
#몽고db 서버 연결
conn = MongoClient("mongodb://localhost")
#cine db 데이터베이스 연결
cine = conn.cine21
print(cine)

# member collection연결
member = cine.member
print(member)
# document(하나의 row) 1개 추가, db에 데이터 넣기
# data = {'name':'song','age':500,'add':'young','tel':'011'}
# member.insert_one(data)

# data2 = {'name':'mike','age':45}
# member.insert_one(data2)
#
# data3 = [
# {'name':'dave','age':23},
# {'name':'jack','age':44,'add':'seoul'},
# {'name':'sujan','age':32,'add':'kang','tel':'011'}
# ]
# member.insert_many(data3)

# print(member.count())#DeprecationWarning - 곳 없어질꺼라는 뜻
# 하나만 검색해서 가져오기 .find_one()
# print(member.find_one())

data4 = {'title': '암살', 'castings': ['이정재', '전지현', '하정우']}
data5 = {'title': '실미도', 'castings':  ['설경구', '안성기'],
'date': '2003.3', 'spaces':  ['cgv', 'lotte']}
# member.insert_one(data4)
member.insert_one(data5)
# json => dictionary(사전 타입)
print(member.find_one({'title': '실미도'}))
# cusur 검색해서 보여준다.
print(member.find({'tel': '011'}))

# for문으로 다 뽑아서 보여준다.
docs = member.find({'tel':'011'}).sort('age') #나이순으로 정렬하기
for x in docs:
    print(x)

#하나면 업데이트를 해라
member.update_one({'age':32}, {'$set':{'tel':999}})