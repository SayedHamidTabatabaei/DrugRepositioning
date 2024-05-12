import mysql.connector

from configs.config import mysql_host, mysql_user, mysql_password, mysql_database_name


class MySqlRepository:
    def __init__(self):
        self.host = mysql_host
        self.user = mysql_user
        self.password = mysql_password
        self.database = mysql_database_name

        try:
            self.connection = mysql.connector.connect(
                host=mysql_host,
                user=mysql_user,
                password=mysql_password,
                database=mysql_database_name
            )
        except mysql.connector.Error as err:
            self.create_database()
            self.connection = mysql.connector.connect(
                host=mysql_host,
                user=mysql_user,
                password=mysql_password,
                database=mysql_database_name
            )

        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def execute_many_query(self, query, params=None):
        self.cursor.executemany(query, params)
        self.connection.commit()

    def call_procedure(self, procedure_name, args=()):
        self.cursor.callproc(procedure_name, args)
        result = self.cursor.fetchall()
        self.connection.commit()
        return result

    def execute_query_and_return_last_row_id(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.lastrowid

    def execute_many_queries_and_return_last_row_id(self, query, params=None):
        self.cursor.executemany(query, params)
        self.connection.commit()
        return self.cursor.lastrowid

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def commit_connection(self):
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    @staticmethod
    def create_database():
        mydb_for_create = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password
        )

        sql_cursor = mydb_for_create.cursor()

        sql_cursor.execute(f"DROP DATABASE IF EXISTS {mysql_database_name}")
        sql_cursor.execute(f"CREATE DATABASE {mysql_database_name}")
