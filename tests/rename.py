import unittest
from pybase_db import PyBase


class TestPush(unittest.TestCase):
    def test_push(self):
        db = PyBase(database="test_rename", db_type="json", db_path="./rename")

        # Insert content to rename later
        db.insert(content={"unsupportedLanguages": ["json", "yaml", "bytes"]},
                  mode="w")

        db.rename(key="unsupportedLanguages", new_name="supportedLanguages")

        print(db.get())


if __name__ == '__main__':
    unittest.main()
