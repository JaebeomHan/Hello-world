#실제로 데이터를 인서트


import Mysql_Controller
values = ['id','1', '2','3','4','5','6','created']
table_name = 'megaton_data'
if __name__ == '__main__':
    mysql_controller = Mysql_Controller.MysqlController('localhost', 'root', 'cordmfdlfrwk07', 'pra')
    mysql_controller.save_value(table_name, values)
