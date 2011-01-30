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


    def probability(self, value):
        with self.conn as cursor:
            result = cursor.execute("""
                SELECT all_w.count, more_w.count
                    FROM
                        (SELECT COUNT(*) AS count FROM widgets) AS all_w,
                        (SELECT COUNT(*) AS count FROM widgets WHERE length >= ?) AS more_w;
            """, (value,)).fetchone()
            return result[1] / float(result[0])

    def insert_widget(self, widget):
        with self.conn as cursor:
            cursor.execute("""
                INSERT INTO widgets (length)
                    VALUES (?);
                """, (widget.length,)
            )
            cursor.commit()
