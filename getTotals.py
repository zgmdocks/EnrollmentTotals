#! /usr/bin/python
import MySQLdb
import requests
import json
import datetime
from info import *

courses = ['cs/240','cs/241','cs/251','co/481','econ/102','co/444','biol/355','clas/104','biol/450','kin/310','ahs/100','hlth/340','chem/267','cs/452','math/136','math/239','math/138','phys/122','cs/136','econ/101','math/128','math/127']

db = MySQLdb.connect(host="localhost",user="root",passwd=password,db='Courses')
cur = db.cursor()

url1 = "https://api.uwaterloo.ca/v2/courses/"
url2 = "/schedule.json"
payload = {'key':key}

date = datetime.datetime.today().strftime('%Y-%m-%d')
time = datetime.datetime.today().strftime('%H:%M:%S')

for course in courses:
    url = url1 + course + url2
    resp = requests.get(url=url,params=payload)
    info = json.loads(resp.text)['data']

    total = 0
    limit = 0

    print course
    for lec in info:
        if 'LEC' in lec['section']:
            total = lec['enrollment_total']
            limit = lec['enrollment_capacity']
            section = lec['section']
            print section
            lecturers = lec['classes'][0]['instructors']
            if len(lecturers) > 0:
                lecturer = lecturers[0]
            print lecturer
            print total
            print limit
            cur.execute("INSERT INTO enrollment VALUES (%s,%s,%s,%s,%s,%s,%s)",(course,section,lecturer,total,limit,date,time))
            db.commit()

