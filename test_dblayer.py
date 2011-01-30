import unittest
import dblayer
import sqlite3
import os

TEST_DB_NAME = "test_db.sqlite"

class TestDbLayer(unittest.TestCase):
    def setUp(self):
        db = sqlite3.connect(TEST_DB_NAME)
        with db as cursor:
            cursor.execute("""
                CREATE TABLE widgets (
                    length REAL
                );""")
            for l in range(1,11) + [12]:
                cursor.execute("""
                    INSERT INTO widgets (length)
                        VALUES (?);
                    """, (l,)
                )
            cursor.commit()
        db.close()

    def tearDown(self):
        os.remove(TEST_DB_NAME)
    
    def test_average_length(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_insert_widget(self):
        db = dblayer.DBLayer(TEST_DB_NAME)
        w = dblayer.Widget(20)
        db.insert_widget(w)
        self.assertEqual(
            7.25, db.average_length()
        )

    def test_report(self):
        db = dblayer.DBLayer(TEST_DB_NAME)
        self.assertMultiLineEqual("""
Consolidated Widget Report
--------------------------

Average length: 6.09
Maximum length: 12.00
Minimum length: 1.00
""",
            db.report()
        )

if __name__ == "__main__":
    unittest.main()
