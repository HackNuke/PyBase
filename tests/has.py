import unittest

from pybase_db import PyBase


class TestPush(unittest.TestCase):
    def test_push(self):
        db = PyBase(database="test_has", db_type="toml", db_path="./has")

        # Insert content to update later
        db.insert(content={
            "users": {
                "1": {
                    "username": "bloodbath",
                    "password": "secret_pass"
                }
            }
        },
                  mode="w")

        print(db.has(key="users.1"))  # True
        print(db.has(key="users.2"))  # False


if __name__ == '__main__':
    unittest.main()
