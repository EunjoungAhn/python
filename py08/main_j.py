# -*- coding: utf-8 -*-

#네이버증권크롤링
#증권 여러개를 해보세요. 여러개 증권 코드번호를 list에 넣어서, 여러회사 크롤링
#크롤링한 여러회사것을 삼성전자.txt로 만들어서 서장
#증권정보 중 3개 이상
from pack01.정우씨크롤링 import *
from py08.정우씨db import *
code = ["005930","323990","068270","066570","009900"]
data_list = []
#코드로 데이터 리스트 추가해주기
for i in code:
    data_list.append(crawl(i))

for i in data_list:
    create(i[0],i[1],i[2],i[3])