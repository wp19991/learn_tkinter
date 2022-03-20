import sqlite3
import time


class sqlite_diver:
    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.status = False
        self.__test_connect()

    def __test_connect(self):
        res = self.get_find_list(sql_str='select name from sqlite_master where type="table"')
        if res is None or res == []:
            self.status = False
        else:
            self.status = True

    def __get_conn(self):
        return sqlite3.connect(self.db_file_path)

    def add_one(self, table_name, columns_list, value_list):
        """
        例子：add_one("user", ["user_name", "password"], ["wp", "wp123456"])
        """
        # 连接database
        conn = self.__get_conn()
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()

        if type(value_list[0]).__name__ == 'int' or type(value_list[0]).__name__ == 'float':
            value_list = [str(i) for i in value_list]
        elif type(value_list[0]).__name__ == 'str':
            value_list = ["'" + i + "'" for i in value_list]

        sql_str = "insert into " + table_name + "(gmt_create,gmt_modified," + ",".join(columns_list) + ") values ('" \
                  + time.strftime("%Y-%m-%d %H:%M:%S") + "','" + time.strftime("%Y-%m-%d %H:%M:%S") + "'," \
                  + ",".join(value_list) + ");"
        print(sql_str)
        try:
            # 执行SQL语句
            cursor.execute(sql_str)
            # 提交事务
            conn.commit()
            # 提交之后，获取刚插入的数据的ID
            last_id = cursor.lastrowid
            cursor.close()
            conn.close()
            return last_id
        except Exception as e:
            # 有异常，回滚事务
            conn.rollback()
            cursor.close()
            conn.close()
            return False

    def update_one(self, table_name, set_columns_name_value_list,
                   select_columns_name_value_list):
        """
        例子：update_one("web_password", ["password=2225"], ["account=12", "web_name=12"])
        """
        # 连接database
        conn = self.__get_conn()
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()

        sql_str = "update " + table_name + " set gmt_modified='" + time.strftime("%Y-%m-%d %H:%M:%S") + "'," + \
                  ",".join(set_columns_name_value_list) + " where " + " and ".join(select_columns_name_value_list)

        try:
            # 执行SQL语句
            cursor.execute(sql_str)
            # 提交事务
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            # 有异常，回滚事务
            conn.rollback()
            cursor.close()
            conn.close()
            return False

    def get_find_list(self, sql_str):
        """
        例如: "select * from tsglxt_config_info where info_id=50"
        """
        # 连接database
        conn = self.__get_conn()
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        # 查询数据的SQL语句
        sql = sql_str

        try:
            # 执行SQL语句
            cursor = cursor.execute(sql)
            # 获取多条查询数据
            res_data_list = [i for i in cursor]
            cursor.close()
            conn.close()
            return res_data_list
        except:
            return None

    def create_table(self, create_table_sql_file_path="./myutil/create_table.sql"):
        # 连接database
        conn = self.__get_conn()
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        # 查询数据的SQL语句
        sql = None

        with open(create_table_sql_file_path, "r") as f:
            sql = f.read()
        try:
            for i in sql.split(";"):
                # 执行SQL语句
                cursor = cursor.execute(i)
            cursor.close()
            conn.close()
            return True
        except:
            return False


if __name__ == "__main__":
    sql = sqlite_diver("../test/test.db")
    if not sql.status:
        # 如果这个数据库里面没有表，就按照sql文件创建表
        sql.create_table("./create_table.sql")
        # 创建一个用户
        sql.add_one("user", ["user_name", "password"], ["wp", "wp123456"])

    res = sql.get_find_list("select * from user")
    print(res, "==")

    for i in range(14, 17):
        print(sql.add_one("web_password", ["web_name", "account"], [i, i]))
    res = sql.get_find_list("select * from web_password")
    print(res)

    # sql.update_one("update web_password set password = 2222 where account=12 and web_name=12")
    sql.update_one("web_password", ["password=2225"], ["account=12", "web_name=12"])
    res = sql.get_find_list("select * from web_password")
    print(res)

    sql.update_one("web_password", ["password=2226"], ["account=11", "web_name=11"])
    res = sql.get_find_list("select * from web_password")
    print(res)
