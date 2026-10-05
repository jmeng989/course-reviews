import pymysql as p

def get_db():
    return p.connect(
        host="127.0.0.1",
        port=3307,
        user="jm2598",
        password="acFipaxHuv",
        database="jm2598",
        cursorclass=p.cursors.DictCursor
    )