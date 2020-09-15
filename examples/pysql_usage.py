# NTBBloodbath | PyBase v0.4.0
# Usage example file (for v0.4.0).

# To analyze the data within SQLite3 run these commands:
# $ sqlite3 example.db
# sqlite> .headers on
# sqlite> .mode column
# sqlite> SELECT * FROM users;

# Lets import PySQL Class from PyBase Package
from pybase_db.pysql import PySQL

# Lets define our database name (with default db_path).
# We can activate Debugging by setting debug to True.
db = PySQL(database = "example", debug = True)

# Lets create a table called users with two columns;
# username and languages and their values.
db.create(objects = {
    "table": {
        "name": "users",
        "columns": {
            "username": {
                "type": "text",
                "value": ["bloodbath", "danny", "paco", "unknown"]
            },
            "password": {
                "type": "text",
                "value": "mypass1"
            },
            "email": {
                "type": "text",
                "value": ["email@email.xyz", "email@email.zyx", "email@gmail.com"]
            },
            "languages": {
                "type": "text", 
                "value": ["Ruby", "Python", "JavaScript"]
            },
        }
    }
})
#
# Lets delete the value JavaScript from languages table in users table.
db.delete(table = "users", objects = {
    "column": "languages",
    "value": "JavaScript"
})
#
# Lets get the value "Ruby" from the "languages" column in "users" table.
getData = db.get(table = "users", objects = {
    "column": "languages",
    "value": "Ruby"
})
# 
# Lets delete the entire table.
db.delete(table = "users")
