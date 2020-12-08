import unittest
from pybase_db.pybase_db import PyBase


class TestDelete(unittest.TestCase):
    def test_delete(self):
        db = PyBase(database="test_delete", db_type="json", db_path="./delete")

        # Insert content to update later
        db.insert(content={
            "supportedLanguages": ["json", "yaml", "bytes"],
            "unsupportedLanguages": ["toml"]
        },
                  mode="w")

        db.delete("unsupportedLanguages")

        print(db.get())


if __name__ == '__main__':
    unittest.main()
