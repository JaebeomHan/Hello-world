#클래스로 인자 받을것 받고, 데이터 인서트
import pymysql

class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user= id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def save_value(self, table_name, values):
        sql = 'INSERT INTO {0} VALUES ({1})'.format(table_name, ','.join(values))
        self.curs.execute(sql)
        self.conn.commit()
