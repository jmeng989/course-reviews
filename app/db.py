import pymysql as p

def get_db():
    return p.connect(
        host="mysql.internal",
        user="jm2598",
        password="acFipaxHuv",
        database="jm2598",
        cursorclass=p.cursors.DictCursor
    )