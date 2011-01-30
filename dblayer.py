import sqlite3

class Widget(object):
    def __init__(self, length):
        self.length = length

class DBLayer(object):
    def __init__(self, conn_string):
        self.conn = sqlite3.connect(conn_string)

    def average_length(self):
        with self.conn as cursor:
            result = cursor.execute("""
                SELECT COUNT(length), SUM(length)
                FROM widgets;""").fetchone()
            return result[1] / result[0]

    def insert_widget(self, widget):
        with self.conn as cursor:
            cursor.execute("""
                INSERT INTO widgets (length)
                    VALUES (?);
                """, (widget.length,)
            )
            cursor.commit()
