import pymysql
from helpers.loggerbase import log

class UpDao:
    # Connect to the database
    def __init__(self):
        self._host = 'localhost'
        self._user = 'root'
        self._password = 'qwerty123'
        self._db = 'up'
        self.connection = None
        self.connect()

    def __del__(self):
        if self.connection:
            self.connection.close()

    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise Exception("Not connected to DB")

    def commit_transaction(self):
        if self.connection:
            self.connection.commit()
            log.debug("Transaction committed")
        else:
            log.error("Not connected to DB")

    def connect(self):
        self.connection = pymysql.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            db=self._db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def get_record_by_id(self, id):
        try:
            with self.get_cursor() as cursor:
                query = "SELECT * FROM `uploadRecords` WHERE id = %s"
                cursor.execute(query, (id,))

                result = cursor.fetchone()
                print(result)
        except Exception as e:
            log.error(f"DB Exception : {e}")

    def get_all_records(self):
        try:
            with self.get_cursor() as cursor:
                query = "SELECT * FROM `uploadRecords`"
                cursor.execute(query)

                result = cursor.fetchall()
                print(result)
        except Exception as e:
            log.error(f"DB Exception : {e}")

if __name__ == '__main__':
    log.info("Testing DB")
    dao = UpDao()
    dao.get_record_by_id(1)
    log.info("")
    dao.get_all_records()