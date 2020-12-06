import unittest
from pybase_db import PyBase

class TestPush(unittest.TestCase):
    def test_push(self):
        db = PyBase(database="test_push", db_type="toml", db_path="./push")

        # Insert content to update later
        db.insert(content={
            "supportedLanguages": ["json", "yaml", "bytes"]
        }, mode="w")

        db.push(key="supportedLanguages", element="toml")

        print(db.get("supportedLanguages"))

if __name__ == '__main__':
    unittest.main()
