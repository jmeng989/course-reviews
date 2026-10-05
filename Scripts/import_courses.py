import pymysql as p

conn = p.connect(
    host="127.0.0.1",
    port=3307,
    user="jm2598",
    password="acFipaxHuv",
    database="jm2598"
)
cur = conn.cursor()

cur.execute(
    """SELECT No., 2020_2021_lecturer, 2019_2020_lecturer, 2018_2019_lecturer, 2017_2018_lecturer, 2016_2017_lecturer
    FROM mguide_courses"""
)
conn.commit()

conn.close()