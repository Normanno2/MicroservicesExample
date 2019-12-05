from tornado.web import RequestHandler
import pymysql
import os

class HelloDBHandler(RequestHandler):

    def get(self):
        print("HELLO ALL")

        host = "" if os.environ["db_host"] is None else str(os.environ["db_host"])
        user = "" if os.environ["db_username"] is None else str(os.environ["db_username"])
        password = "" if os.environ["db_pass"] is None else str(os.environ["db_pass"])
        port = 3306 if os.environ["db_port"] is None else int(os.environ["db_port"])
        database = "" if os.environ["db_database"] is None else str(os.environ["db_database"])
        connection = None

        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=database,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        
            print("Get")
            sql = "SELECT name FROM people"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                for p in result:
                    self.write("Hello "+p["name"]+"</br>")
        except Exception as ex:
            self.write("Hello DB FAILED")
            self.write(str(ex))
        finally:
            if connection is not None:
                connection.close()


class HelloNewDBHandler(RequestHandler):

    def get(self, mate):
        print("New db handler")
        host = "" if os.environ["db_host"] is None else str(os.environ["db_host"])
        user = "" if os.environ["db_username"] is None else str(os.environ["db_username"])
        password = "" if os.environ["db_pass"] is None else str(os.environ["db_pass"])
        port = 3306 if os.environ["db_port"] is None else int(os.environ["db_port"])
        database = "" if os.environ["db_database"] is None else str(os.environ["db_database"])
        connection = None
        
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=database,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        
            print("Get")
            sql = "INSERT INTO `people` (`name`) VALUES (%s)"
            with connection.cursor() as cursor:
                cursor.execute(sql, (str(mate)))
            
            connection.commit()
            self.write("Hello "+str(mate))
        except Exception as ex:
            self.write("Hello DB FAILED")
            self.write(str(ex))
        finally:
            if connection is not None: 
                connection.close()
        