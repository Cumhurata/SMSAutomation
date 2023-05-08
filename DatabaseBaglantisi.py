import cx_Oracle
import Config


class OracleDB:

    def __init__(self):
        cx_Oracle.init_oracle_client(lib_dir=r'C:\instantclient_21_8')
        self.username = Config.username
        self.password = Config.password
        self.dsn = Config.dsn
        self.port = Config.port
        self.encoding = Config.encoding
        self.connection = cx_Oracle.connect(self.username, self.password, self.dsn, encoding=self.encoding)
        self.cursor = self.connection.cursor()

    def select_all(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select(self, table_name, columns, condition):
        query = f"SELECT {columns} FROM {table_name} WHERE {condition}"
        print(query)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, table_name, columns, values):
        query = f"INSERT INTO {table_name} ({columns}) VALUES({values})"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def update(self, table_name, set_values, condition):
        query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def retrieve_first_row(self, table_name, condition):
        query = f"SELECT FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        top_row = self.cursor.fetchone()
        return top_row

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
