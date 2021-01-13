import pymysql
#네트워크 연결 객체 requests
#alt_enter: 라이브러리 설치
import requests

def all():
    #Mysql connection 연결
    con = pymysql.connect(host='localhost', port=3306, user='root', password='1234',
                    db='shop1', charset='utf8')
    print('연결 성공', con)

    curs = con.cursor()
    print('커서 객체 생성')
    sql = 'select * from member'
    curs.execute(sql)
    print('all sql문 생성 후 전송')

    #커서 객체에 결과를 담는다.
    rows = curs.fetchall()
    print(len(rows))

    rows_list = list() # 전체 목록을 담을 리스트

    for row in rows:
       print('---all()',row)
       rows_list.append(list(row)) # 리스트의 리스트로 만들기

    print(rows_list)
    con.close()
    print('all myslq과 연결되었던 스트림 closed!')
    return rows_list #리스트가 리턴

def read():
    #Mysql connection 연결
    con = pymysql.connect(host='localhost', port=3306, user='root', password='1234',
                    db='shop1', charset='utf8')
    print('연결 성공', con)

    curs = con.cursor()
    print('커서 객체 생성')
    sql = 'select * from member'
    curs.execute(sql)
    print('sql문 생성 후 전송')

    #커서 객체에 결과를 담는다.
    rows = curs.fetchall()
    print(rows[0]) #수정을 할 수 없는 상태 튜플

    result = list(rows[0])
    print(result)

    con.close()
    print('myslq과 연결되었던 스트림 closed!')
    return result #리스트가 리턴

def create(id, pw, name, tel):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='1234',
                          db='shop1', charset='utf8')
    print('create 연결 성공', con)

    curs = con.cursor()
    print('create 커서 객체 생성')
    sql = "insert into member values ('" + id + "','" + pw + "','" + name + "','" + tel + "')"
    # sql = f"-- insert into member values ('{id}', '{pw}', '{name}', '{tel}')"
    curs.execute(sql)
    print('create sql문 생성 후 전송')

    con.commit()
    con.close()
    print('create myslq과 연결되었던 스트림 closed!')


def update():
    pass

def delete():
    pass