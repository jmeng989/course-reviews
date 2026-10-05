import pymysql as p

conn = p.connect(
    host="127.0.0.1",
    port=3307,
    user="jm2598",
    password="acFipaxHuv",
    database="jm2598"
)
cur = conn.cursor()



cur.execute("SELECT course_id, User_id, Timestamp, Year_of_lecture, Review_markdown, Add_data FROM mguide_course_1 WHERE Status = 2")
rows = cur.fetchall()
cur.execute("SET FOREIGN_KEY_CHECKS = 0")

for row in rows:
    course_id = row[0]
    hidden = 0
    likes = 0
    lecturer_content = ''
    crsid = row[1]
    timestamp = row[2]
    year =  row[3][0:4]
    content = row[4]
    data = row[5].split(',')
    f = data[-2].find(':')
    f2 = f+2
    while f2 < len(data[-2]) and (data[-2][f2].isdigit() or data[-2][f2] == '.'):
        f2 += 1
    d = data[-1].find(':')
    d2 = d+2
    while d2 < len(data[-1]) and (data[-1][d2].isdigit() or data[-1][d2] == '.'):
        d2 += 1
    fun = int(float(data[-2][f+2:f2])*2)
    difficulty = int(float(data[-1][d+2:d2])*2)
    cur.execute(
        "INSERT INTO Reviews (course_id, year, crsid, fun, difficulty, content, lecturer_content, hidden, likes, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (course_id, year, crsid, fun, difficulty, content, lecturer_content, hidden, likes, timestamp)
    )


cur.execute("SET FOREIGN_KEY_CHECKS = 1")
conn.commit()

conn.close()