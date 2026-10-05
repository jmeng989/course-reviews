with open("cleaned.txt", encoding="utf-8") as f:
    lines = f.readlines()

import pymysql as p

conn = p.connect(
    host="127.0.0.1",
    port=3307,
    user="jm2598",
    password="acFipaxHuv",
    database="jm2598"
)
cur = conn.cursor()

for line in lines:
    i = 0
    prev = 0
    while not line[i].isdigit():
        i += 1
    j = i
    while line[j].isdigit():
        j += 1
    course_id = int(line[i:j])

    cur.execute(f"ALTER TABLE mguide_course_1 MODIFY course_id INT DEFAULT {course_id}")
    conn.commit()
    cur.execute(line[:i] + '1`(id, User_id, Timestamp, Year_of_lecture, Target_audience, Type_of_review, Status, Edit_counter, Reason_for_rejection, Review_markdown, Review_content, Add_data)' +  line[j+1:])

conn.commit()
conn.close