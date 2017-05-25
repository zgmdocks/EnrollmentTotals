#! /usr/bin/python3.5
import MySQLdb
from info import *
import matplotlib.pyplot as plt
from datetime import datetime

courses = ['cs/240','cs/241','cs/251','co/481','phys/467','cs/467','econ/102','co/444','biol/355','clas/104','biol/450','kin/310','ahs/100','hlth/340','chem/267','cs/452','math/136','math/239','math/138','phys/122','cs/136','econ/101','math/128','math/127','chem/123']

for course in courses:
    db = MySQLdb.connect(host="localhost",user="root",passwd=password,db='Courses')
    cur = db.cursor()

    db.query("SELECT enrollment_total,time,time_stamp FROM enrollment where course='{}'".format(course))

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
    plt.savefig("{}.png".format(course).replace("/",""))
