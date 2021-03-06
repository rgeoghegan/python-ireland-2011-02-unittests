import unittest
import dblayer

class TestDbLayer(unittest.TestCase):
    def test_average_length(self):
        db = dblayer.DBLayer("test.sqlite")

        self.assertEqual(
            6.090909, db.average_length()
        )

    def test_insert_widget(self):
        db = dblayer.DBLayer("test.sqlite")
        w = dblayer.Widget(20)
        db.insert_widget(w)
        self.assertEqual(
            7.25, db.average_length()
        )

    def test_report(self):
        db = dblayer.DBLayer("test.sqlite")
        self.assertEqual("""
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
