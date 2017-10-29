import MySQLdb


class MySqlWrapper(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="mysql-486830.vipserv.org", user="destyl_hack",
                                            passwd="pal1nka#", db="destyl_hack", charset='utf8')

    def fetch_rows_from_query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
