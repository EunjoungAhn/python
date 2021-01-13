#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install pymongo')


# In[9]:


from pymongo import MongoClient


# In[10]:


conn = MongoClient("mongodb://localhost")
conn


# In[11]:


from bs4 import BeautifulSoup
import requests


# In[12]:


mel = conn.melon
mel


# In[13]:


music_url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'}


# In[14]:


response = requests.get(music_url, headers=headers)


# In[16]:


res = response.text
res


# In[17]:


soup = BeautifulSoup(res, 'html.parser')


# In[19]:


#이런 순서를 xpath라고 부른다
result = soup.select('#tb_list > form > div > table > tbody > tr > td > div.wrap > a > img')
result


# In[21]:


len(result)


# In[26]:


result[0].get('src')


# In[28]:


image = []


# In[29]:


for i in soup.select('#tb_list > form > div > table > tbody > tr > td > div.wrap > a > img'):
    image.append(i.get('src'))


# In[30]:


title = []


# In[32]:


for i in soup.select('div.ellipsis.rank01 > span > a'):
    title.append(i.getText())


# In[33]:


singer = []


# In[35]:


for i in soup.select('td >div > div > div.ellipsis.rank02 > span > a'):
    singer.append(i.text)


# In[48]:


len(singer)


# In[59]:


singer.remove('미란이 (Mirani)')


# In[80]:


singer.remove('아이유')


# In[79]:


len(singer)


# In[38]:


setSinger = set(singer)


# In[40]:


len(setSinger)


# In[41]:


like = [113791,63280,65487,153449,49420,295179,50405,180655,107605,136134,
        81530,100350,108155,114308,66528,86842,52830,221633,100454,240560,
        141023,248863,88177,249893,87203,179563,25275,66710,14392,329432,
        56680,149563,294566,234462,382200,57394,157584,50665,205481,192918,
        59484,83117,336086,76165,83791,88709,29448,169618,14392,20319,
        93814,216193,35207,5826,67576,37945,105837,23880,105113,8505,
        51297,129283,258112,4603,13499,12460,82935,485883,161133,194129,
        92868,43812,230375,155658,42314,121823,26357,39039,263255,48300,
        74332,8961,139368,16518,166084,54972,59448,137149,43583,256299,
        51826,37107,130846,130044,98090,30030,130658,127616,108275,132023]


# In[43]:


len(like)


# In[44]:


imsi= [] #[{},{},{}]


# In[86]:


#몽고 db에 넣어봅시다
for i in range(100):
    melon = {} # dictionary
    melon.update(title = title[i]) #{'title':'iamsongtitle'}
    melon.update(singer = singer[i])
    melon.update(like = like[i])
    melon.update(img = image[i])
    imsi.append(melon)
imsi


# In[85]:


len(imsi)


# In[81]:


doc = mel.docu
doc


# In[91]:


doc.insert_many(imsi)


# In[90]:


doc.find()


# In[93]:


import pandas as pd


# In[94]:


data = pd.read_csv('docu.csv') # 2차원 테이블형태의 데이터 구조: '데이터프레임'이라고 한다.


# In[96]:


data


# In[99]:


data.drop('_id', axis=1) # axis 파괴함수


# In[100]:


import matplotlib.pyplot as plt # 데이터 시각화를 위해 import 그리고 한글을 지원하지 않아서
import seaborn as sns #그래프를 컬러입히는 라이브러리


# In[101]:


import platform # 로 한글화를 한다.

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 


# In[104]:


plt.figure(figsize=[10,10])

a = sns.barplot(x='title', y='like', data=data.head(10))

for item in a.get_xticklabels(): #제목이 겹치므로 각도를 주어서 안 겹치도록 설정
    item.set_rotation(45)

plt.show()


# In[106]:


plt.figure(figsize=[10,10])
plt.pie(data['like'].head(10), 
        explode=[0,0,0,0,0,0,0,0,0,0], 
        labels=data['title'].head(10), 
        autopct='%1.2f%%', # second decimal place
        shadow=True, 
        startangle=90,
        textprops={'fontsize': 14}) # text font size
plt.axis('equal') #  equal length of X and Y axis
plt.title('Melon - Top10(좋아요)', fontsize=20)

plt.show()

