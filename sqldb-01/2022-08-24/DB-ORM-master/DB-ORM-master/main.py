import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# # 1. Artist 생성
# import datetime
# artist = Artist()
# artist.name = '아이브'
# # 2021년 12월 1일
# artist.debut = datetime.date(2021, 12, 1)
# artist.save()

# artist = Artist() 
# artist.name = '아이유'
# artist.debut = '2019-12-26'
# artist.save()

# 3
import datetime
Director.objects.create(name = '봉준호', debut = datetime.date(1993, 1, 1), country = 'KOR')
Director.objects.create(name = '김한민', debut = datetime.date(1999, 1, 1), country = 'KOR')
Director.objects.create(name = '최동훈', debut = datetime.date(2004, 1, 1), country = 'KOR')
Director.objects.create(name = '이정재', debut = datetime.date(2022, 1, 1), country = 'KOR')
Director.objects.create(name = '이경규', debut = datetime.date(1992, 1, 1), country = 'KOR')
Director.objects.create(name = '한재림', debut = datetime.date(2005, 1, 1), country = 'KOR')
Director.objects.create(name = 'Joseph Kosinski', debut = datetime.date(1999, 1, 1), country = 'KOR')
Director.objects.create(name = '김철수', debut = datetime.date(2022, 1, 1), country = 'KOR')


# 4 
title = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']

for t in title:
    genre = Genre()
    genre.title = t
    genre.save()

# 5
for i in range(len(Director.objects.all())):
    temp = []
    temp.append(Director.objects.all()[i].name)
    temp.append(Director.objects.all()[i].debut)
    temp.append(Director.objects.all()[i].country)
    print(*temp)

# 6 
id1 = Director.objects.get(id=1)
print(id1.name, id1.debut, id1.country)


# 7
Director.objects.get(country = 'USA')

# 8 
# 오류 메세지
# DoesNotExist: Director matching query does not exist.

# 이유 작성
# 다들 KOR이라 USA에 매칭되는 값이 없어서 오류가 뜨는 것이다.


# 9
jk = Director.objects.get(name = 'Joseph Kosinski')
jk.country = 'USA'
jk.save()

jk = Director.objects.get(name='Joseph Kosinski')
print(jk.name, jk.debut, jk.country)

# 10
Director.objects.get(country = 'KOR')

# 11
# 오류 메세지
# MultipleObjectsReturned: get() returned more than one Director -- it returned 7!

# 이유 작성
# country가 KOR인 사람이 1개 보다 많기 때문에 오류 발생

# 12
c_kr = Director.objects.filter(country = 'KOR')
for i in range(len(c_kr)):
    print(c_kr[i].name, c_kr[i].debut, c_kr[i].country)

# 13
kcs = Director.objects.get(name = '김철수')
kcs.delete()