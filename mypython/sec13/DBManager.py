import mysql.connector


class DBManager:
    def __init__(self, user: str, password: str, database: str, host='127.0.0.1', raise_on_warnings=False) -> None:
        self.config = {'user': user,
                       'password': password,
                       'database': database,
                       'host': host,
                       'raise_on_warnings': raise_on_warnings}
        self.conn = None

    # DB 접속
    def connect_database(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            print("Database connect")
        except mysql.connector.Error as error:
            self.conn = None
            print({error})

    # DB에 테이블 생성 dict 로 받아서 CREATE 문 자동 생성
    """
    table_dict = {
        'id': 'INT PRIMARY KEY AUTO_INCREMENT',
        'image_name': 'VARCHAR(255)',
        'image_data': 'MEDIUMBLOB'
    }
    """

    def create_table(self, table_name: str, table_dict: dict):
        if self.conn is not None:
            create_str = "CREATE TABLE IF NOT EXISTS " + table_name + " "
            create_str += self.__get_create_table_str(table_dict)
            print(create_str)

            cursor = self.conn.cursor()
            try:
                cursor.execute(create_str)
                self.conn.commit()
            except mysql.connector.Error as error:
                print({error})
            finally:
                cursor.close()
        else:
            print("Database Not connect")

    # DB에 data INSERT -> dict 로 받아서 INSERT 문 자동 생성
    """
    insert_dict = {
            'image_name': image,
            'image_data': image_file
        }
    """
    def insert_data(self, table_name: str, insert_dict: dict):
        if self.conn is not None:
            insert_str = "INSERT INTO " + table_name + " "
            insert_str += self.__get_dict_keys_str(insert_dict)
            insert_str += " VALUES "
            insert_str += self.__get_placeholder_str("%s", len(insert_dict.keys()))

            print(insert_str)

            cursor = self.conn.cursor()
            try:
                cursor.execute(insert_str, tuple(insert_dict.values()))  #
                self.conn.commit()
            except mysql.connector.Error as error:
                print({error})
            finally:
                cursor.close()
        else:
            print("Database Not connect")

    # DB에 data SELECT - TODO : select_where() - WHERE 절 추가 메소드
    def select_all(self, table_name: str):
        if self.conn is not None:
            cursor = self.conn.cursor()
            try:
                cursor.execute(f"SELECT * FROM {table_name}")
                return cursor.fetchall()
            except mysql.connector.Error as error:
                print({error})
            finally:
                cursor.close()
        else:
            print("Database Not connect")

    # 테이블 삭제
    def drop_table(self, table_name: str):
        if self.conn is not None:
            cursor = self.conn.cursor()
            try:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            except mysql.connector.Error as error:
                print({error})
            finally:
                cursor.close()
        else:
            print("Database Not connect")

    # CREATE 문 자동 생성
    def __get_create_table_str(self, table_dict: dict):
        _table_str = "("
        for _key, _value in table_dict.items():
            _table_str += _key + " " + _value + ", "
        _table_str = _table_str[:-2]
        _table_str += ")"
        return _table_str

    # INSERT 문 필드명 추출 (image_name, image_data)
    def __get_dict_keys_str(self, dict_data: dict):
        return tuple(dict_data.keys()).__str__().replace("'", "")

    # INSERT 문 placeholder 추출 (%s, %s) -> 향후 Mysql, Sqlite 호환을 위해 placeholder 매개 변수로 '%s' , '?' 지정함
    def __get_placeholder_str(self, placeholder, dict_key_count):
        placeholder_str = "("
        for i in range(0, dict_key_count):
            placeholder_str += placeholder
            if i < dict_key_count - 1:  placeholder_str += ', '
        placeholder_str += ')'
        return placeholder_str

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
