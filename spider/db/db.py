import pymysql

import config
from logger import SpiderLogger


class Mysql(object):
    def __init__(self, db):
        self.host = config.get("mysql", "host")
        self.port = config.get("mysql", "port")
        self.user = config.get("mysql", "user")
        self.password = config.get("mysql", "password")
        self.charset = config.get("mysql", "charset")
        self.db = db
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = pymysql.Connect(
                host=self.host,
                port=self.port,
                user=self.user,
                db=self.db,
                charset=self.charset
            )
        except Exception as ex:
            SpiderLogger().logging.error("database[%s] connect is fail, ex[%s]" % (self.db, ex))
            return False
        self.cur = self.conn.cursor()
        SpiderLogger().logging.info("database[%s] connect is ok" % self.db)
        return True

    def close(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    def execute_and_commit(self, sql, params=None):
        self.connect()
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as ex:
            SpiderLogger().logging.error("sql execute error, sql[%s] params[%s] ex[%s]" % (sql, params, ex))
            return False
        finally:
            self.close()
        return True

    def execute_not_commit(self, sql, params=None):
        self.connect()
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
        except Exception as ex:
            SpiderLogger().logging.error("sql execute error, sql[%s] params[%s] ex[%s]" % (sql, params, ex))
            return False
        finally:
            self.close()
        return True

    def fetchall(self, sql, params=None):
        self.execute_not_commit(sql, params)
        return self.cur.fetchall()


if __name__ == '__main__':
    Mysql("db").execute_not_commit("select * from %s", "product")
