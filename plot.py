#! /usr/bin/python3.5
import MySQLdb
from info import *
import matplotlib.pyplot as plt
from datetime import datetime

db = MySQLdb.connect(host="localhost",user="root",passwd=password,db='Courses')
cur = db.cursor()

db.query("SELECT enrollment_total,time,time_stamp FROM enrollment where course='cs/240'")

query = db.store_result()

results = query.fetch_row(maxrows=0)

data = {}

for val in results:
    time = datetime.strptime(val[2].strftime("%m/%d/%y") + " " + val[1],"%m/%d/%y %H:%M:%S")
    if not time in data:
        data[time] = val[0]
    else:
        data[time] = data[time] + val[0]

x = []
y = []

for val in data:
    x.append(val)
    y.append(data[val])

plt.plot_date(x,y,'-')
plt.show()
