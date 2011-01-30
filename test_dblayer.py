import unittest
import dblayer
import sqlite3
import os
import time

TEST_DB_NAME = "test_db.sqlite"

class TestDbLayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        time.sleep(1)
        db.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(TEST_DB_NAME)
    
    def test_average_length_0(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_1(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_2(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_3(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_4(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_5(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_6(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_7(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_8(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    def test_average_length_9(self):
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
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

class TestWriteDbLayer(unittest.TestCase):
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
    
    def test_insert_widget(self):
        db = dblayer.DBLayer(TEST_DB_NAME)
        w = dblayer.Widget(20)
        db.insert_widget(w)
        self.assertEqual(
            7.25, db.average_length()
        )

if __name__ == "__main__":
    unittest.main()
