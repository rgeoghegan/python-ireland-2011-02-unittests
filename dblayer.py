import sqlite3

class Widget(object):
    def __init__(self, length):
        self.length = length

class DBLayer(object):
    def __init__(self, conn_string):
        self.conn = sqlite3.connect(conn_string)

    def average_length(self):
        with self.conn as cursor:
            count, sum_l = cursor.execute("""
                SELECT COUNT(length), SUM(length)
                FROM widgets;""").fetchone()
            return sum_l / float(count)

    def insert_widget(self, widget):
        with self.conn as cursor:
            cursor.execute("""
                INSERT INTO widgets (length)
                    VALUES (?);
                """, (widget.length,)
            )
            cursor.commit()

    def report(self):
        with self.conn as cursor:
            count, min_l, max_l, sum_l = cursor.execute("""
                SELECT COUNT(length), MIN(length), MAX(length), SUM(length)
                    FROM widgets;""").fetchone()
            return ("""
Consolidated Widget Report
--------------------------

Average length: %.2f
Maximum length: %.2f
Minimum length: %.2f
""" % (sum_l/float(count), max_l, min_l))

            
            
