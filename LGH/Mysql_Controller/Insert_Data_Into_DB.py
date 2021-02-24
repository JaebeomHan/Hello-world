#실제로 데이터를 인서트


import Mysql_Controller

if __name__ == '__main__':
    mysql_controller = Mysql_Controller.MysqlController('localhost', 'root', 'cordmfdlfrwk07', 'megaton')
    table_name = 'megaton_data'
    mysql_controller.save_value(table_name, ['id', '"test"', '"test1"','1','1.234','1.234','"test5"', 'created'])
