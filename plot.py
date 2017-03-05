#! /usr/bin/python3.5
import MySQLdb
from info import *
import matplotlib.pyplot as plt
from datetime import datetime

db = MySQLdb.connect(host="localhost",user="root",passwd=password,db='Courses')
cur = db.cursor()

db.query("SELECT enrollment_total,time,time_stamp FROM enrollment where course='clas/104'")

query = db.store_result()

results = query.fetch_row(maxrows=0)

tempDict = {}

# used to add up all sections
for val in results:
    time = datetime.strptime(val[2].strftime("%m/%d/%y") + " " + val[1],"%m/%d/%y %H:%M:%S")
    if not time in tempDict:
        tempDict[time] = val[0]
    else:
        tempDict[time] = tempDict[time] + val[0]

data = []

# now changing dictionary into a list so I can sort by date
for key in tempDict.keys():
    data.append([key, tempDict[key]])

data.sort()

x = [x for (x,y) in data]
y = [y for (x,y) in data]

plt.plot_date(x,y,'-')
plt.show()
