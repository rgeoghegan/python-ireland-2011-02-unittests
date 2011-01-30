import unittest
import dblayer
import sqlite3
import os
import time
import mock

TEST_DB_NAME = "test_db.sqlite"

class TestDbLayer(unittest.TestCase):
    def setUp(self):
        self.stash = dblayer.sqlite3.connect

        cursor = mock.Mock()
        dblayer.sqlite3.connect = mock.Mock()
        dblayer.sqlite3.connect.return_value.__enter__ = mock.Mock(return_value=cursor)
        dblayer.sqlite3.connect.return_value.__exit__ = mock.Mock(return_value=False)

    def tearDown(self):
        dblayer.sqlite3.connect = self.stash

    @mock.patch("dblayer.sqlite3.connect")
    def test_average_length(self, connect):
        cursor = mock.Mock()
        connect.return_value.__enter__ = mock.Mock(return_value=cursor)
        connect.return_value.__exit__ = mock.Mock(return_value=False)
        cursor.execute.return_value.fetchone.return_value = (11, 67.0)
        
        db = dblayer.DBLayer(TEST_DB_NAME)

        self.assertAlmostEqual(
            6.090909, db.average_length(),
            places=4
        )

    @mock.patch("dblayer.sqlite3.connect")
    def test_report(self, connect):
        cursor = mock.Mock()
        connect.return_value.__enter__ = mock.Mock(return_value=cursor)
        connect.return_value.__exit__ = mock.Mock(return_value=False)
        cursor.execute.return_value.fetchone.return_value = (11, 1.0, 12.0, 67.0)

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

    @mock.patch("dblayer.sqlite3.connect")
    def test_insert_widget(self, connect):
        cursor = mock.Mock()
        connect.return_value.__enter__ = mock.Mock(return_value=cursor)
        connect.return_value.__exit__ = mock.Mock(return_value=False)
        cursor.execute.return_value.fetchone.return_value = (12, 87.0)

        db = dblayer.DBLayer(TEST_DB_NAME)
        w = dblayer.Widget(20)
        db.insert_widget(w)
        self.assertEqual(
            7.25, db.average_length()
        )

if __name__ == "__main__":
    unittest.main()
